from config import SUBSCRIBER_TABLE

def subscribe(client, data):
    try:
        client.put_item(
            TableName=SUBSCRIBER_TABLE,
            Item={
                'topic': { 'S': data['topic'] },
                'subscriber': { 'S': data['subscriber'] },
                'address': { 'S': data['address'] }
            }
        )
        return {'message': 'SUCCESS'}
    except Exception as e:
        print(e)
        return {'message': 'FAILURE'}