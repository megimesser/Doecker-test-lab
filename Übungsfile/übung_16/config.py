import os 
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Für Secrets falls vorhanden
load_dotenv(os.path.join(BASE_DIR, '.env'))

JSON_FILE = os.path.join(BASE_DIR, "test.json")



