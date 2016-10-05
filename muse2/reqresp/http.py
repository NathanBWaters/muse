import flask
from muse.endpoint import Endpoint

class HTTPEndpoint(Endpoint):
    def __init__(self, conf, handler):
        if not isinstance(server, IInterface): raise Exception('Bad interface')
        if not IInterface.version() == '1.0': raise Exception('Bad revision')

        self._server = server


    def client_show(self):
        self._server.show()
