from seitenaufruf import requester
from seitenaufruf import *
from seitenaufruf import hauptseiten_links
from seitenaufruf import txt_path


#Textdatei leeren
message_emptyer(txt_path, message="")

#Request + in Testdatei schreiben
text_writer(txt_path, requester(hauptseiten_links))   # Reihenfolge: path, message