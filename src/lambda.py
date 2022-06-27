from numpy import random

def handler(event, context):

    if event['type'] == 'dev':
        return f'Dev\n {random.randint(100)}'

    if event == 'prod':
        return  f'Prod\n'