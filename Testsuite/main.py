# Requester
from seitenaufruf import requester
from seitenaufruf import *
from seitenaufruf import hauptseiten_links, unterseiten_links, unterseiten_aussteller, unterseiten_besucher
from seitenaufruf import txt_path

from gmail.deleter import delete_all
from gmail.filter import get_service
from gmail.reader import get_service

# Variablendefinition
service = get_service()



# Sender
#from twillio import sms_sender, sms_searcher



#Nummer = "+491602986823"
delete_all(service)



#Textdatei leeren
message_emptyer(txt_path, message="")

#Request + in Testdatei schreiben
text_writer(txt_path, requester(hauptseiten_links))   # Reihenfolge: path, message
text_writer(txt_path, requester(unterseiten_links))
text_writer(txt_path, requester(unterseiten_aussteller))
text_writer(txt_path, requester(unterseiten_besucher))


#SMS - Sender
#sms_searcher(txt_path)
#sms_sender(nachricht="fail",empfaenger=Nummer)

