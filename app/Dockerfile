# Use the official Python image as a base
FROM python:3.10.6-slim

# Set the working directory to /app
WORKDIR /app

# Update package lists and install pip
RUN apt-get update -y && \
    apt-get install -y python3-pip

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the Flask application
EXPOSE 8000

# Define the command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
