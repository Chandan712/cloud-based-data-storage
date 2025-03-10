# Cloud-Based Storage System

## Project Overview
This project is a cloud-based storage system using AWS services, including S3, API Gateway, Lambda, Cognito, and DynamoDB. It provides secure file storage, upload, and retrieval functionalities with IAM-based access control.

## AWS Services Used
- **S3**: File storage
- **API Gateway**: Handles API requests
- **Lambda**: Processes file uploads and retrievals
- **Cognito**: User authentication
- **DynamoDB**: Metadata storage

## Setup Instructions

### 1. Create API Gateway
- Navigate to **AWS Console > API Gateway**
- Click **Create API** and configure as required
- **Screenshot:**  
  ![API Gateway Creation]![Screenshot (3)](https://github.com/user-attachments/assets/d7c9ba67-c162-4464-aee2-9cb964a295ca)


### 2. Create API Resources
- Add `/upload` and `/download` resources
- **Screenshot:**  
  ![API Resources]![Screenshot (4)](https://github.com/user-attachments/assets/120a6011-ae6c-41ff-bce4-7ae5ce9124bc)


### 3. Create a Lambda Function
- Navigate to **AWS Lambda**
- Create a function and add triggers
- **Screenshot:**  
  ![Lambda Function]![Screenshot (5)](https://github.com/user-attachments/assets/ce455543-9495-4530-927f-5ad9ddd6d180)


### 4. Deploying API Gateway
- After configuring API Gateway, click **Deploy API**

## AWS CLI Commands
To deploy the Lambda function, run the following commands:
```sh
aws lambda create-function \
    --function-name S3_file_handler \
    --runtime python3.8 \
    --role arn:aws:iam::<AWS_ACCOUNT_ID>:role/execution_role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda_function.zip
```

To update the Lambda function:
```sh
aws lambda update-function-code \
    --function-name S3_file_handler \
    --zip-file fileb://lambda_function.zip
```

## Lambda Function Code
```python
import json
import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    
    if event['httpMethod'] == 'POST':
        file_content = base64.b64decode(event['body'])
        file_key = event['queryStringParameters']['filename']
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully'})
        }
    
    elif event['httpMethod'] == 'GET':
        file_key = event['queryStringParameters']['filename']
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_data = base64.b64encode(file_obj['Body'].read()).decode('utf-8')
        return {
            'statusCode': 200,
            'body': json.dumps({'file_data': file_data})
        }
    
    return {'statusCode': 400, 'body': json.dumps({'message': 'Invalid request'})}
```

## API Endpoints
- **Upload File**: `POST /upload?filename=<file_name>`
- **Download File**: `GET /download?filename=<file_name>`

## Console Output
```
$ curl -X POST "https://waxiaskfil.execute-api.us-east-1.amazonaws.com/First-stage/Upload" \
  -H "Content-Type: application/json" \
  -d '{"file_name": "test.txt", "file_content": "Hello AWS"}'

{"statusCode": 200, "body": "File test.txt uploaded successfully"}
```
**Screenshot:**  
  ![Console Output]![Screenshot (6)](https://github.com/user-attachments/assets/c19fdced-bca1-45d4-ad06-7aca65f3027a)


This completes the setup. Now you can use the API Gateway URL to upload and retrieve files securely.
