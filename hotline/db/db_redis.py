from db.db_abstract import AbstractClient
from redis import StrictRedis
from urllib.parse import urlparse

class RedisClient(AbstractClient):

    def __init__(self, url):
        self.url = url
        self.client = None

    def connect(self):
        redis_url = urlparse(self.url)
        self.client = StrictRedis(host=url.hostname, port=url.port, password=url.password)

    def get(self, **kwargs):
        pass

    def set(self, **kwargs):
        pass

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
