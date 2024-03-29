# Use an official Python runtime as a parent image
FROM python:3.7.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Docker/ /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME jenkins-test

# Make port 5000 available to the world outside this container
EXPOSE 80 

# Run app.py when the container launches
CMD ["python", "app.py"]

