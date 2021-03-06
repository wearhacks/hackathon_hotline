import os

from flask import Flask
from flask.ext import restful
from resources.hello_world import HelloWorld
from resources.sms import SMS
from resources.volunteers import Volunteers

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Admin, '/admin')
api.add_resource(HelloWorld, '/')
api.add_resource(SMS, '/sms')
api.add_resource(Volunteers, '/volunteers')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # Local Environment
    if os.environ.get('DEBUG'):
        app.run(debug=True, port=port)
    # Production Environment
    else:
        app.run(host='0.0.0.0', port=port)
