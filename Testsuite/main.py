# Requester
from seitenaufruf import requester
from seitenaufruf import *
from seitenaufruf import hauptseiten_links, unterseiten_links, unterseiten_aussteller, unterseiten_besucher
from seitenaufruf import txt_path

from gmail.deleter import delete_all
from gmail.filter import get_service, main_reader
from gmail.reader import get_service

from config import *


from seitennachricht import aussteller,besucher
from karten import messe_looper, freikarte
from anmeldung import messe_looper_anmeldung, anmeldung

# Variablendefinition
service = get_service()



# Sender
#from twillio import sms_sender, sms_searcher



#Nummer = "+491602986823"

#Nachrichten im Postfach werden gelöscht
#delete_all(service)

#Textdatei wird geleert 
#message_emptyer(txt_path, message="")

#Request + in Testdatei schreiben
#text_writer(txt_path, requester(hauptseiten_links))   # Reihenfolge: path, message
#text_writer(txt_path, requester(unterseiten_links))
#text_writer(txt_path, requester(unterseiten_aussteller))
#text_writer(txt_path, requester(unterseiten_besucher))





# Nachrichten versenden 
#aussteller(TEST_MAIL,TEST_NUMMER,MESSAGE)
#besucher(TEST_MAIL,TEST_NUMMER,MESSAGE)



# Karten versenden 
#messe_looper(TEST_MAIL,MESSE_LOOP)


# warten bis Schnittstellen Nachrichten versendet haben 
#time.sleep(60)


# Austeller 
#messe_looper_anmeldung(TEST_MAIL,MESSE_LOOP_A)
# Fehlersucher 

#SMS - Sender
#sms_searcher(txt_path)
#sms_sender(nachricht="fail",empfaenger=Nummer)

main_reader()