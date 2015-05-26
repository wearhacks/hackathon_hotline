import os
import pickle

from flask import request, Response
from flask.ext import restful
from twilio import twiml
from twilio.rest import TwilioRestClient

from common.time_zone import current_time_zone_info
from db.db_mongo import mongo_db
#from db.db_redis import redis_client
# from resources.users import DB

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

class SMS(restful.Resource):

    def post(self):
        response = twiml.Response()
        body_msg = 'hello' # request.form['Body']
        if _forward_sms(body_msg):
            reply_msg = "Your message has been received. Someone will be with you shortly!!!"
        else:
            reply_msg = "No one on duty currently!!!"
        response.sms(reply_msg)
        return Response(str(response), content_type='text/xml')

def _forward_sms(body_msg):
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    current_date, current_time = current_time_zone_info()
    current_time = int(current_time)
    volunteer_count = 0
    for document in mongo_db.contacts.find():
        time_from, time_to = document['time_from'], document['time_to']
        if document['date'] == current_date:
            if time_from > time_to and (current_time < time_from and current_time < time_to):
                client.messages.create(to=document['phone_number'], from_=TWILIO_NUMBER, body=body_msg)
                volunteer_count += 1
            elif time_from < time_to and (time_from < current_time < time_to):
                client.messages.create(to=document['phone_number'], from_=TWILIO_NUMBER, body=body_msg)
                volunteer_count += 1
    return volunteer_count
