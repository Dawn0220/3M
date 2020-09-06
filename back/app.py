from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource
from flask import (abort, current_app, jsonify,
                   make_response, request, send_file)

import csv
DATA_FILE = "./data.csv"

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."


# class Hello(Resource):
#     @staticmethod
#     def get():
#         return "[get] hello flask"

#     @staticmethod
#     def post():
#         return "[post] hello flask"

# api.add_resource(Hello, '/hello')

@app.route('/hello_api', methods = ['GET', 'POST'])
def hellp_api():
    data = request.get_json(silent=True)
    data_in = data['input']
    return_data = {
        'hello': "hello flask, hello vue " + data_in,
        "flask": 2
    }
    return make_response(jsonify(return_data))

@app.route('/get_released_task', methods = ['GET', 'POST'])
def get_released_task():
    data = request.get_json(silent=True)
    user_id = data['user_id']
    return_data = get_released_task_data(user_id)
    return make_response(jsonify(return_data))

def get_released_task_data(user_id):
    return_data = {
        "data": []
    }
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        head_row=next(reader)
        for row in reader:
            if row[5] == user_id:
                activity = {
                    'title': row[1],
                    'position': row[3],
                    'status': row[7],
                    'participant': row[6],
                    'key_word': row[8]
                }
                return_data['data'].append(activity)
    return return_data

@app.route('/get_participated_task', methods = ['GET', 'POST'])
def get_participated_task():
    data = request.get_json(silent=True)
    user_id = data['user_id']
    return_data = get_participated_task_data(user_id)
    return make_response(jsonify(return_data))

def get_participated_task_data(user_id):
    return_data = {
        "data": []
    }
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        head_row=next(reader)
        for row in reader:
            if row[5] != user_id:
                activity = {
                    'title': row[1],
                    'position': row[3],
                    'status': row[7],
                    'participant': row[6],
                    'key_word': row[8]
                }
                return_data['data'].append(activity)
    return return_data

@app.route('/get_task_on_map', methods = ['GET', "POST"])
def get_task_on_map():
    data = request.get_json(silent=True)
    user_id = data['user_id']
    return_data = get_map_data(user_id)
    return make_response(jsonify(return_data))

def get_map_data(user_id):
    return_data = {
        'freeData': [],
        'discountsData': []
    }
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        head_row=next(reader)
        for row in reader:
            activity = {
                'name': row[1],
                'value': [
                    float(row[4].split(',')[0][1:]), # 经度
                    float(row[4].split(',')[1][:-1]), # 纬度
                    row[3], # position
                    row[2], # distription
                    row[9], # requirement
                    row[8], # key word
                    row[11], # pic
                    row[12], # store distription
                    row[10], # task
                ]
            }
            if row[5] == user_id:
                return_data['discountsData'].append(activity)
            else:
                return_data['freeData'].append(activity) 
    return return_data

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
