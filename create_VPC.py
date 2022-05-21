import boto3

# create VPC

ec2 = boto3.client("ec2")

response = ec2.create_vpc(CidrBlock='10.0.0.0/16')

print(response) 