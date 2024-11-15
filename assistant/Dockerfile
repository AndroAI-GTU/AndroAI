# We create a base image using the latest version of the RASA SDK
FROM rasa/rasa-sdk:latest

# We set the working directory
WORKDIR /app

# We copy the necessary files
COPY actions /app/actions
COPY actions/requirements.txt /app/requirements.txt

# We install the necessary dependencies with root privileges
USER root
RUN pip install --no-cache-dir -r /app/requirements.txt

# Back to normal user from root
USER 1001

ARG ACTION_SERVER_PORT
ENV ACTION_SERVER_PORT=$ACTION_SERVER_PORT
EXPOSE $ACTION_SERVER_PORT

# We start the action server
CMD ["start", "--actions", "actions"]
