from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from Testsuite.config import CMS_EINTRÄGE, SMS_EMPFAENGER, TXT_PATH
from Testsuite.sender import sms_sender

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)   # einmal global, reicht




def zaehle_items():
    x = driver.execute_script(
        "return document.querySelectorAll('.w-dyn-item').length"
    )
    x = int(x)
    return x



def verzeichnis():
    driver.get("https://www.wohnbautrend.de/ausstellerverzeichnis")
    Datenbankeinträge = 0
    # Filter 1: Kleinwohnung (radio-kl)
    driver.find_element(By.ID, "radio-kl").click()
    print("Filter 'kl' geklickt")
    time.sleep(2)  # Finsweet kurz austauschen lassen
    Datenbankeinträge += zaehle_items()
    
    print(f"{zaehle_items()} Items nach Filter 'kl'")
    

    # Filter 2: Moderne (radio-mo) — nach Refresh NEU suchen
    driver.refresh()
    driver.find_element(By.ID, "radio-mo").click()
    print("Filter 'mo' geklickt")
    time.sleep(2)
    
    print(f"{zaehle_items()} Items nach Filter 'mo'")
    Datenbankeinträge += zaehle_items()

    return Datenbankeinträge

def counter_cms(anzahl):
    if anzahl != CMS_EINTRÄGE:
        meldung = "Fehler : vorhandene Anzahl ist nicht korrekt - CMS"
        print(meldung)
        sms_sender(nachricht=meldung, empfaenger=SMS_EMPFAENGER)
        text_writer(meldung)
        driver.quit()
    else:
        print("anzahl korrekt")
        meldung_2 = f"\n\n⭐CMS⭐ \n✅ {anzahl} / {CMS_EINTRÄGE} Einträge sind innerhalb des Ausstellerverzeichnisses vorhanden"
        text_writer(meldung_2)
        driver.quit()


def text_writer(message, path=TXT_PATH):
    with open(path, "a") as f:
        f.write(message)


#test



#driver.quit()

if __name__ == "__main__":
    #print(verzeichnis())
    #input("Enter drücken zum Schließen...")
    #driver.quit()
    counter_cms(verzeichnis())