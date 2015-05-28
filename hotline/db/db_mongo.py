from db.db_abstract import AbstractClient
from pymongo import MongoClient as _MongoClient

class MongoClient(AbstractClient):

    def __init__(self, url, db_name):
        self.url = url
        self.db_name = db_name
        self.client = None

    def connect(self):
        self.client = _MongoClient(self.url)
        self.db = self.client[self.db_name]

    def get(self, key):
        pass

    def set(self, table_name, args):
        self.db[table_name].insert_one(args)

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
