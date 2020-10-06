import boto3
sts = boto3.client('sts')
sts.get_caller_identity()

