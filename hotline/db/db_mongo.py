import os

from pymongo import MongoClient
from urllib.parse import urlparse

mongo_url = os.environ.get('MONGODB_URL', 'mongodb://localhost:27017/') 
# mongo_url_parse = urlparse(mongo_url)
mongo_client = MongoClient(mongo_url)
mongo_db = mongo_client['hotline']


