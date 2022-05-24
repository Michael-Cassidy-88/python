import boto3


def create_food_table(dynamodb = None):

    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb')

    table_name = 'food_table'
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'description', 'KeyType': 'HASH'},
            {'AttributeName': 'macronutrient', 'KeyType': 'RANGE'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'description', 'AttributeType': 'S'},
            {'AttributeName': 'macronutrient', 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }
    table = dynamodb.create_table(**params)
    print(f"Creating {table_name}...")
    table.wait_until_exists()
    return table


if __name__ == '__main__':
    food_table = create_food_table()
    print(f"Created table.")
    