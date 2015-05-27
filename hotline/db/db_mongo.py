from db.db_abstract import AbstractClient
from pymongo import MongoClient

class MongoClient(AbstractClient):

    def __init__(self, url):
        self.url = url
        self.client = None

    def connect(self):
        self.client = MongoClient(mongo_url)

    def get(self, **kwargs):
        pass

    def set(self, **kwargs):
        pass

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
