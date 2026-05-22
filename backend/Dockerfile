# ─────────────────────────────────────────────────────────────────
# Backend Dockerfile — FastAPI + Uvicorn
# ─────────────────────────────────────────────────────────────────
# Build context: ./backend
# This image is built once and rebuilt only when you change
# requirements.txt or the Dockerfile itself
# ─────────────────────────────────────────────────────────────────

# Base image — Python 3.11 on minimal Debian
# slim keeps the image small by excluding unnecessary system packages
FROM python:3.11-slim

# Set the working directory inside the container
# All subsequent commands run from here
# Your code will live at /app inside the container
WORKDIR /app

# ── Install system dependencies ───────────────────────────────────
# These are OS-level packages some Python libraries need to compile
# --no-install-recommends keeps the image lean
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# ── Install Python dependencies ───────────────────────────────────
# Copy requirements FIRST — before copying your app code
# This way Docker caches this layer and only re-runs pip install
# when requirements.txt actually changes (not on every code change)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy application code ─────────────────────────────────────────
# Copied after dependencies for optimal layer caching
# In development, the docker-compose volume mount overlays this
# so live code changes work without rebuilding the image
COPY . .

# ── Expose the port ───────────────────────────────────────────────
# Documents that this container listens on port 8000
# The actual port mapping is handled in docker-compose.yml
EXPOSE 8000

# ── Start the server ──────────────────────────────────────────────
# --host 0.0.0.0 makes it reachable from outside the container
# --reload watches for code changes and restarts automatically
# --reload only in development — we remove it for production later
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]