import json
import boto3
 
def is_a_queue(event):
    return not bool(event.get('Records'))


def read_queue(event):
    records = []
    for record in event.get('Records', []):
        records.append(json.loads(record.get('body')))

    return records

def lambda_handler(event, context):
    if is_a_queue(event):
        records = read_queue(event)
    else:
        records = [event]
        
    for item in records:
        print(item)
        
    
    
        sns = boto3.client("sns")
        response = sns.publish (
            TargetArn = "<SNS_ARN>",
            Message = json.dumps(event, indent=2),
            Subject = "SQS Polled"
        )

    return {
        'statusCode': 200,
        'body': str(len(records)) + ' processed'
    }
