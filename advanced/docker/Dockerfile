# This is the base image for the example_docker advanced example cloud execution
FROM ubuntu:22.04
WORKDIR /

# Configure apt
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa

# Install python3.9
RUN apt-get update -y && apt-get install -y python3.9
RUN rm /usr/bin/python3
RUN ln -s /usr/bin/python3.9 /usr/bin/python3
RUN ln -s /usr/bin/python3.9 /usr/bin/python

# Install pip3
RUN apt-get update -y && apt-get install -y python3-pip
RUN apt-get update -y && apt-get install --reinstall -y python3.9-distutils

# Install all pipeline requirements, including Sematic itself
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt

# Copy the data files
COPY advanced/data/message.txt advanced/data/message.txt

# Copy the pipeline source files
COPY advanced/*.py advanced/
