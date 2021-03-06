# This function should terminate an EC2 instance that is running

import boto3
client = boto3.client('ec2')

#print(dir(ec2))

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances

########### STEP 1  - List all the EC2 instances or describe ##########

response = client.describe_instances()
print(response)
print(type(response))   # O/P: dict 

print(list(response.keys())) # O/P: ['Reservations', 'ResponseMetadata']

# O/P: # O/P: {'Reservations': [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-032930428bf1abbff', 'InstanceId': 'i-02417ddb4e49c97a4', 'InstanceType': 't2.micro', 'KeyName': 'timon', 'LaunchTime': datetime.datetime(2020, 10, 9, 10, 0, 11, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': '', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 48, 'Name': 'terminated'}, 'StateTransitionReason': 'User initiated (2020-10-09 10:20:04 GMT)', 'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': 'c2218ef1-1048-4d4d-a015-b770a772bf25', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [], 'StateReason': {'Code': 'Client.UserInitiatedShutdown', 'Message': 'Client.UserInitiatedShutdown: User initiated shutdown'}, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled'}}], 'OwnerId': '574832147455', 'ReservationId': 'r-0f13ff404057d1fe6'}, {'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-032930428bf1abbff', 'InstanceId': 'i-01ad7860d7d8ae746', 'InstanceType': 't2.micro', 'KeyName': 'timon', 'LaunchTime': datetime.datetime(2020, 10, 9, 10, 27, 55, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-31-106.ec2.internal', 'PrivateIpAddress': '172.31.31.106', 'ProductCodes': [], 'PublicDnsName': 'ec2-50-19-168-29.compute-1.amazonaws.com', 'PublicIpAddress': '50.19.168.29', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-d6205a9b', 'VpcId': 'vpc-e72fe89a', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2020, 10, 9, 10, 27, 56, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-063e0d68f34f475be'}}], 'ClientToken': '6810a996-ef9a-47fb-b1b6-75ec68799b2c', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-50-19-168-29.compute-1.amazonaws.com', 'PublicIp': '50.19.168.29'}, 'Attachment': {'AttachTime': datetime.datetime(2020, 10, 9, 10, 27, 55, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-045e8fe35c14caa10', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached'}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-c6d795f8'}], 'Ipv6Addresses': [], 'MacAddress': '0a:84:09:b7:bc:69', 'NetworkInterfaceId': 'eni-0b17a193a13c49c5a', 'OwnerId': '574832147455', 'PrivateDnsName': 'ip-172-31-31-106.ec2.internal', 'PrivateIpAddress': '172.31.31.106', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-50-19-168-29.compute-1.amazonaws.com', 'PublicIp': '50.19.168.29'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-31-106.ec2.internal', 'PrivateIpAddress': '172.31.31.106'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-d6205a9b', 'VpcId': 'vpc-e72fe89a', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-c6d795f8'}], 'SourceDestCheck': True, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled'}}], 'OwnerId': '574832147455', 'ReservationId': 'r-07afd7770e6ecdac5'}], 'ResponseMetadata': {'RequestId': '9beff560-87bc-488e-ac43-85f1fd016df2', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '9beff560-87bc-488e-ac43-85f1fd016df2', 'content-type': 'text/xml;charset=UTF-8', 'transfer-encoding': 'chunked', 'vary': 'accept-encoding', 'date': 'Fri, 09 Oct 2020 10:55:26 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}


values=response['Reservations']
print(values)
print(type(values)) # O/P: List

for i in values:
    print(i)
    '\n'
    print(type(i)) # O/P: dict
    #if i == 'Instances':
    #    print(i)

# O/P: [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-032930428bf1abbff', 'InstanceId': 'i-02417ddb4e49c97a4', 'InstanceType': 't2.micro', 'KeyName': 'timon', 'LaunchTime': datetime.datetime(2020, 10, 9, 10, 0, 11, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': '', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 48, 'Name': 'terminated'}, 'StateTransitionReason': 'User initiated (2020-10-09 10:20:04 GMT)', 'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': 'c2218ef1-1048-4d4d-a015-b770a772bf25', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [], 'StateReason': {'Code': 'Client.UserInitiatedShutdown', 'Message': 'Client.UserInitiatedShutdown: User initiated shutdown'}, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled'}}], 'OwnerId': '574832147455', 'ReservationId': 'r-0f13ff404057d1fe6'}, {'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-032930428bf1abbff', 'InstanceId': 'i-01ad7860d7d8ae746', 'InstanceType': 't2.micro', 'KeyName': 'timon', 'LaunchTime': datetime.datetime(2020, 10, 9, 10, 27, 55, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-31-106.ec2.internal', 'PrivateIpAddress': '172.31.31.106', 'ProductCodes': [], 'PublicDnsName': 'ec2-50-19-168-29.compute-1.amazonaws.com', 'PublicIpAddress': '50.19.168.29', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-d6205a9b', 'VpcId': 'vpc-e72fe89a', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'AttachTime': datetime.datetime(2020, 10, 9, 10, 27, 56, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-063e0d68f34f475be'}}], 'ClientToken': '6810a996-ef9a-47fb-b1b6-75ec68799b2c', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-50-19-168-29.compute-1.amazonaws.com', 'PublicIp': '50.19.168.29'}, 'Attachment': {'AttachTime': datetime.datetime(2020, 10, 9, 10, 27, 55, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-045e8fe35c14caa10', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached'}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-c6d795f8'}], 'Ipv6Addresses': [], 'MacAddress': '0a:84:09:b7:bc:69', 'NetworkInterfaceId': 'eni-0b17a193a13c49c5a', 'OwnerId': '574832147455', 'PrivateDnsName': 'ip-172-31-31-106.ec2.internal', 'PrivateIpAddress': '172.31.31.106', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-50-19-168-29.compute-1.amazonaws.com', 'PublicIp': '50.19.168.29'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-31-106.ec2.internal', 'PrivateIpAddress': '172.31.31.106'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-d6205a9b', 'VpcId': 'vpc-e72fe89a', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-c6d795f8'}], 'SourceDestCheck': True, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled'}}], 'OwnerId': '574832147455', 'ReservationId': 'r-07afd7770e6ecdac5'}]



### WORKS GREAT #### - Lists all the EC2 Instances Running; - Use this to filter out the key of the instance-id and pass it to next step to 
# terminate the instance

########### STEP 2  - Terminate the instance by filtering the key from above ##########

# For now, input InstanceIds manually;

#response = client.terminate_instances(InstanceIds=['i-02417ddb4e49c97a4',])
#print(response)

### WORKS GREAT###





