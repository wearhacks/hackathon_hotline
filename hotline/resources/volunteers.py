import csv
import os

from db.db_client import db_client
from flask import request
from flask.ext import restful 
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'

class Volunteers(restful.Resource):

    def post(self):
        file = request.files['file']
        file_name = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, file_name))
        with open(os.path.join(UPLOAD_FOLDER, file_name)) as f:
            csv_f = csv.reader(f)
            next(csv_f, None)
            for data in csv_f:
                try:
                    db_client.set(self.__class__.__name__.lower(), {'first_name': data[0], 'last_name': data[1], 'phone_number': data[2], 'date' : data[3], 'time_from' : int(data[4]), 'time_to' : int(data[5])})
                except ValueError:
                    pass
