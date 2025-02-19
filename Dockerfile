# Use official Python image as a base
#FROM python:3.11
#FROM public.ecr.aws/docker/library/python:3.11
#FROM python:3.11-slim
FROM public.ecr.aws/docker/library/python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 8080

# Set environment variable for Flask
ENV FLASK_APP=application.py

# Command to run the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "application:application"]
