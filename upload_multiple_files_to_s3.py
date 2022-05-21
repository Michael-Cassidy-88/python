import boto3
import os
import glob

cwd = os.getcwd()
files = glob.glob(cwd+"/*.py")
for file in files:
    s3 = boto3.client("s3")
    response = s3.upload_file(
    Filename = file,
    Bucket = "mcass-boto3-bucket-88-private",
    Key = file.split("/")[-1]
    )

response = s3.list_objects(Bucket = "mcass-boto3-bucket-88-private")["Contents"] # sets the response to list the contents of the object in the bucket

objects = response

for object in objects:
    print(object["Key"]) # prints the object key