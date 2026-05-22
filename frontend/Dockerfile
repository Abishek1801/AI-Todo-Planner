# ─────────────────────────────────────────────────────────────────
# Frontend Dockerfile — React + Vite dev server
# ─────────────────────────────────────────────────────────────────
# Build context: ./frontend
# This runs the Vite development server with hot module replacement
# In production this would build static files and serve via Nginx
# ─────────────────────────────────────────────────────────────────

# Base image — Node 20 LTS on minimal Alpine Linux
# alpine keeps the image very small
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /app

# ── Install Node dependencies ─────────────────────────────────────
# Copy package files FIRST for layer caching
# npm install only re-runs when package.json or package-lock.json changes
COPY package*.json ./
RUN npm install

# ── Copy application code ─────────────────────────────────────────
# Copied after npm install for optimal caching
# In development, docker-compose volume mount overlays this
# so edits in VS Code hot-reload in the browser instantly
COPY . .

# ── Expose the Vite dev server port ──────────────────────────────
EXPOSE 5173

# ── Start Vite dev server ─────────────────────────────────────────
# --host 0.0.0.0 makes it reachable from outside the container
# Without --host, the browser on your Mac can't reach it
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]