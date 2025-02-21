
# Specify the base image
FROM python:3.10.16-slim  

# Set the working directory
WORKDIR /app

# Copy the requirements file and pipfile into the image
COPY requirements.txt Pipfile Pipfile.lock /app/

# Add images(pictures used by pyautogui) folder into the image
ADD images /app/

# Add the application code into the image
ADD src /app/

# Install the Python dependencies in the image
# This is slow, about 240 seconds, mostly because of pyautogui
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "src/app.py"]
