# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install git and basic utilities
RUN apt-get update && \
    apt-get install -y git curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install CPU-only PyTorch
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set Python path so backend is discoverable
ENV PYTHONPATH=/app

# Expose Gradio default port
EXPOSE 7860

# Run the Gradio app
CMD ["python3", "ui/app.py"]