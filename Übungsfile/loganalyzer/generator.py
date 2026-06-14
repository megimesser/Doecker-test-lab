import random 
import datetime
import time
import os 
from config import *


MESSAGES = ["INFO", "WARNING", "ERROR", "CRITICAL"]
NAMES = ["Laura", "Max", "Peter", "Günther", "Paul"]
FEHLER = ["Waschbecken nicht sauber", "Datenbank nicht erreichbar", "Login erfolgreich", "Laura hat einen fahren lassen"]
PFAD = LOG_DATA


message = ""

f= 1
while f < 200:
    x = datetime.datetime.now()
    x = str(x).split()
    x[1] = x[1][0:8] 
    l = random.choice(MESSAGES)
    fail = random.choice(FEHLER)
    user = random.choice(NAMES)
    string_a = f"{x[0]} {x[1]} {l} {fail} user={user}\n"
    message += string_a
    time.sleep(0.5)
    f +=1 
 

with open(LOG_DATA, "w") as f:
    f.write(message)



print(message)