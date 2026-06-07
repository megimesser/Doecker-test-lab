from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


test_mail = "testautomationheinze@gmail.com"

vorname = "Testautomation"
nachname = "Testautomation"
messe = "Messe Duisburg"


messe_loop = ["Messe Duisburg","Messe Kaiserslautern","Messe Moers", "Messe Düren", "Messe Düsseldorf", "Messe Hückelhoven - (bald erhältlich)"]


def messe_looper(test_mail, messe_loop):
    for i in messe_loop:
        freikarte(test_mail, i)



def freikarte(test_mail, messe):

  

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.wohnbautrend.de/messeticket-formular")

        print(driver.title)

        # Felder finden
        vorname_input = wait.until(
            EC.presence_of_element_located((By.ID, "Vorname"))
        )

        nachname_input = driver.find_element(By.ID, "Nachname")

        # ID ohne Punkt!
        mail_input = driver.find_element(By.ID, "Mail")

        messe_dropdown = driver.find_element(By.ID, "Messe")

        checkbox = driver.find_element(By.ID, "checkbox-2")

        submit = driver.find_element(
            By.CSS_SELECTOR,
            ".submit-button-4.w-button"
        )

        # Formular ausfüllen
        vorname_input.send_keys(vorname)
        nachname_input.send_keys(nachname)
        mail_input.send_keys(test_mail)

        select = Select(messe_dropdown)
        select.select_by_visible_text(messe)

        checkbox.click()

        time.sleep(1)

        submit.click()

        time.sleep(5)

    finally:
        driver.quit()


if __name__ == "__main__":
    messe_looper(test_mail,messe_loop)
    #freikarte(test_mail, messe)
    