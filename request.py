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

def get_quote_call():
    url = "http://localhost:5001/quote/AAPL"

    resp = requests.get(url)
    print(resp.json())

def get_quotes_call():
    url = "http://localhost:5001/quotes/"
    params = {
        'symbols': ','.join(['AAPL', 'MSFT'])
    }
    resp = requests.get(url, params=params)
    print(resp.json())

def scan_call(tb="TopicSubscribers"):
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    response = ddb.scan(
        TableName=tb
    )
    #for i in response['Items']:
    #    print(i)
    return response['Items']

def print_stock(stock):
    temp = "{:s} {:8.2f}".format(stock['symbol']['S'], float(stock['last_trade_price']['N']))
    print(temp)

def scan_call_print(tb="TopicSubscribers"):
    quotes = scan_call(tb)
    for i in quotes:
        print_stock(i)

def nuke_ddb(tb='TopicSubscribers'):
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    response = ddb.delete_table(
        TableName=tb
    )

def show_tables():
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    response = ddb.list_tables()
    print(response)

scan_call_print('instruments')