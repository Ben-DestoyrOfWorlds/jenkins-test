# Use an official Python runtime as a parent image
FROM python:3.7.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80 

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME jenkins-test

# Run app.py when the container launches
CMD ["python", "app.py"]
