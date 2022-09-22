import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    tableEvents = dynamodb.Table('events')
    # TODO re-implement to avoid full table scan (select by deviceId or other key)
    response = tableEvents.scan()
    return {    
        'statusCode': 200,
        'body': response['Items']
    }
