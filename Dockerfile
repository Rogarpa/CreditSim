FROM node:20-alpine

WORKDIR /app
RUN npm install -g serve

COPY ./html ./static_front

EXPOSE 5000
CMD ["serve", "-s", "static_front", "-l", "5000"]
