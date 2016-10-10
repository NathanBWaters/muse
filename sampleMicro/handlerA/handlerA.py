from muse.reqresp.http_endpoint import HTTPEndpoint

def metrics(resp):
    print "called metrics"

def logger(resp):
    print "called logging"

def tracing(resp):
    print "called tracing!"

def handler():
    print "called handler!"
    return "returning from handler in handlerA!!"

endpointA = HTTPEndpoint(handler, [logger, metrics, tracing])
