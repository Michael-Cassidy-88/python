import boto3

# deletes a snapshot 

ec2 = boto3.client('ec2')

response = ec2.delete_snapshot(SnapshotId='snap-04f5827b79204719e')

print(response)