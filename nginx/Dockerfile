FROM nginx:1.17-alpine
LABEL MAINTAINER="Tezzy O."

# RUN rm /etc/nginx/nginx.conf
COPY ./conf.d/app.conf /etc/nginx/conf.d/app.conf

# - Need to run NGINX in the fore‐ground, either by -g "daemon off;" or add daemon off; to your configuration
# - Alter your NGINX configuration to log to /dev/stdout for access logs and /dev/stderr for error logs; \
#    doing so will put your logs into the hands of the Docker daemon, which will make them available \
#    to you more easily based on the log driver you’ve chosen to use with Docker:
# ALL OF THE ABOVE ARE DONE IN THE NGINX BASE IMAGE DOCKERFILE! NO NEED TO DO THEM!