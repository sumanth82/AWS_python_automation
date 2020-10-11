# This function will list and terminate 1st running  EC2 instance! 
# Run this at the end of the day!!

import boto3
client = boto3.client('ec2')

########### STEP 1  - List all the EC2 instances or describe ##########

response = client.describe_instances()

#print(type(response))   # O/P: dict 
#print(list(response.keys())) # O/P: ['Reservations', 'ResponseMetadata']

values=response['Reservations']

#print(values)
#print(type(values)) # O/P: List

# Let's print the 1st value of this List

print(values[0])
print(type(values[0])) # dict

# Let's print the keys of the dict of the 1st value of the list

print(values[0].keys()) # O/P: dict_keys(['Groups', 'Instances', 'OwnerId', 'ReservationId']) 
print(list(values[0].keys())) # O/P: ['Groups', 'Instances', 'OwnerId', 'ReservationId']

#list_of_instances = list(values[0].keys())

print(values[0]['Instances']) # O/P: List 

list_of_instances = (values[0]['Instances'])

############################ STEP - 2 - LIST AND TERMINATE ALL THE RUNNING INSTANCES ######### WORKS GREAT !

for i in list_of_instances:
    i == 'InstanceId'
    print(i['InstanceId'])   # O/P: i-0d8af7cd6b81b0c22
    response = client.terminate_instances(InstanceIds=[i['InstanceId']])
    print(response)


