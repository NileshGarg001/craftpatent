FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set PYTHONPATH to ensure proper module discovery
ENV PYTHONPATH=/app

# Set environment variables
ENV GOOGLE_GENAI_USE_VERTEXAI=TRUE
ENV GOOGLE_CLOUD_PROJECT=craft-patent
ENV GOOGLE_CLOUD_LOCATION=us-central1
ENV GOOGLE_CLOUD_STAGING_BUCKET=gs://craftpatent

# Expose port
EXPOSE 8080

# Run the ADK web server
CMD ["adk", "web", ".", "--host", "0.0.0.0", "--port", "8080"]
