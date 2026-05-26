from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.chrome.options import Options
import json

driver = webdriver.Chrome()
jsson_path = "test.json"
txt_path = "test.txt"

hauptseiten_links = ["https://www.wohnbautrend.de/"]
                     #,"https://www.wohnbautrend.de/aussteller-links","https://www.wohnbautrend.de/besucher-links","https://www.wohnbautrend.de/uber-uns","https://www.wohnbautrend.de/aktuelles","https://www.wohnbautrend.de/messeanmeldung","https://www.wohnbautrend.de/messeticket-formular"]
#austeller_seiten = 


#driver.get(link)

#title = driver.title
#options = Options()

#driver.implicitly_wait(0.5)



#url = "https://www.wohnbautrend.de/"

hauptseiten_anzahl = len(hauptseiten_links)
hauptseiten_erreichbar = 0

# Berechnet die Erreichbarkeit aller Seiten
def erreichbarkeit(anzahl, erreichbar):
    erreichbarkeit = erreichbar / anzahl * 100
    return erreichbarkeit


# Öffnet die Json in welche geschrieben werden soll 
def json_opener(path): 
    with open(path, "w") as f: 
        data=json.open(f)
    return data

def text_opener(path): 
    with open(path,"r") as f: 
        data=open(f)
    return data

def text_writer(message,path):
    with open(path,"w") as f: 
        f.writelines(message)


def requester(links):
    for i in links: 
        seiten_erreichbar = 0 
        message_string = ""
        #print(type(i))
        response = requests.get(i)
        if response.status_code == 200:
            print(f"✅ Status {response.status_code} — Seite erreichbar")
            driver = webdriver.Chrome()
            driver.get(i)
            print(f"Titel: {driver.title}")
            time.sleep(10)
            driver.quit()
            seiten_erreichbar += 1
            message_string += (f"✅ Status {response.status_code} — Seite erreichbar")
            message_string += (f"Titel: {driver.title}")
        else:
            print(f"❌ Status {response.status_code} — Seitenaufruf fehlgeschlagen")
        
    return  message_string
        

text_writer(txt_path, requester(hauptseiten_links))



seiten_erreichbar = 0
hauptseiten_erreichbar = seiten_erreichbar   

requester(hauptseiten_links)
x = erreichbarkeit(hauptseiten_anzahl, hauptseiten_erreichbar)

print(f"Erriechbarkeit Hauptseiten bei {x} %")

"""
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.wohnbautrend.de/")



text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")



text_box.send_keys("Selenium")
submit_button.click()



message = driver.find_element(by=By.ID, value="message")
text = message.text
"""


time.sleep(5)
driver.quit()
