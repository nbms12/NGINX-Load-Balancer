# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
