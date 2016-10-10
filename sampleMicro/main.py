from multiprocessing import Process

from muse.reqresp.http_service import HTTPService
from muse.pubsub.kafka_service import KafkaService
from handlerA.handlerA import endpointA
from messageA.messageA import messageA


def startMessageServer():
    print "-- startMessageServer"
    svc = KafkaService()
    svc.addEndpoint("foobar2", messageA)
    svc.start()

def startHTTPServer():
    print "-- startHTTPServer"
    svc = HTTPService()
    svc.addEndpoint("GET", "/endpointA", endpointA)
    svc.start()

if __name__ == "__main__":
    print "Starting up"
    p = Process(target=startHTTPServer)
    n = Process(target=startMessageServer)
    p.start()
    n.start()
