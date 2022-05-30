# creates an SNS topic

import boto3
import time

def create_sns_topic(sns = None):
    if sns is None:
        sns = boto3.client("sns")
        

    response = sns.create_topic(Name='Publish_Message')
    print("Creating Topic...")
    time.sleep(1)
    return response
    
if __name__ == '__main__':
    Publish_Message = create_sns_topic()
    print("Topic Created") 
