from abc import ABCMeta, abstractmethod

class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get(self, **kwargs):
        pass

    @abstractmethod
    def set(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass
