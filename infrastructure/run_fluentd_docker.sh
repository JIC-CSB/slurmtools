LOG_PATH=`pwd`/log
FLUENT_CONF_PATH=`pwd`/conf/fluentd

#    --network container:mongo \
docker run --name mongofluent \
    -d \
    -v $LOG_PATH:/log \
    -v $FLUENT_CONF_PATH:/conf \
    -p 24224:24224 \
    -p 8888:8888 \
    mongofluent \
    fluentd -c /conf/fluent.conf
