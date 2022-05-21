import boto3

# deletes a single object from s3 bucket

s3 = boto3.client("s3")


response = s3.delete_object(Bucket = "mcass-boto3-bucket-88-private", 
    Key = "Python_Study.png")

response = s3.list_objects(Bucket = "mcass-boto3-bucket-88-private")["Contents"] # sets the reponse to list the contents of the object in the bucket

objects = response

for object in objects:
    print(object["Key"]) # prints the object key
