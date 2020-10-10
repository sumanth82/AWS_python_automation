# This function should delete any snapshots created and NOT in use by any EC2

import boto3

ec2_client=boto3.client('ec2')

#response = ec2_client.describe_snapshots()
#response = ec2_client.describe_snapshots(Filters=[{'Name': 'snapshot-id'}, {'Values': ''} ])
response = ec2_client.describe_snapshots(Filters=[{'Name': 'status', 'Values': ['completed']}])
print(response)
print(type(response))   # O/P: <class 'dict'>

print(response.)

### WORKS GREAT  #####
# Ref: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-snapshots.html

#JSON Syntax:

#[
#  {
#    "Name": "string",
#    "Values": ["string", ...]
#  }
#  ...
#]



