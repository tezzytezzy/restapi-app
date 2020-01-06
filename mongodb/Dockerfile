FROM mongo:4.0-xenial

# 2020-01-02T15:04:29.846+0000 E -        [main] Error saving history file: FileOpenFailed: Unable to open() file /home/mongodb/.dbshell: Unknown error

#ENV GROUP_ID=999 \
#    USER_ID=999

#RUN addgroup -g $GROUP_ID mongodb
#RUN adduser -D -u $USER_ID -G mongodb mongodb -s /bin/sh


#RUN groupadd -r mongodb \
#  && useradd -r -s /bin/false -g mongodb mongodb

#groupadd: group 'mongodb' already exists
#useradd: user 'mongodb' already exists
#RUN useradd -r -s /bin/false -g mongodb mongodb

WORKDIR /home/mongodb/  

CMD "/usr/bin/mongo", "$MONGODB_URI_PREFIX$MONGODB_DB$MONGODB_URI_SUFFIX", "--username", $MONGODB_USER, "--password", $MONGODB_PWD
