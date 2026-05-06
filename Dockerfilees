# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies (if pygame used)
RUN pip install pygame

# Run app
CMD ["python", "shootthefruit.py"]
