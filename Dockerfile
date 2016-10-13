############################################################
# Dockerfile to build Python Flask Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
#MAINTAINER Maintaner Name what does this do : )?

# Add the application resources URL
#RUN echo deb http://download.fpcomplete.com/ubuntu xenial main|sudo tee /etc/apt/sources.list.d/fpco.list
RUN sudo echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# Update the sources list
RUN sudo apt-get update

# Install basic applications
RUN sudo apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN sudo apt-get install -y python python-dev python-distribute python-pip

RUN git clone https://github.com/AndreaRylander/Cloudgroup11.git

# Get pip to download and install requirements:
RUN sudo pip install -r Cloudgroup11/test_application/requirements.txt

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR Cloudgroup11/test_application

# Set the default command to execute
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python app.py
