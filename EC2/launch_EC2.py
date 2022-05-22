import boto3

# Launch EC2 Instance

ec2 = boto3.resource("ec2")

response = ec2.create_instances(ImageId = 'ami-0022f774911c1d690',
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1)
    
print(response)  # prints [ec2.Instance(id='i-xxxxxxxxxxxxxxxxx')]