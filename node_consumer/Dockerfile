FROM node:8-alpine

RUN apk --no-cache add \
      bash \
      g++ \
      ca-certificates \
      lz4-dev \
      musl-dev \
      cyrus-sasl-dev \
      openssl-dev \
      make \
      python

RUN apk add --no-cache --virtual .build-deps gcc zlib-dev libc-dev bsd-compat-headers py-setuptools bash

# Create app directory
RUN mkdir -p /opt

# Move to the app directory
WORKDIR /opt

# Install node-rdkafka
RUN npm install node-rdkafka
# Copy package.json first to check if an npm install is needed
COPY package.json package.json
RUN npm install

COPY . .

CMD ["npm", "start"]
