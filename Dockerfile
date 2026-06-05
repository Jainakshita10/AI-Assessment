# =========================
# 1️⃣ Builder Stage
# =========================
FROM python:3.12-slim-bookworm AS builder

ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     gcc \
#     libffi-dev \
#     libssl-dev \
#     && rm -rf /var/lib/apt/lists/*

# Create a virtual environment in /venv
RUN python -m venv /venv

# Ensure our venv Python is the default
ENV PATH="/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency files first (for caching)
COPY ./requirements.txt .

# Upgrade pip & install dependencies into a temp directory
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

# =========================
# 2️⃣ Final Runtime Stage
# =========================
FROM python:3.12-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive
# Set working directory
WORKDIR /app

# Copy the virtual environment from builder
COPY --from=builder /venv /venv

# Ensure our venv Python is the default
ENV PATH="/venv/bin:$PATH"

# Install only runtime dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libffi8 \
#     libssl3 \
#     bash \
#     && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group
RUN groupadd --system appuser && useradd --system --create-home --gid appuser appuser

# Copy only necessary project files
COPY ./pages ./pages
COPY ./media ./media
COPY ./app.py ./app.py
COPY ./questions.py ./questions.py
COPY ./utils.py ./utils.py
COPY ./config.py ./config.py
COPY ./AI_App_data_sample.xlsx ./AI_App_data_sample.xlsx
COPY ./database.py ./database.py

# unzip chromadb
# RUN apt update && apt install unzip && unzip chroma_data.zip

# Copy project files & set ownership to non-root user
# Ensure startup.sh is executable
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Run the startup script
CMD ["streamlit", "run", "app.py", "--server.port", "8000", "--server. Address", "0.0.0.0"]