# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY ip-tool.py /app/ip-tool.py

# Install necessary dependencies
RUN apt-get update && apt-get install -y iproute2 && rm -rf /var/lib/apt/lists/*

# Set the default command to execute the script
ENTRYPOINT ["python", "ip-tool.py"]
