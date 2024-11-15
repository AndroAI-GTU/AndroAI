# Based on the official Python image
FROM python:3.10

# We set the working directory
WORKDIR /app

COPY requirements.txt requirements.txt
COPY conversationServer.py conversationServer.py

# We install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
ARG FLASK_PORT
ENV FLASK_PORT=${FLASK_PORT}
EXPOSE ${FLASK_PORT}

# Command to run Flask server
CMD ["python3", "conversationServer.py"]
