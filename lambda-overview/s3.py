import boto3

# The below sample uses high-level resource object

s3=boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)                   #O/P: timeddsad


# The below sample uses low-level client object

client=boto3.client('s3')
response=client.list_buckets()
print(response)

# O/P: {'ResponseMetadata': {'RequestId': '519570530CBC5365', 'HostId': 'EZleDE9aelRI9W+BoaY30gWqqF3l2spfsSQ3P7N865S8+O0EzYBjRK1qCIJ5nTwQwGMbM5oOQR0=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'EZleDE9aelRI9W+BoaY30gWqqF3l2spfsSQ3P7N865S8+O0EzYBjRK1qCIJ5nTwQwGMbM5oOQR0=', 'x-amz-request-id': '519570530CBC5365', 'date': 'Wed, 07 Oct 2020 10:59:10 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'timeddsad', 'CreationDate': datetime.datetime(2020, 10, 6, 10, 38, 25, tzinfo=tzutc())}], 'Owner': {'DisplayName': 'sumant.renukarya', 'ID': 'b67155a35aba37ca19b1505d5b02a6fdcaa5ba034da93f777d903a759a8537eb'}}





