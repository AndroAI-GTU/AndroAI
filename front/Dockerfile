# Base image
FROM debian:buster

# We install Node.js
RUN apt-get update && \
    apt-get install -y gnupg curl && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_21.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install -y nodejs

# Uupdating npm
RUN npm install -g npm

# We create the working directory
RUN mkdir /app
WORKDIR /app

# We copy the project files
COPY . .

# Instaling dependincies
RUN npm install

# We make the entry point file executable
RUN chmod +x /app/entrypoint.sh

# We open the port required for the application
EXPOSE ${FRONT_PORT}

# We set entrypoint.sh as entry point
ENTRYPOINT ["sh", "entrypoint.sh"]
