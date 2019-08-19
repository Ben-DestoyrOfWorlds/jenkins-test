# Use an official Python runtime as a parent image
FROM python:3.5.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Docker/ /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME jenkins-test

