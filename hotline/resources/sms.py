from flask import request, Response
from flask.ext import restful
from twilio import twiml

class SMS(restful.Resource):

    def post(self):
        response = twiml.Response()
        user_input = request.form['Body']
        user_from = request.form['From']
        print(request.form)
        msg = "success!!!"
        response.sms(msg)
        return Response(str(response), content_type='text/xml')
