# --- Konfiguration ---
from Testsuite.config import SMS_EMPFAENGER, TXT_PATH  # nur das aufzählen, was du hier wirklich nutzt

# --- Seitenaufrufe ---
from Testsuite.seitenaufruf import (
    requester,
    hauptseiten_links,
    unterseiten_links,
    unterseiten_aussteller,
    unterseiten_besucher,
    txt_path,
)

# --- Gmail ---
from Testsuite.gmail.deleter import delete_all
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
message_emptyer(txt_path, message="")

#Request + in Testdatei schreiben
text_writer(txt_path, requester(hauptseiten_links))   # Reihenfolge: path, message
text_writer(txt_path, requester(unterseiten_links))
text_writer(txt_path, requester(unterseiten_aussteller))
text_writer(txt_path, requester(unterseiten_besucher))





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
sms_searcher(txt_path)