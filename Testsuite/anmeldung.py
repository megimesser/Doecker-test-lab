from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from config import *



def messe_looper_anmeldung(TEST_MAIL, MESSE_LOOP):
    for i in MESSE_LOOP:
        anmeldung(TEST_MAIL, i)



def anmeldung(TEST_MAIL, messe):

   

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
        time.sleep(1)
        unternehmen_input.send_keys("Testautomation")
        time.sleep(1)
        select = Select(branche_dropdown)
        time.sleep(1)
        select.select_by_visible_text("Camping")
        time.sleep(1)
        mail_input.send_keys(TEST_MAIL)
        time.sleep(1)
        number_input.send_keys("01602986822")
        time.sleep(1)
        message_input.send_keys("Dies ist ein automatisches Testscript")
        time.sleep(1)

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
    messe_looper_anmeldung(TEST_MAIL,MESSE_LOOP)
