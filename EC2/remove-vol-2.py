import boto3

ec2_client = boto3.client('ec2')
#print(dir(ec2_client))

for region in ec2_client.describe_regions()['Regions']:
        regions = [region['RegionName']]
        print(regions)

# O/P: ['eu-north-1']
#['ap-south-1']
#['eu-west-3']
#['eu-west-2']
#['eu-west-1']
#['ap-northeast-2']
#['ap-northeast-1']
#['sa-east-1']
#['ca-central-1']
#['ap-southeast-1']
#['ap-southeast-2']
#['eu-central-1']
#['us-east-1']
#['us-east-2']
#['us-west-1']
#['us-west-2']

for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Region: ", region)

        # O/P: Region:  us-west-2

## List only unattached volumes:

volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])
print(volumes)

# ec2.volumesCollection(ec2.ServiceResource(), ec2.Volume)

print(type(volumes))

# <class 'boto3.resources.collection.ec2.volumesCollection'>

for volume in volumes:
        v = ec2.Volume(volume.id)
        print(f"Deleting EBS volume: {v.id}, Size: {v.size}")
        #v.delete()




