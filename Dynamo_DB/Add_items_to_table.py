import boto3


def write_food_table(description, macronutrient, micronutrient, dynamodb = None):
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('food_table')
    response = table.put_item(
        Item = {
            'description': description,  # partition key
            'macronutrient': macronutrient,  # sort key 
            'micronutrient': micronutrient, # some data
        }
    )
    print(f"Creating item...")
    return response


if __name__ == '__main__':
    food_table = write_food_table("Bacon", "Fat", "VitB")
    food_table2 = write_food_table("Steak", "Protein", "VitB")
    food_table3 = write_food_table("Eggs", "Protein", "Choline")
    food_table4 = write_food_table("Spinach", "Carb", "VitK")
    food_table5 = write_food_table("Potato", "Carb", "VitC")
    food_table6 = write_food_table("Carrot", "Carb", "VitA")
    food_table7 = write_food_table("Butter", "Fat", "VitA")
    food_table8 = write_food_table("Blueberry", "Carb", "Fiber")
    food_table9 = write_food_table("DarkChocolate", "Fat", "Magnesium")
    food_table10 = write_food_table("CoffeeBean", "Carb", "ChlorogenicAcid")
    print(f"Items created")