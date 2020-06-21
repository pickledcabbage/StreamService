import boto3

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

response = client.put_item(
    TableName='TopicSubscribers',
    Item={
        'topic': { 'S': 'testtopic' },
        'subscriber': { 'S': 'testsubscriber' }
    }
)

response = client.get_item(
    TableName='TopicSubscribers',
    Key={
        'topic': { 'S': 'testtopic' },
        'subscriber': { 'S': 'testsubscriber' }
    })
print(response)