import importlib
import os

class DBClient:

    db_defaults = {'mongo': 'mongodb://localhost:27017/',
                   'redis': 'redis://localhost:6379',
                   'postgresql': 'postgresql://localhost:5432'
                  }

    def __init__(self, url=None, db_type=None, db_name=None):
       self.db_type = db_type
       self.url = url or DBClient.db_defaults[db_type]
       db_module = importlib.import_module('db.db_{0}'.format(db_type))
       self.client = getattr(db_module, '{0}Client'.format(db_type.capitalize()))(self.url)

    def connect(self):
        pass

# Update later to remove default db_type 'mongo'
db_client = DBClient(db_type='mongo')
db_client.connect()
