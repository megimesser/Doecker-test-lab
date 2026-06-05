from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


test_mail = "testautomationheinze@gmail.com"
number = "01602986822"

vorname = "Testautomation"
#messe = "Messe Duisburg"
message = "Dies ist ein automatisches Testscript"


messe_loop = ["Messe Duisburg","Messe Kaiserslautern","Messe Moers","Messe Düren","Messe Düsseldorf","Messe Hückelhoven"]


def messe_looper_anmeldung(test_mail, messe_loop):
    for i in messe_loop:
        anmeldung(test_mail, i)



def anmeldung(test_mail, messe):

   

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.wohnbautrend.de/messeanmeldung-formular")

        print(driver.title)

        # Felder finden
        ansprechpartner_input = wait.until(
            EC.presence_of_element_located((By.ID, "Ansorechpartner"))
        )

        unternehmen_input = driver.find_element(By.ID, "Unternehmen")

        branche_dropdown = driver.find_element(By.ID, "Branche")

        # ID ohne Punkt!
        mail_input = driver.find_element(By.ID, "Email-4")

        number_input = driver.find_element(By.ID, "Telefonnummer")

        message_input = driver.find_element(By.ID, "Nachricht")

        messe_dropdown = driver.find_element(By.ID, "Messeauswahl")

        checkbox = driver.find_element(By.ID, "Aussteller")

    



        submit = driver.find_element(
            By.ID,
            "submitter"
        )

        # Formular ausfüllen
        ansprechpartner_input.send_keys("Testautomation")
        unternehmen_input.send_keys("Testautomation")
        select = Select(branche_dropdown)
        select.select_by_visible_text("Camping")
        mail_input.send_keys(test_mail)
        number_input.send_keys("01602986822")
        message_input.send_keys("Dies ist ein automatisches Testscript")

        select = Select(messe_dropdown)
        select.select_by_visible_text(messe)

        checkbox.click()

        time.sleep(1)

        submit.click()

        time.sleep(5)

        

    finally:
        driver.quit()


if __name__ == "__main__":
    #freikarte(test_mail, messe)
    messe_looper_anmeldung(test_mail,messe_loop)
