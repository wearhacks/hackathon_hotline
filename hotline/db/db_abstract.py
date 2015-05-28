from abc import ABCMeta, abstractmethod

class AbstractClient(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get(self, table_name, key):
        pass

    @abstractmethod
    def set(self, table_name, data):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass
