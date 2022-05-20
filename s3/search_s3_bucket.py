import boto3

s3 = boto3.client('s3')
response = s3.list_buckets() # list buckets

buckets = response["Buckets"] 

for bucket in buckets:
    print(bucket["Name"]) 
    
print('\n') # prints a new line

s3 = boto3.client('s3')
response = s3.list_objects(Bucket = "mcass-boto3-bucket-88-private") # lists objects in bucket

print(response) 
