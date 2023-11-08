FROM debian:stretch
 
# Setting working directory
WORKDIR /app

COPY . /app

# Installing necessary dependencies
RUN apt-get update && apt-get install -y python3 python3-pip sakis3g
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
