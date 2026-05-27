from selenium import webdriver
import time
import requests
import os 
from dotenv import load_dotenv



### Links ### 

txt_path = "test.txt"
hauptseiten_links = ["https://example.com/does-not-exist?utm_source=chatgpt.com","https://www.wohnbautrend.de/","https://www.wohnbautrend.de/aussteller-links","https://www.wohnbautrend.de/besucher-links","https://www.wohnbautrend.de/uber-uns","https://www.wohnbautrend.de/aktuelles","https://www.wohnbautrend.de/messeanmeldung","https://www.wohnbautrend.de/messeticket-formular"]
unterseiten_links = ["https://www.wohnbautrend.de/messeunterseiten/duisburg","https://www.wohnbautrend.de/messeunterseiten/wohn-bau-trend-kaiserslautern","https://www.wohnbautrend.de/messeunterseiten/moers","https://www.wohnbautrend.de/messeunterseiten/dueren","https://www.wohnbautrend.de/messeunterseiten/huckelhoven","https://www.wohnbautrend.de/messeunterseiten/duesseldorf"]
unterseiten_aussteller = ["https://www.wohnbautrend.de/ausstellerunterseiten/duisburg-aussteller","https://www.wohnbautrend.de/ausstellerunterseiten/aussteller---wohn-bau-trend-kaiserslautern","https://www.wohnbautrend.de/ausstellerunterseiten/moers-aussteller","https://www.wohnbautrend.de/ausstellerunterseiten/dueren-aussteller","https://www.wohnbautrend.de/ausstellerunterseiten/huckelhoven-aussteller","https://www.wohnbautrend.de/messeunterseiten/duesseldorf"]
unterseiten_besucher = ["https://www.wohnbautrend.de/besucherunterseiten/duisburg-besucher","https://www.wohnbautrend.de/besucherunterseiten/kaiserslautern-besucher","https://www.wohnbautrend.de/besucherunterseiten/moers-besucher","https://www.wohnbautrend.de/besucherunterseiten/dueren-besucher","https://www.wohnbautrend.de/besucherunterseiten/huckelhoven-besucher","https://www.wohnbautrend.de/besucherunterseiten/duesseldorf-besucher"]
### Functions ###

def message_emptyer(path,message):
    with open(path,"w") as f:
        f.writelines(message)


def text_writer(path, message):
    with open(path, "a") as f:
        f.writelines(message)


def requester(links):
    message_string = ""                         # vor der Schleife
    seiten_erreichbar = 0

    for i in links:
        response = requests.get(i)
        if response.status_code == 200:
            print(f"✅ Status {response.status_code} — Seite erreichbar")
            driver = webdriver.Chrome()
            driver.get(i)
            titel = driver.title                # titel VORHER speichern
            print(f"Titel: {titel}")
            time.sleep(10)
            driver.quit()                       # jetzt erst beenden
            seiten_erreichbar += 1
            message_string += f"✅ Status {response.status_code} — Seite erreichbar\n"
            message_string += f"Titel: {titel}\n"
        else:
            print(f"❌ Status {response.status_code} — Seitenaufruf fehlgeschlagen")
            message_string += f"❌ Status {response.status_code} — fehlgeschlagen\n"
            #message_string += f"Titel: {titel}\n"
    
    seiten_erreichbar = int(seiten_erreichbar)

    return message_string


### Function callingd ### 

if __name__ == "__main__":
    message_emptyer(txt_path, message="")
    ergebnis = requester(hauptseiten_links)
    text_writer(txt_path, ergebnis)