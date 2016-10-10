from muse.endpoint import Endpoint
from kafka import KafkaConsumer

class KafkaService(object):
    def __init__(self, host='localhost', port='9092', group_id="group2"):
        self.host = host
        self.port = port
        self.group_id = group_id

    def addEndpoint(self, topic, endpoint):
        print "called addEndpoint"
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=self.host + ":" + self.port,
                                 group_id=self.group_id)
        for msg in consumer:
            print "called msg"
            endpoint.call(msg)

    def start(self):
        print "called start on KafkaService"
