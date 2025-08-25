FROM python:3.8-slim

WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy local files
COPY calculator.py .

# Run the app
CMD ["python", "calculator.py"]
