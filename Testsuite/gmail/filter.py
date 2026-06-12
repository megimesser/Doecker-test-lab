from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import os
import re
import datetime
import time

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
txt_path = "test.txt"

def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as f:
            f.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)


def get_body(payload):
    mime = payload.get('mimeType', '')
    data = payload.get('body', {}).get('data')

    # Leaf-Node mit Klartext
    if mime == 'text/plain' and data:
        return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')

    # Kinder durchlaufen; bevorzugt plain, sonst html merken
    html = ''
    for part in payload.get('parts', []):
        text = get_body(part)
        if text:
            if part.get('mimeType') == 'text/html':
                html = text          # merken, aber weiter nach plain suchen
            else:
                return text
    if html:
        return html

    # Fallback für reine text/html-Mails
    if mime == 'text/html' and data:
        return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')

    return ''


def get_all_message_ids(service, query=None):
    ids = []
    page_token = None
    while True:
        resp = service.users().messages().list(
            userId='me',
            maxResults=500,
            pageToken=page_token,
            q=query
        ).execute()

        ids.extend(m['id'] for m in resp.get('messages', []))

        page_token = resp.get('nextPageToken')
        if not page_token:
            break
    return ids




def has_pdf_attachment(service, message_id):
    msg = service.users().messages().get(
        userId='me', id=message_id, format='full'
    ).execute()

    payload = msg['payload']

    for part in payload.get('parts', []):
        filename = part.get('filename', '')
        mime = part.get('mimeType', '')
        if filename.lower().endswith('.pdf') or mime == 'application/pdf' or filename.lower().endswith('.jpg') :
            return True

#Twillio sender einfügen 
    return False



# Prüfung Anzahl der Nachrichten - 14 - Stück 
def zähler(ids):
    if ids != 14:
        print("Fehler : vorhandene Anzahl ist nicht korrekt")
    else: 
        print("anzahl korrekt")

# textwriter
def text_writer(message, path="../test.txt"):
    with open(path, "a") as f:
        f.writelines(message)





#Prüfung für Nachrichtenversand
def main_reader():
    service = get_service()
    message_string=""

    #Prüfung für Nachrichtenversand

    # q=None holt ALLE Mails. Zum Filtern z.B. q='is:unread' oder q='newer_than:7d'
    message_ids = get_all_message_ids(service, query=None)
    print(f'{len(message_ids)} Nachrichten gefunden')
    zähler(len(message_ids))


    for i, mid in enumerate(message_ids, 1):
        
        msg = service.users().messages().get(
            userId='me', id=mid, format='full'
        ).execute()

        #has_pdf_attachment(service, message_id=mid)
        print(message_string)

        




        headers = {h['name']: h['value'] for h in msg['payload'].get('headers', [])}
        subject = headers.get('Subject', '(kein Betreff)')
        sender = headers.get('From', '(unbekannt)')
        body = get_body(msg['payload'])


        # Prüfung Anmeldedaten 
        if re.search("^Ihre", subject) and has_pdf_attachment(service, message_id=mid) == True:

            #def anmeldeprüfer()
            #print(body)
            f = subject.split()
            x = f[-1]
            s = f[1]
            #print("da")
            text = f"{s} {x} in Ordnung ✅ "
           
            print(f"{s} {x} in Ordnung ✅ ")
            message_string += f"{text} \n"
            #text_writer(message_string)
            #message_string = ""

        #Prüfung Karten 
        if re.search("^Dein", subject) and has_pdf_attachment(service, message_id=mid) == True:
            f = subject.split()
            x = f[-1]
            s = f[1]
            #print("da")
            text = f"{s} {x} in Ordnung ✅ "
           
            print(f"{s} {x} in Ordnung ✅ ")
            message_string += f"{text} \n"
            #text_writer(message_string)
            #message_string = ""

            
            


        # Prüfung Nachrichten 
        if re.search("Webseite :", subject):
            nachricht = subject.split()
            l = nachricht[-1]
            string = f"{l} wird versendet ✅"
            print(string)
            message_string += f"{string} \n"
            #text_writer(message_string)
            #message_string = ""

 
    text_writer(message_string)
    print(message_string)

        #print(subject)

        #print(f'[{i}/{len(message_ids)}] {sender} — {subject}')
        # ------ hier deine Prüf-Logik mit body ------
        


if __name__ == '__main__':
    main_reader()