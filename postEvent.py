import json
import boto3
from datetime import datetime

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    tableEvents = dynamodb.Table('events')
    
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    deviceId = event['deviceId']

    try:
        
        tableEvents.put_item(
           Item={
                'eventDateTime': eventDateTime,
                'deviceId': deviceId
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully submitted an event!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error submitting the event')
        }
