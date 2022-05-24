import boto3


def delete_food_table(dynamodb = None):
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('food_table')
    table.delete()

    print(f"Deleting {table.name}...")
    table.wait_until_not_exists()


if __name__ == '__main__':
    delete_food_table()
    print("Table deleted.")