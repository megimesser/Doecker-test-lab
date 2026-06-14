import time

# --- Konfiguration ---
from Testsuite.config import *  # nur das aufzählen, was du hier wirklich nutzt

# --- Seitenaufrufe ---
from Testsuite.seitenaufruf import (
    requester,
    text_writer,
    message_emptyer
)

# --- Gmail ---
from Testsuite.gmail.deleter import delete_all, get_service
from Testsuite.gmail.filter import get_service, main_reader

# --- Messe-Workflows ---
from Testsuite.seitennachricht import aussteller, besucher
from Testsuite.karten import messe_looper, freikarte
from Testsuite.anmeldung import messe_looper_anmeldung, anmeldung

# --- Benachrichtigung ---
from Testsuite.sender import sms_sender, sms_searcher
# Variablendefinition
service = get_service()



# Sender



#Nachrichten im Postfach werden gelöscht
delete_all(service)

#Textdatei wird geleert 
message_emptyer(TXT_PATH, message="")

#Request + in Testdatei schreiben
text_writer(TXT_PATH, requester(HAUPTSEITEN_LINKS))   # Reihenfolge: path, message
text_writer(TXT_PATH, requester(UNTERSEITEN_LINKS))
text_writer(TXT_PATH, requester(UNTERSEITEN_AUSSTELLER))
text_writer(TXT_PATH, requester(UNTERSEITEN_BESUCHER))





# Nachrichten versenden 
aussteller(TEST_MAIL,TEST_NUMMER,MESSAGE)
besucher(TEST_MAIL,TEST_NUMMER,MESSAGE)



# Karten versenden 
messe_looper(TEST_MAIL,MESSE_LOOP)


# warten bis Schnittstellen Nachrichten versendet haben 



# Austeller 
messe_looper_anmeldung(TEST_MAIL,MESSE_LOOP_A)
# Fehlersucher 

time.sleep(60)


#SMS - Sender



main_reader()
sms_searcher(TXT_PATH)