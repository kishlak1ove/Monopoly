FROM node:alpine AS build

WORKDIR /usr/src/app

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine

COPY --from=build /usr/src/app/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]