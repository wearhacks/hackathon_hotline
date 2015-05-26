import os
import redis

from urllib.parse import urlparse

redis_url = os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379') 
redis_url_parse = urlparse(redis_url)
redis_client = redis.StrictRedis(host=redis_url_parse.hostname, port=redis_url_parse.port)


