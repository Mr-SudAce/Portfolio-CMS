# Use official Python image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "run.py"]
