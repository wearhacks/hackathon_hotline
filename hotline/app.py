from flask import Flask
from flask.ext import restful
from resources.sms import SMS
from resources.hello_world import HelloWorld

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(SMS, '/sms')

if __name__ == '__main__':
    app.run()
