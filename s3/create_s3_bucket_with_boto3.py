import boto3

# create a private s3 buckt

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("mcass-boto3-bucket-88-private")

response = bucket.create(  
    ACL='private',
    
    
)

print(response)
