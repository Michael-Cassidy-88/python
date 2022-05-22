import boto3

# creates a snapshot from an EBS volume

ec2 = boto3.client('ec2')

response = ec2.create_snapshot(VolumeId = 'vol-0a7dc560654931301')

# prints the snapshot ID

response = ec2.describe_snapshots(
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [
                'vol-0a7dc560654931301',
            ]
        },
    ]
)

snapshots = response["Snapshots"]

for snapshot in snapshots:
    print(snapshot["SnapshotId"])