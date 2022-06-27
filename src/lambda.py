import process.prod as prod_code

def handler(event, context):

    if event['type'] == 'prod':
        return  prod_code.func('test')
    elif event['type'] == "dev":
        try:
            import process.dev as dev_code
            return dev_code.func('test')
        except:
            print('Failed')
            pass

        