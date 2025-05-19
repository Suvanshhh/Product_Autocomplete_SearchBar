FROM node:18

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

# Install a lightweight server to serve the build
RUN npm install -g serve

EXPOSE 5173

CMD ["serve", "-s", "dist", "-l", "5173"]
