from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


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


def main():
    service = get_service()

    # q=None holt ALLE Mails. Zum Filtern z.B. q='is:unread' oder q='newer_than:7d'
    message_ids = get_all_message_ids(service, query=None)
    print(f'{len(message_ids)} Nachrichten gefunden')

    LIMIT = 50  # Sicherheits-Cutoff fürs Testen. Auf None setzen für alle.

    for i, mid in enumerate(message_ids, 1):
        if LIMIT and i > LIMIT:
            print(f'... gestoppt bei {LIMIT} (LIMIT auf None setzen für alle)')
            break

        msg = service.users().messages().get(
            userId='me', id=mid, format='full'
        ).execute()

        headers = {h['name']: h['value'] for h in msg['payload'].get('headers', [])}
        subject = headers.get('Subject', '(kein Betreff)')
        sender = headers.get('From', '(unbekannt)')
        body = get_body(msg['payload'])

        print(f'[{i}/{len(message_ids)}] {sender} — {subject}')
        # ------ hier deine Prüf-Logik mit body ------


if __name__ == '__main__':
    main()