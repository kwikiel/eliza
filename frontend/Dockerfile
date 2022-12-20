FROM node:19-bullseye-slim
COPY . /app
WORKDIR /app
ENV NODE_OPTIONS=--openssl-legacy-provider
RUN npm install
RUN npm run build
CMD ["serve","-s", "build"]