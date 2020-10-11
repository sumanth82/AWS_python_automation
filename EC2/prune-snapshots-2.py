# This function should delete any snapshots created and NOT in use by any EC2

import boto3
import json

ec2_client=boto3.client('ec2')

#response = ec2_client.describe_snapshots(Filters=[{'Name': 'status', 'Values': ['completed']}])

response = ec2_client.describe_snapshots(Filters=[{'Name': 'owner-id', 'Values': ['574832147455']}])
#print(response)

#print(type(response))   # O/P: <class 'dict'>
#print(len(response))    # O/P: 2

# Owner : 574832147455

keys_of_snapshots = response['Snapshots']

# O/P: [{'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:55:56', 'Encrypted': False, 'OwnerId': '574832147455', 'Progress': '100%', 'Sna
#pshotId': 'snap-0853bb37b1de49445', 'StartTime': datetime.datetime(2020, 10, 8, 10, 55, 57, 563000, tzinfo=tzutc()), 'State': 'completed', #'VolumeId': 'vol-0491298cf15fe0053', 'Vol
#umeSize': 8}, {'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:53:56', 'Encrypted': False, 'OwnerId': '574832147455', 'Progress':
# '100%', 'SnapshotId': 'snap-08445240781469bb1', 'StartTime': datetime.datetime(2020, 10, 8, 10, 53, 57, 152000, tzinfo=tzutc()), 'State': 'completed', 'VolumeId': 'vol-0491298cf15
#fe0053', 'VolumeSize': 8}, {'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:57:56', 'Encrypted': False, 'OwnerId': '574832147455'
#, 'Progress': '100%', 'SnapshotId': 'snap-0aed77ebc0e0a984d', 'StartTime': datetime.datetime(2020, 10, 8, 10, 57, 57, 542000, tzinfo=tzutc()), 'State': 'completed', 'VolumeId': 'vo
#l-0491298cf15fe0053', 'VolumeSize': 8}, {'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:51:56', 'Encrypted': False, 'OwnerId': '
#574832147455', 'Progress': '100%', 'SnapshotId': 'snap-096e42859ff839b82', 'StartTime': datetime.datetime(2020, 10, 8, 10, 51, 57, 47000, tzinfo=tzutc()), 'State': 'completed', 'Vo
#lumeId': 'vol-0491298cf15fe0053', 'VolumeSize': 8}, {'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:51:00', 'Encrypted': False, 
#'OwnerId': '574832147455', 'Progress': '100%', 'SnapshotId': 'snap-0c613e9df99db5c86', 'StartTime': datetime.datetime(2020, 10, 8, 10, 51, 0, 669000, tzinfo=tzutc()), 'State': 'com
#pleted', 'VolumeId': 'vol-0491298cf15fe0053', 'VolumeSize': 8}, {'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:49:58', 'Encrypt
#ed': False, 'OwnerId': '574832147455', 'Progress': '100%', 'SnapshotId': 'snap-02bc24d26d58d5416', 'StartTime': datetime.datetime(2020, 10, 8, 10, 49, 59, 73000, tzinfo=tzutc()), '
#State': 'completed', 'VolumeId': 'vol-0491298cf15fe0053', 'VolumeSize': 8}]

print(keys_of_snapshots)

print(type(keys_of_snapshots))  # <class 'list'>
print(len(keys_of_snapshots))   # 6

print(keys_of_snapshots[0])

# O/P: {'Description': 'Backup of i-09314304feb2573fc, volume vol-0491298cf15fe0053, created 2020-10-08T10:55:56', 'Encrypted': False, 'OwnerId': '574832147455', 'Progress': '100%', 'SnapshotId': 'snap-0853bb37b1de49445', 'StartTime': datetime.datetime(2020, 10, 8, 10, 55, 57, 563000, tzinfo=tzutc()), 'State': 'completed', 'VolumeId': 'vol-0491298cf15fe0053', 'VolumeSize': 8}


print(type(keys_of_snapshots[0])) # dict

print(keys_of_snapshots[0]['SnapshotId']) # O/P: snap-0853bb37b1de49445

snapshot1=keys_of_snapshots[0]['SnapshotId']
print(snapshot1)

####### DELETE THE SNAPSHOT ######

#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_snapshot

response = ec2_client.delete_snapshot(
    SnapshotId=snapshot1,
    DryRun=False
)

#### DELETED This SNAPSHOT - BRAVO !!!!! ######


#ec2_snapshot = boto3.resource('ec2')
#snapshot = keys_of_snapshots[0]['SnapshotId']
#response = snapshot.delete()
#print(response)
#snapshot = ec2_snapshot.Snapshot('id')
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.delete



#json_value = json.dump(response)
#print(json_value)


#print(response.keys())  # O/P: dict_keys(['Snapshots', 'ResponseMetadata'])

#print(response['Snapshots'])

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