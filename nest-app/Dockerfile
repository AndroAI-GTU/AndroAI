# Base image
FROM node:18

# Create app directory
WORKDIR /usr/src/app

RUN mkdir /files_to_compile /apk_files

# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./

# Install app dependencies
RUN npm install
RUN npm install axios @types/axios
RUN npm install dotenv

# Expose port
ARG BACK_PORT
ENV BACK_PORT=${BACK_PORT}
EXPOSE ${BACK_PORT}

# Bundle app source
COPY . .

# Creates a "dist" folder with the production build
RUN npm run build

# Start the server using the production build
CMD [ "node", "dist/main.js" ]
