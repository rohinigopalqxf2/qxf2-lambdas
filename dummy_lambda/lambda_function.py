"""
Simplest lambda to play with GitHub actions
"""
import json
import boto3
import cv2

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
