# Use an official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Default command to run the dev server (for local dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
