from selenium import webdriver
import time
import requests


### Links ### 

txt_path = "test.txt"
hauptseiten_links = ["https://example.com/does-not-exist?utm_source=chatgpt.com","https://www.wohnbautrend.de/","https://www.wohnbautrend.de/aussteller-links","https://www.wohnbautrend.de/besucher-links","https://www.wohnbautrend.de/uber-uns","https://www.wohnbautrend.de/aktuelles","https://www.wohnbautrend.de/messeanmeldung","https://www.wohnbautrend.de/messeticket-formular"]


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
            message_string += f"Titel: {titel}\n"
    
    seiten_erreichbar = int(seiten_erreichbar)

    return message_string


### Function callingd ### 

message_emptyer(txt_path, message="")
text_writer(txt_path, requester(hauptseiten_links))   # Reihenfolge: path, message