import boto3

# deletes VPC

ec2 = boto3.client("ec2")

response = ec2.delete_vpc(VpcId="vpc-0dad0dd14c9767a04")

# describes remaining VPCs

response = ec2.describe_vpcs()["Vpcs"]

vpcs = response

for vpc in vpcs:
    print(vpc["VpcId"])