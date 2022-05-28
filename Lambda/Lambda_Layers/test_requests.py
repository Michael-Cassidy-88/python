import requests


def lambda_handler(event, context):

    response = requests.get('<website>')
    if response:
        print('Success!')
    else:
        print('An error has occurred.')
