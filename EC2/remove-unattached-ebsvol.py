# For an EC2 instance,  a root vol by default will be termintaed upon EC2 termination. 
# Here we will put that to false using - mappings.json file and AWS CLI 

# aws ec2 modify-instance-attribute --instance-id i-01ad7860d7d8ae746 --block-device-mappings file://mapping.json

# Once done EBS vol will show as available in EC2 Console. Now, we will create a Lambda function to find available volumes (not in use)
# and to delete them.

import boto3


def lambda_handler(object, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        
        # List only unattached volumes ('available' vs. 'in-use')
        volumes = ec2.volumes.filter(
            Filters=[{'Name': 'status', 'Values': ['available']}])

        for volume in volumes:
            v = ec2.Volume(volume.id)
            print("Deleting EBS volume: {}, Size: {} GiB".format(v.id, v.size))
            v.delete()