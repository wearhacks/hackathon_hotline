import csv
import os

from flask import request, jsonify
from flask.ext import restful 
from flask.ext.restful import reqparse
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'
DB = {}

class Users(restful.Resource):

    def post(self):
        file = request.files['file']
        file_name = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, file_name))
        with open(os.path.join(UPLOAD_FOLDER, file_name)) as f:
            csv_f = csv.reader(f)
            next(csv_f, None)
                # DB.update({(data[3], int(data[4]), int(data[5])) : {'first_name': data[0], 'last_name': data[1], 'phone_number': data[2]} for data in csv_f})
            for data in csv_f:
                try:
                    DB.update({(data[3], int(data[4]), int(data[5])) : {'first_name': data[0], 'last_name': data[1], 'phone_number': data[2]}})
                except ValueError:
                    pass
