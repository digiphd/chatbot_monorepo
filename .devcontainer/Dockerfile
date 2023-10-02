# Use an official Python as a parent image
FROM python:3.11 as base

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm separately
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y npm

# Debug: Print PATH and npm location
RUN echo $PATH
RUN which npm

# For Python backend
WORKDIR /workspace/api

# Copy requirements file and install dependencies
COPY api/requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pylint black

# For Node.js frontend
WORKDIR /workspace/frontend
COPY frontend/package.json .

# Install Node.js dependencies
RUN npm install

# Expose the ports that your app uses. For example, Python API and Next.js frontend
EXPOSE 8000 3000

# Change back to root
WORKDIR /workspace/

# Copy start-dev.sh and make it executable
COPY start-dev.sh /workspace/start-dev.sh
RUN chmod +x /workspace/start-dev.sh

# Use start-dev.sh as the entrypoint
ENTRYPOINT ["/workspace/start-dev.sh"]
