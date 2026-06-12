import os 
from dotenv import load_dotenv


#karten.py 
TEST_MAIL = "testautomationheinze@gmail.com"
VORNAME = "Testautomation"
NACHNAME = "Testautomation"
MESSE_LOOP = ["Messe Duisburg","Messe Kaiserslautern","Messe Moers", "Messe Düren", "Messe Düsseldorf", "Messe Hückelhoven - (bald erhältlich)"]

#seitennachricht.py 
TEST_NUMMER = "01602986882"
MESSAGE = "Dies ist eine automatisch generierte Nachricht zur Testautomation"

#anmeldungen.py
MESSE_LOOP_A = ["Messe Duisburg","Messe Kaiserslautern","Messe Moers", "Messe Düren", "Messe Düsseldorf", "Messe Hückelhoven"]

#filter.py
# --- Pfade relativ zur Skriptdatei, nicht zum Startverzeichnis ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# .env-Datei laden (liegt neben der config.py)
load_dotenv(os.path.join(BASE_DIR, '.env'))

SMS_EMPFAENGER = os.environ.get("SMS_EMPFAENGER", "")

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
TOKEN_PATH = os.path.join(BASE_DIR, 'token.json')
CLIENT_PATH = os.path.join(BASE_DIR, 'client.json')
TXT_PATH = os.path.join(BASE_DIR, 'test.txt')

ERWARTETE_ANZAHL = 14


#sender.py

AUTH_TOKEN = os.environ.get("AUTH_TOKEN", "")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID", "")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER", "")
