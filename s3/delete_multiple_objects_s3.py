import boto3

# deleting all objects in s3 bucket

s3 = boto3.client('s3')

response = s3.list_objects(Bucket = "mcass-boto3-bucket-88-private")

for object in response['Contents']:
    print('Deleting', object['Key'])
    s3.delete_object(Bucket = "mcass-boto3-bucket-88-private", Key = object['Key'])
