import boto3

# deletes an EBS volume

ec2 = boto3.client('ec2')

response = ec2.delete_volume(VolumeId = "vol-0819ddc12732c32e5")

# describes EBS volumes and prints Volume IDs

import time
time.sleep(10) # give it 10 seconds so volume is gone

response = ec2.describe_volumes()

volumes = response["Volumes"]

for volume in volumes:
  print(volume["VolumeId"])
