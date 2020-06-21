import requests
import boto3


def subscribe_call():
    url = "http://localhost:5000/subscribe"
    data = {
        'topic': 'test',
        'subscriber': 'test2',
        'address': 'test2'
    }

    resp = requests.post(url, json=data)
    print(resp.json())

def publish_call():
    url = "http://localhost:5000/publish"
    data = {
        'topic': 'test',
        'data': {'message': 'hello world'}
    }

    resp = requests.post(url, json=data)
    print(resp.json())

def scan_call():
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    response = ddb.scan(
        TableName="TopicSubscribers"
    )
    for i in response['Items']:
        print(i)

def nuke_ddb():
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    response = ddb.delete_table(
        TableName='TopicSubscribers'
    )

def show_tables():
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    response = ddb.list_tables()
    print(response)

publish_call()