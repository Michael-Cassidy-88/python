import boto3

# creates an EBS volume from a snapshot

ec2 = boto3.client("ec2")

response = ec2.create_volume(
      AvailabilityZone='us-east-1f',
      Encrypted=True,
      Size=8,
      SnapshotId='snap-04f5827b79204719e',
      VolumeType='gp2')

# describes EBS volume created from snapshot and prints Volume ID

response = ec2.describe_volumes(
    Filters=[
        {
            'Name': 'snapshot-id',
            'Values': [
                'snap-04f5827b79204719e',
            ]
        },
    ]
)

volumes = response["Volumes"]

for volume in volumes:
  print(volume["VolumeId"])