docker run \
    -p 27017:27017 \
    --name mongodb \
    -v `pwd`/conf/mongodb.conf:/etc/mongodb.conf -d mongo
