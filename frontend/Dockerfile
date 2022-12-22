FROM node:19-bullseye-slim
COPY package.json package-lock.json /app/
WORKDIR /app
ENV NODE_OPTIONS=--openssl-legacy-provider
RUN npm install
RUN npm install -g serve
COPY . /app/
RUN ls -la
RUN npm run build
CMD ["serve","-s", "build"]