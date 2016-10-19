############################################################
# Dockerfile to build Python Flask Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Alessandro Piccolo, Andrea Rylander & Abdullah Al Hinai

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

#Install RabbitMQ-server
RUN apt-get install -y rabbitmq-server

# Install octave
RUN apt-get install -y octave

# Upgrade
RUN apt-get -y upgrade

# Export local variable (obscure error)
RUN export LC_ALL=C

# Export local variable (obscure error)
RUN export LC_ALL=C

# Get pip to download and install requirements:
RUN pip install flask
RUN pip install oct2py
RUN pip install celery
RUN pip install pygal

#Install celery-common
RUN apt install -y python-celery-common
#Install scipy
RUN apt-get install -y python-scipy

# Export local variable (obscure error)
RUN export LC_ALL=C
RUN export C_FORCE_ROOT="true"

# Expose ports
EXPOSE 80

# Download awsome repository
RUN git clone https://github.com/AndreaRylander/Cloudgroup11.git /home/Cloudgroup11

# Run celery with sudo 
RUN export C_FORCE_ROOT="true"

# Set the default directory where CMD will execute
WORKDIR /home/Cloudgroup11/application-files/

