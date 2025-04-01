import json
import boto3
from datetime import datetime
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    tableEvents = dynamodb.Table('events')
    
    eventDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            'body': json.dumps('Successfully submitted an event!')
        }
    except ClientError as e:
        print(f'Error: {str(e)}')
        return {
                'statusCode': 400,
                'body': json.dumps(f'Error submitting the event: {str(e)}')
        }