# Test simple message that should be logged to disk
echo '{"json" : "message"}' | fluent-cat hmmm.wumm

# Test a message that shoudl be logged to mongodb
echo '{"json" : "message"}' | fluent-cat mongo.testit
