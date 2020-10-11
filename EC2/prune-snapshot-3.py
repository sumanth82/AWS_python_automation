# This function should delete any snapshots created and NOT in use by any EC2

import boto3
import json

ec2_client=boto3.client('ec2')

response = ec2_client.describe_snapshots(Filters=[{'Name': 'owner-id', 'Values': ['574832147455']}])

keys_of_snapshots = response['Snapshots']
print(keys_of_snapshots)
print(type(keys_of_snapshots))

for i in keys_of_snapshots:
    snapshot_to_delete = i['SnapshotId']
    print(snapshot_to_delete)
    response = ec2_client.delete_snapshot(
    SnapshotId=snapshot_to_delete,
    DryRun=False)
    

#### WORKS GREAT - This Will delete the snapshots NOT in use by any AMI #####


# O/P: <class 'list'>
#snap-08445240781469bb1
#snap-0aed77ebc0e0a984d
#Traceback (most recent call last):
#  File "prune-snapshot-3.py", line 19, in <module>
#    DryRun=False)
#  File "/Users/sumantrenukarya/Library/Python/3.7/lib/python/site-packages/botocore/client.py", line 357, in _api_call
#    return self._make_api_call(operation_name, kwargs)
#  File "/Users/sumantrenukarya/Library/Python/3.7/lib/python/site-packages/botocore/client.py", line 676, in _make_api_call
#    raise error_class(parsed_response, operation_name)
#botocore.exceptions.ClientError: An error occurred (InvalidSnapshot.InUse) when calling the DeleteSnapshot operation: The snapshot snap-0aed77ebc0e0a984d is currently in use by ami-07feebb72b73e7831
