import csv
import os
import json 

from db.db_client import db_client
from flask import request, jsonify
from flask.ext import restful 
from flask.ext.restful import reqparse
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'

class Users(restful.Resource):

    def post(self):
        file = request.files['file']
        file_name = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, file_name))
        with open(os.path.join(UPLOAD_FOLDER, file_name)) as f:
            csv_f = csv.reader(f)
            next(csv_f, None)
            for data in csv_f:
                try:
                    db_client.contacts.insert({'first_name': data[0], 'last_name': data[1], 'phone_number': data[2], 'date' : data[3], 'time_from' : int(data[4]), 'time_to' : int(data[5])})
                except ValueError:
                    pass
