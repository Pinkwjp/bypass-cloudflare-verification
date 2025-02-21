
# Specify the base image
FROM python:3.10.16-slim  

# Set the working directory
WORKDIR /app

# Copy the requirements file and pipfile into the image
COPY requirements.txt Pipfile Pipfile.lock /app/

# Copy images(pictures) used by pyautogui into the image
COPY ./images /app/

