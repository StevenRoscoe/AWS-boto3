#Event Pattern:
{
  "source": [
      "aws.ec2"
  ],
  "detail-type": [
      "AWS API Call via CloudTrail"
  ],
  "detail": {
      "eventSource": [
          "ec2.amazonaws.com"
      ],
      "eventName": [
          "CreateVpc"
      ]
  }
}

#Lambda Execution Role:
{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateFlowLogs",
        "ec2:DescribeFlowLogs",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}

#Lambda Function
import os

import boto3
from botocore.exceptions import ClientError

ROLE_ARN = os.environ['ROLE_ARN']

ec2 = boto3.client('ec2')
logs = boto3.client('logs')


def lambda_handler(event, context):

    try:
        # Extract the VPC ID from the event
        vpc_id = event['detail']['responseElements']['vpc']['vpcId']

        flow_logs_group = 'VPCFlowLogs-' + vpc_id

        print('VPC: ' + vpc_id)

        try:
            response = logs.create_log_group(
                logGroupName=flow_logs_group)
        except ClientError:
            print(f"Log group '{flow_logs_group}' already exists.")

        # Get Flow Logs status
        response = ec2.describe_flow_logs(
            Filter=[
                {
                    'Name': 'resource-id',
                    'Values': [
                        vpc_id,
                    ]
                },
            ],
        )

        if len(response['FlowLogs']) > 0:
            print('VPC Flow Logs are ENABLED')
        else:
            print('VPC Flow Logs are DISABLED. Enabling...')

            response = ec2.create_flow_logs(
                ResourceIds=[vpc_id],
                ResourceType='VPC',
                TrafficType='ALL',
                LogGroupName=flow_logs_group,
                DeliverLogsPermissionArn=ROLE_ARN,
            )

            print('Created Flow Logs:' + response['FlowLogIds'][0])

    except Exception as e:
        print('Error - reason "%s"' % str(e))
        
  
#Test Event:
{
  "version": "0",
  "id": "e3f9c65c-6b72-3ce4-b1f3-20494cbc87e0",
  "detail-type": "AWS API Call via CloudTrail",
  "source": "aws.ec2",
  "account": "111111111111",
  "time": "2019-02-25T15:33:07Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "eventVersion": "1.05",
    "userIdentity": {
      "type": "Root",
      "principalId": "111111111111",
      "arn": "arn:aws:iam::111111111111:root",
      "accountId": "111111111111",
      "accessKeyId": "...",
      "sessionContext": {
        "attributes": {
          "mfaAuthenticated": "false",
          "creationDate": "2019-02-25T14:13:11Z"
        }
      },
      "invokedBy": "signin.amazonaws.com"
    },
    "eventTime": "2019-02-25T15:33:07Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "CreateVpc",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "73.125.25.100",
    "userAgent": "signin.amazonaws.com",
    "requestParameters": {
      "cidrBlock": "10.0.0.0/16",
      "instanceTenancy": "default"
    },
    "responseElements": {
      "requestId": "ee1f6203-3e40-4669-a50b-17c52abc69b7",
      "vpc": {
        "vpcId": "vpc-0a71e831cb5152c43",
        "state": "pending",
        "cidrBlock": "10.0.0.0/16",
        "cidrBlockAssociationSet": {
          "items": [
            {
              "cidrBlock": "10.0.0.0/16",
              "associationId": "vpc-cidr-assoc-07ba205e048b7798a",
              "cidrBlockState": {
                "state": "associated"
              }
            }
          ]
        },
        "ipv6CidrBlockAssociationSet": {},
        "dhcpOptionsId": "dopt-c0bf6fbb",
        "instanceTenancy": "default",
        "tagSet": {},
        "isDefault": false
      }
    },
    "requestID": "ee1f6203-3e40-4669-a50b-17c52abc69b7",
    "eventID": "9be08716-256d-4286-9378-8137d661109b",
    "eventType": "AwsApiCall"
  }
}


#Trust Policy:
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": [
        "vpc-flow-logs.amazonaws.com"
      ]
    },
    "Action": "sts:AssumeRole"
  }]
}

#Flow Logs IAM Role:
{
  "Version": "2012-10-17",
  "Statement": [{
    "Action": [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
      "logs:DescribeLogGroups",
      "logs:DescribeLogStreams"
    ],
    "Resource": "*",
    "Effect": "Allow"
  }]
}