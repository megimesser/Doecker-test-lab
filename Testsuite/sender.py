from dotenv import load_dotenv
import os
from twilio.rest import Client
import re
from config import * 


load_dotenv()
path = "test.txt"

def sms_sender(nachricht, empfaenger):
    #Head twillio

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=nachricht,
        from_=TWILIO_NUMBER,
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
        print("gefunden")
        
        #sms_sender(nachricht="hi", empfaenger="+491602986823")
    #return x
        

if __name__ == '__main__':
    sms_searcher(path)
    print(sms_searcher(path))






#sms_sender(nachricht="hi", empfaenger="+491602986823")


