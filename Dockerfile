# Use an official Debian stretch image
FROM debian:stretch

# Set the working directory
WORKDIR /app

# Copy only the necessary files for setup
COPY requirements.txt /app/

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip sakis3g && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Copy the entire project
COPY . /app/


# Expose any needed ports
EXPOSE 80

# Define the command to run your application
CMD ["sh", "start.sh"]
