import boto3
from boto3.dynamodb.conditions import Key
import requests
from config import SUBSCRIBER_TABLE, GSI_NAME

def publish(client, topic, data):
    try:
        response = client.query(
            TableName=SUBSCRIBER_TABLE,
            KeyConditionExpression='topic = :topicname',
            ExpressionAttributeValues={
                ':topicname': { 'S': topic }
            }
        )
        for i in response['Items']:
            requests.post(url="http://localhost" + i['address']['S'], json=data)
    except Exception as e:
        return {'message': 'Failed to query database', 'error': e}
    return response