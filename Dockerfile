FROM ubuntu:24.04

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Install the dependencies
RUN apt-get -y install libopencv-dev

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy the application files
COPY src/ ./src/

# Set the command to run the application
CMD ["python3", "src/main.py", "--nogui"]