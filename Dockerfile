# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port your Flask app will run on
EXPOSE 80

# Start the Flask application
CMD ["python", "app.py"]
