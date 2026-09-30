FROM nginx:alpine

LABEL maintainer="maazghufran@example.com"
LABEL version="1.0"
LABEL description="Optimized web application for Docker lab"

COPY src/index.html /usr/share/nginx/html/

RUN echo 'server { \
    listen 80; \
    server_name localhost; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html; \
    } \
    add_header X-Frame-Options "SAMEORIGIN" always; \
    add_header X-Content-Type-Options "nosniff" always; \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
