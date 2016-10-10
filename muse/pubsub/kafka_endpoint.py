from kafka import KafkaConsumer

class KafkaEndpoint(object):
    def __init__(self, handler, instrumentation):
        self.handler = handler
        self.instrumentation = instrumentation

    def call(self, message):
        resp = self.handler(message)
        for func in self.instrumentation:
            func(resp)

        return resp
