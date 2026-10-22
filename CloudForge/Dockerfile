FROM python:3.11-slim

WORKDIR /app

# Upgrade base tooling
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements and install
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip uninstall -y setuptools

# Copy source code (filtered by .dockerignore)
COPY . .

# Enforce non-root execution
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /bin/sh appuser && \
    chown -R appuser:appgroup /app

USER 10001

EXPOSE 5000

ENV HOST=0.0.0.0
ENV PORT=5000

CMD ["python", "app/app.py"]