from muse.pubsub.kafka_endpoint import KafkaEndpoint

def metrics(resp):
    print "called metrics"
    print "message was " + str(resp)

def logger(resp):
    print "called logging"

def tracing(resp):
    print "called tracing!"

def handler(message):
    print "called handler!"
    print "handler was passed the message " + str(message)
    return message

messageA = KafkaEndpoint(handler, [logger, metrics, tracing])
