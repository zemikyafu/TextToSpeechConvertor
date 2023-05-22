# FROM alpine:3.14.0
# RUN apk --no-cache add python3
# # ADD repositories /etc/apk/repositories
# RUN mkdir /textToSpeech
# WORKDIR /textToSpeech 
# COPY . .
# RUN apk --update add --no-cache python3 py3-pip
# RUN pip install azure-cognitiveservices-speech
# RUN pip install boto3
# # RUN apk --no-cache add boto3
# RUN pip install Flask-Cors
# RUN pip install flask
# RUN pip install requests



# RUN apk add --no-cache bash
# EXPOSE 5002
# CMD ["python3", "translator.py","run","--host=0.0.0.0"]


#########################################################################
# Use Alpine base image
# FROM python:3.8-alpine

# # Set working directory
# RUN mkdir /textToSpeech
# WORKDIR /textToSpeech 

# # Install required dependencies
# RUN apk --no-cache add  gcc  musl-dev  linux-headers  libffi-dev openssl-dev

# # Install Azure Cognitive Services SDK
# RUN pip install azure-cognitiveservices-speech

# # Copy your application code to the container
# COPY . .

# RUN apk add --no-cache bash
# EXPOSE 5002
# CMD ["python3", "translator.py","run","--host=0.0.0.0"]

################################################################
# Use Alpine base image
# FROM python:3.8-alpine

# # Set working directory
# WORKDIR /app

# # Install required dependencies
# RUN apk --no-cache add \
#     gcc \
#     musl-dev \
#     linux-headers \
#     libffi-dev \
#     openssl-dev

# # Install Azure Cognitive Services SDK
# RUN pip install azure-cognitiveservices-speech

# # Copy your application code to the container
# COPY . .

# # Set the entry point command
# CMD ["python", "your_script.py"]


FROM python:3.8
# FROM alpine:latest
# Set working directory
RUN mkdir /textToSpeech
WORKDIR /textToSpeech 
COPY . .
# Install dependencies

RUN pip install Flask-Cors
RUN pip install flask
RUN pip install requests
RUN pip install boto3
RUN pip install azure-cognitiveservices-speech
# RUN apk add --no-cache bash
EXPOSE 5003
CMD ["python3", "textToSpeech.py","run","--host=0.0.0.0"]