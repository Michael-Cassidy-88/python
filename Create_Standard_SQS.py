# creates a standard SQS Queue

import boto3
import time

def create_message_queue(sqs = None):
    if sqs is None:
        sqs = boto3.client("sqs")
        

    response = sqs.create_queue(QueueName='Message_In')
    print("Creating Queue...")
    time.sleep(1)
    return response
    
if __name__ == '__main__':
    Message_In = create_message_queue()
    print("Queue Created") 