from dotenv import load_dotenv
import os
from twilio.rest import Client
import re


load_dotenv()
path = "test.txt"

def sms_sender(nachricht, empfaenger):
    #Head twillio

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=nachricht,
        from_=twilio_nummer,
        to=empfaenger
    )
    print(f"SMS gesendet — SID: {message.sid}")
#test





def sms_searcher(path):
    with open(path,"r") as f:
        daten = f.read()
    x = re.search("fehlgeschlagen", daten)
    print(type(x))
    x = bool(x)
    if x == True:
        sms_sender(nachricht="hi", empfaenger="+491602986823")
    return x
        
print(sms_searcher(path))






#sms_sender(nachricht="hi", empfaenger="+491602986823")


