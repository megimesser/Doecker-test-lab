import os 
import dotenv

# Habe die beiden einfach reinkopiert
# --- Pfade relativ zur Skriptdatei, nicht zum Startverzeichnis ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DATA = os.path.join(BASE_DIR, 'test.log')
JSONI = os.path.join(BASE_DIR, "report.json")