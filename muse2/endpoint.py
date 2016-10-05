from abc import ABCMeta, abstractmethod

class Endpoint(ABCMeta):
    @abstractmethod
    def read(self, data):
        pass
    @abstractmethod
    def write(self, data):
        pass
