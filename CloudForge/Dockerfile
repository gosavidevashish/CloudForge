FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Upgrade base tooling to clean versions
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install production dependencies
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip uninstall -y setuptools

# Copy application source
COPY . .

# Create and switch to non-root user (matches Kubernetes securityContext user 10001)
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /bin/sh appuser && \
    chown -R appuser:appgroup /app

USER 10001

EXPOSE 5000

ENV HOST=0.0.0.0
ENV PORT=5000

CMD ["python", "app/app.py"]