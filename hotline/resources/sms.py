import os

from flask import request, Response
from flask.ext import restful
from twilio import twiml

from resources.users import DB
from common.time_zone import current_time_zone_info

from twilio.rest import TwilioRestClient

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

class SMS(restful.Resource):

    def post(self):
        response = twiml.Response()
        body_msg = request.form['Body']
        if _forward_sms(body_msg):
            reply_msg = "Your message has been received. Someone will be with you shortly!!!"
            response.sms(reply_msg)
            return Response(str(response), content_type='text/xml')

def _forward_sms(body_msg):
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    current_date, current_time = current_time_zone_info()
    current_time = int(current_time)
    for time, volunteer in DB.items():
        if time[0] == current_date:
            if time[1] > time[2] and (current_time < time[1] and current_time < time[2]):
                return client.messages.create(to=volunteer['phone_number'], from_=TWILIO_NUMBER, body=body_msg)
            elif time[1] < time[2] and (time[1] < current_time < time[2]):
                return client.messages.create(to=volunteer['phone_number'], from_=TWILIO_NUMBER, body=body_msg)
    return None
