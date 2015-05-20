from flask import request
from flask.ext import restful
from twilio import twiml

class SMS(restful.Resource):

    def post(self):
        response = twiml.Response()
        user_input = request.form['Body']
        user_from = request.form['From']
        print(request.form)
        msg = "success!!!"
        response.message(msg)
        return str(response)
