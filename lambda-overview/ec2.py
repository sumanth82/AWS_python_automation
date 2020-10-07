# This program creates an ec2 instance;
# Note: There is: 

# a. client
# b. resource

import boto3

ec2=boto3.client('ec2')

response=ec2.run_instances(
    ImageId='ami-032930428bf1abbff',
    InstanceType='t2.micro',
    KeyName='timon',
    MinCount=1,
    MaxCount=1
)

print(response)

# O/P: {'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-032930428bf1abbff', 'InstanceId': 'i-0e4871b6ee8b2344a', 'InstanceType': 't2.micro', 'KeyName': 'timon', 'LaunchTime': datetime.datetime(2020, 10, 6, 10, 44, 21, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-16-247.ec2.internal', 'PrivateIpAddress': '172.31.16.247', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 0, 'Name': 'pending'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-d6205a9b', 'VpcId': 'vpc-e72fe89a', 'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': 'c048801f-eb92-4cdc-8847-64570a57203a', 'EbsOptimized': False, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2020, 10, 6, 10, 44, 21, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-04f1143b8863ae1a5', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attaching'}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-c6d795f8'}], 'Ipv6Addresses': [], 'MacAddress': '0a:9e:7a:4b:d0:b5', 'NetworkInterfaceId': 'eni-084e91e0f69961e0c', 'OwnerId': '574832147455', 'PrivateDnsName': 'ip-172-31-16-247.ec2.internal', 'PrivateIpAddress': '172.31.16.247', 'PrivateIpAddresses': [{'Primary': True, 'PrivateDnsName': 'ip-172-31-16-247.ec2.internal', 'PrivateIpAddress': '172.31.16.247'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-d6205a9b', 'VpcId': 'vpc-e72fe89a', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-c6d795f8'}], 'SourceDestCheck': True, 'StateReason': {'Code': 'pending', 'Message': 'pending'}, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled'}}], 'OwnerId': '574832147455', 'ReservationId': 'r-03a7d8bfd5d22a3aa', 'ResponseMetadata': {'RequestId': 'f81a8ce2-0f15-4686-8066-1df9abce2264', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'f81a8ce2-0f15-4686-8066-1df9abce2264', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '4736', 'vary': 'accept-encoding', 'date': 'Tue, 06 Oct 2020 10:44:21 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

