import boto3


def scan_food_table(dynamodb = None):
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('food_table')
    response = table.scan()['Items']
    for item in response:
        print (item)
    return response
    
if __name__ == '__main__':
    food_table = scan_food_table()
    print(f"Table scanned.")    