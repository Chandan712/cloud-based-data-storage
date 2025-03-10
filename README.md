# cloud-based-data-storage

# Cloud-Based Data Storage System

## Overview
This project is a cloud-based data storage system leveraging AWS services. It includes user authentication via AWS Cognito, metadata storage in DynamoDB, IAM-based role-based access control (RBAC), and secured APIs via API Gateway.

## Features
- User authentication using AWS Cognito
- Secure file upload/download to S3
- API Gateway integration for request handling
- Lambda functions for processing requests
- DynamoDB for metadata storage
- IAM-based RBAC for user permissions

## AWS Services Used
- **Amazon S3** - Storage for user files
- **Amazon Cognito** - User authentication
- **AWS Lambda** - Backend logic
- **Amazon API Gateway** - Secure API endpoints
- **Amazon DynamoDB** - Metadata storage
- **AWS IAM** - Role-based access control

## Setup Instructions

### 1. Create API Gateway
Go to AWS API Gateway and create a new REST API.

![Creating API Gateway](./screenshots/Screenshot_3.png)

### 2. Define API Resources
Create resources and methods in API Gateway for file upload and download.

![Creating Resources](./screenshots/Screenshot_4.png)

### 3. Create AWS Lambda Function
Set up an AWS Lambda function to handle file uploads and downloads.

![Lambda Function Creation](./screenshots/Screenshot_5.png)

### 4. Configure S3 Bucket
- Create an S3 bucket.
- Set appropriate permissions for public or private access.

### 5. Set Up DynamoDB
- Create a DynamoDB table to store metadata related to file uploads.

### 6. Implement IAM Role-Based Access Control
- Define IAM policies for restricted access based on user roles.

### 7. Deploy and Test
- Deploy API Gateway.
- Test API calls using Postman or cURL.

## API Endpoints
| Method | Endpoint       | Description |
|--------|---------------|-------------|
| POST   | /upload       | Upload a file |
| POST   | /download     | Download a file |

## Lambda Function Code
```python
import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Sample Lambda function to handle API Gateway requests
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
```

## Conclusion
This project provides a secure and scalable cloud-based storage solution using AWS services. You can extend its functionality by adding more features like file versioning, sharing, or real-time notifications.
