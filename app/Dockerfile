FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Tezzy O."

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

COPY . /var/www/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn \
    && addgroup -g $GROUP_ID www \
    && adduser -D -u $USER_ID -G www www -s /bin/sh \
    && ln -sf /dev/stderr ${FLASK_LOG_DIR} # ${FLASK_LOG_DIR} must exist prior to execution unlike WORKDIR


USER www

#EXPOSE 8000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "wsgi"]
