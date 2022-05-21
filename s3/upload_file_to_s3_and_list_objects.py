import boto3

# uploads a file to an s3 bucket 

s3 = boto3.client('s3')
response = s3.upload_file( 
    Filename = 'Python_Study.png', 
    Bucket = 'mcass-boto3-bucket-88-private', 
    Key = 'Python_Study.png')
    
response = s3.list_objects(Bucket = "mcass-boto3-bucket-88-private")["Contents"] # sets the reponse to list the contents of the object in the bucket

objects = response

for object in objects:
    print(object["Key"]) # prints the object key
