# This function will list and terminate ALL the running  EC2 instances
# Run this at the end of the day!!

import boto3
client = boto3.client('ec2')

########### STEP 1  - List all the EC2 instances or describe ##########

response = client.describe_instances()

#print(type(response))   # O/P: dict 
#print(list(response.keys())) # O/P: ['Reservations', 'ResponseMetadata']

values=response['Reservations']

for i in values:
    list_of_instances = (i['Instances'])

print(list_of_instances)
#print(type(list_of_instances)) # List 


### Fetch the instanceid from the list of Instances

instanceid = []

for i in list_of_instances:
    #instanceid = (i['InstanceId'])
    instanceid.append((i['InstanceId']))

print(instanceid)

# O/P: ['i-03dff901dca11d175', 'i-049fd4d9bbe21314b']

############################ STEP - 2 - LIST AND TERMINATE ALL THE RUNNING INSTANCES ######### WORKS GREAT !

for i in instanceid:
    response = client.terminate_instances(InstanceIds=[i])
    print(response)
