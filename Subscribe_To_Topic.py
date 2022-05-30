# subscribes to SNS topic

import boto3
import time

def create_sns_subscription(topic, protocol, endpoint, sns = None):
    if sns is None:
        sns = boto3.client("sns")
        

    response = sns.subscribe(
        TopicArn=topic,
        Protocol=protocol,
        Endpoint=endpoint,)
    
    print("Creating Subscription...")
    time.sleep(1)
    return response
    
if __name__ == '__main__':
    create_sns_subscription("<SNS_ARN>", "email", "<YOUR_EMAIL_HERE>")
    print("Subscribed. Make sure to confirm subscription.") 