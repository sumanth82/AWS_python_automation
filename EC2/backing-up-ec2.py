# We will create a lambda function to backup the attached EBS Volumes
# Second lambda function will prune the snapshots; Keeps only the required numbers 

import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    instances= ec2.instances.filter(
        Filters=[
            {'Name': 'tag:backup', 'Values': ['true'] }
        ]
    )

    timestamp=datetime.utcnow().replace(microsecond=0).isoformat()

    for i in instances.all():
        for v in i.volumes.all():
            desc = 'Backup of {0}, volume {1}, created {2}'.format(i.id, v.id, timestamp)
            print(desc)
            snapshot = v.create_snapshot(Description=desc)
            print("Created snapshot: ", snapshot.id)