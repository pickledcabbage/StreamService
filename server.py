from flask import Flask, request
import boto3
import json
from http import HTTPStatus
from subscribe_logic import subscribe
from publish_logic import publish

app = Flask(__name__)
client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

def format_response(data):
    return json.dumps(data)

def check_request(req, params):
    temp = set()
    for i in req:
        temp.add(i)
    for i in params:
        if i not in temp:
            return False
        else:
            temp.remove(i)
    return temp == set()

def wrong_params():
    return format_response({'message': 'Wrong parameters'}), HTTPStatus.BAD_REQUEST

def good_response(data):
    return format_response(data), HTTPStatus.OK

def bad_response(data={'message': 'Unexpected failure'}):
    return format_response(data), HTTPStatus.BAD_REQUEST

@app.route('/create', methods=['POST'])
def api_create_topic():
    return "Hello world!"

@app.route('/subscribe', methods=['POST'])
def api_subscribe():
    try:
        data = request.json
        params = [
            'topic',
            'subscriber',
            'address'
        ]
        if not check_request(data, params):
            return wrong_params()
        return good_response(subscribe(client, data))
    except Exception as e:
        print(e)
        return bad_response()
    

@app.route('/publish', methods=['POST'])
def api_publish():
    try:
        data = request.json
        params = [
            'topic',
            'data'
        ]
        if not check_request(data, params):
            return wrong_params()
        return good_response(publish(client, data['topic'], data['data']))
    except Exception as e:
        print(e)
        return bad_response()



if __name__ == '__main__':
    app.run()