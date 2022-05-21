import boto3

# describes VPCs

ec2 = boto3.client("ec2")

response = ec2.describe_vpcs()["Vpcs"]

vpcs = response

for vpc in vpcs:
    print(vpc["VpcId"])
