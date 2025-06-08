FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

ARG VITE_API_URL

ENV VITE_API_URL=$VITE_API_URL

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
