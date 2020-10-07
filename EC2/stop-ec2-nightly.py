# This Lambda function will stop the EC2 instances nightly in multiple regions.
# In order to invoke this lambda, you create a Cloudwatch Rule, set a schedule and select this lambda function as a target. 
# 

import boto3

def lambda_handler(event, context):
    
    # Get a list of all the regions 

    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
        #print(regions)
        for region in ec2_client.describe_regions()['Regions']]
    # regions is a list, which gets the value of each region and assigns to regions variable

    # Iterate over each region

    for region in regions:
        ec2=boto3.resource('ec2', region_name=region)

        print("Region is: ", region)
    
    # Get Only Running Instances

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['Running']}])

    # Stop the instances

    for instance in instances:
        instances.stop()
        print('Stopped instance: ', instance.id)


    




