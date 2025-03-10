import json
import boto3
import os

s3 = boto3.client('s3')
BUCKET_NAME = 'cloud-based-data-storage-system'  

def lambda_handler(event, context):
    action = event.get('action', 'upload')  # Default action is upload

    if action == 'upload':
        return upload_file(event)
    elif action == 'download':
        return download_file(event)
    else:
        return {'statusCode': 400, 'body': json.dumps('Invalid action!')}

def upload_file(event):
    try:
        file_name = event['file_name']
        file_content = event['file_content']  # Base64 encoded content
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
        return {'statusCode': 200, 'body': json.dumps(f'File {file_name} uploaded successfully')}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}

def download_file(event):
    try:
        file_name = event['file_name']
        response = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
        file_content = response['Body'].read().decode('utf-8')
        return {'statusCode': 200, 'body': json.dumps({'file_name': file_name, 'content': file_content})}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
