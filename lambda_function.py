import json
from urllib import request

##################################################################
# IMPORTANT
# ---------
# Make sure that you remove all the comments and whitespaces while
# uploading your code to lambda functions, as they use GB-s as a
# measure for cost, so I believe, may be wrong also, that the code
# should be as compact as possible to reduce the cost
###################################################################

def lambda_handler(event, context):
    # Since python has None for null, False and True, so to make the JSON file
    # compatible with python, the variables are created so that python will 
    # on it's own assigned the proper Python-ish value to the JSON values
        
    null = None
    false = False
    true = True

    try:
        # The body part of the JSON request is actually a string, as it starts
        # with double-quotes(""). So to convert it into json

        body = json.loads(event["body"])
        
        # fetch the chatID and message from the body
        # And don't forget to convert the int-type chat
        # ID to string as we'll need to concatenate it
        # later in our send_text string and then an int
        # will cause error

        bot_chatID = str(body["message"]["chat"]["id"])
        bot_message = body["message"]["text"]

        #Look documentation for concept of fixed URL

        fixed_url = <fixedURL>
        
        #call the telegram API endpoint to send back the reply
        
        send_text = fixed_url + '%2FsendMessage?chat_id=' + bot_chatID + '&text=' + bot_message
        request.urlopen(send_text)

    except Exception as e:
        print(e)
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'}
    }
