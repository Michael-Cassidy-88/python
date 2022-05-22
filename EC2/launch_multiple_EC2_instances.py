import boto3

# Launch 2 EC2 Instances

ec2 = boto3.resource("ec2")

response = ec2.create_instances(ImageId = 'ami-0022f774911c1d690',
    InstanceType = 't2.micro',
    MaxCount = 2,
    MinCount = 2)
    
print(response)  # prints [ec2.Instance(id='i-xxxxxxxxxxxxxxxxx'), ec2.Instance(id='i-xxxxxxxxxxxxxxxxx')]
