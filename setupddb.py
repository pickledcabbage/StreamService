import boto3
from config import SUBSCRIBER_TABLE, GSI_NAME

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')


client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'subscriber',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'topic',
            'AttributeType': 'S'
        }
    ],
    TableName=SUBSCRIBER_TABLE,
    KeySchema=[
        {
            'AttributeName': 'topic',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'subscriber',
            'KeyType': 'RANGE'
        }
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': GSI_NAME,
            'KeySchema': [
                {
                    'AttributeName': 'subscriber',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'topic',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
    }
)