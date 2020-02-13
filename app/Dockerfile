FROM python:3.6.8-alpine3.9
# ARG must be BELOW FROM!
ARG MAINTAINER_NAME
ARG FLASK_REMOTE_ROOT_DIR
ARG FLASK_LOG_DIR
ARG FLASK_USER
ARG FLASK_ID
ARG FLASK_DEFAULT_IP_ADDRESS
ARG FLASK_PORT
ARG FLASK_DEFAULT_IP_ADDRESS_AND_PORT
LABEL MAINTAINER=${MAINTAINER_NAME}

WORKDIR ${FLASK_REMOTE_ROOT_DIR}

COPY . ${FLASK_REMOTE_ROOT_DIR}
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn \
    && addgroup -g ${FLASK_ID} ${FLASK_USER} \
    && adduser -D -u ${FLASK_ID} -G ${FLASK_USER} ${FLASK_USER} -s /bin/sh \
    && ln -sf /dev/stderr ${FLASK_LOG_DIR} # ${FLASK_LOG_DIR} must exist prior to execution unlike WORKDIR


USER ${FLASK_USER}
# ENV IP_ADDRESS_AND_PORT=${FLASK_DEFAULT_IP_ADDRESS_AND_PORT}
#EXPOSE ${FLASK_PORT}

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "wsgi"]
### TRIED ###
# CMD [ "gunicorn", "-w", "4", "--bind", "${IP_ADDRESS_AND_PORT}", "wsgi"]
# CMD gunicorn -w 4 --bind ${FLASK_DEFAULT_IP_ADDRESS_AND_PORT} wsgi
# CMD gunicorn -w 4 --bind "${FLASK_DEFAULT_IP_ADDRESS}:${FLASK_PORT}" wsgi
# CMD gunicorn -w 4 --bind ${FLASK_DEFAULT_IP_ADDRESS}:${FLASK_PORT} wsgi
# CMD gunicorn -w 4 --bind ${FLASK_DEFAULT_IP_ADDRESS} wsgi
# CMD gunicorn -w 4 --bind '${FLASK_DEFAULT_IP_ADDRESS}:${FLASK_PORT}' wsgi
# CMD [ "gunicorn", "-w", "4", "--bind", '${FLASK_DEFAULT_IP_ADDRESS}:${FLASK_PORT}', "wsgi"]
