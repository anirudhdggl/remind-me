import json
from urllib import request

def lambda_handler(event, context):
    # TODO implement
    
    try:
        bot_chatID = <chatID>
        bot_message = 
        fixed_url = <fixedURL> #Look documentation for concept of fixed URL
        send_text = fixed_url + '%2FsendMessage?chat_id=' + bot_chatID + '&text=' + bot_message
        request.urlopen(send_text)
    except Exception as e:
        print(e)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'}
    }
