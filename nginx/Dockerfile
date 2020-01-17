#FROM digitalocean.com/alpine:latest
#FROM alpine:3.10.3
#
#LABEL MAINTAINER="Tezzy O."
#
#RUN apk --update add nginx && \
#    ln -sf /dev/stdout /var/log/nginx/access.log && \
#    ln -sf /dev/stderr /var/log/nginx/error.log && \
#    mkdir /etc/nginx/sites-enabled/ && \
#    mkdir -p /run/nginx && \
#    rm -rf /etc/nginx/conf.d/default.conf && \
#    rm -rf /var/cache/apk/*
#
#COPY conf.d/app.conf /etc/nginx/conf.d/app.conf
#
#EXPOSE 80 443
#CMD ["nginx", "-g", "daemon off;"]

FROM nginx:1.17-alpine
#RUN rm /etc/nginx/nginx.conf
COPY ./conf.d/app.conf /etc/nginx/conf.d/app.conf

# - Need to run NGINX in the fore‐ground, either by -g "daemon off;" or add daemon off; to your configuration
# - Alter your NGINX configuration to log to /dev/stdout for access logs and /dev/stderr for error logs; \
#    doing so will put your logs into the hands of the Docker daemon, which will make them available \
#    to you more easily based on the log driver you’ve chosen to use with Docker:
# ALL OF THE ABOVE ARE DONE IN THE NGINX BASE IMAGE DOCKERFILE! NO NEED TO DO THEM!