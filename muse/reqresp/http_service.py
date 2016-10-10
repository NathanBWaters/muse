from flask import Flask
from muse.endpoint import Endpoint
app = Flask(__name__)

class HTTPService(object):
    def __init__(self, port=8080):
        self.port = port

    def addEndpoint(self, HTTPVerb, url, endpoint):
        app.add_url_rule(url, view_func=endpoint.call)

    def start(self):
        app.run(port=self.port)
