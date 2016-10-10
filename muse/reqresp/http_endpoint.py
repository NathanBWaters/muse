import flask
from muse.endpoint import Endpoint

class HTTPEndpoint(object):
    def __init__(self, handler, instrumentation):
        self.handler = handler
        self.instrumentation = instrumentation

    def call(self):
        resp = self.handler()
        for func in self.instrumentation:
            func(resp)

        return resp
