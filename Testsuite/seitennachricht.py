from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

from config import TEST_MAIL, TEST_NUMMER, MESSAGE


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

def aussteller(TEST_MAIL, TEST_NUMMER, MESSAGE):
    driver.get("https://www.wohnbautrend.de")

    print(driver.title)

    driver.implicitly_wait(10)

    name = driver.find_element(By.CSS_SELECTOR, ".w-input")
    mail = driver.find_element(By.CSS_SELECTOR, ".text-field-2.w-input")
    nummer = driver.find_element(By.CSS_SELECTOR, ".spacer-form.w-input")
    nachricht = driver.find_element(By.ID, "Ihre-Nachricht")
    confirm = driver.find_element(By.ID, "checkbox-2")
    dropdown = driver.find_element(By.ID, "Sie-sind")
    submit = driver.find_element(By.CSS_SELECTOR, ".submit-button.w-button")


    name.send_keys("Testautomation")
    mail.send_keys(TEST_MAIL)
    nummer.send_keys(TEST_NUMMER)
    select = Select(dropdown)
    select.select_by_visible_text("Aussteller")
    nachricht.send_keys(MESSAGE)
    confirm.click()
    submit.click()
    time.sleep(5)


def besucher(TEST_MAIL, TEST_NUMMER, MESSAGE):
    driver.get("https://www.wohnbautrend.de")

    print(driver.title)

    driver.implicitly_wait(10)

    name = driver.find_element(By.CSS_SELECTOR, ".w-input")
    mail = driver.find_element(By.CSS_SELECTOR, ".text-field-2.w-input")
    nummer = driver.find_element(By.CSS_SELECTOR, ".spacer-form.w-input")
    nachricht = driver.find_element(By.ID, "Ihre-Nachricht")
    confirm = driver.find_element(By.ID, "checkbox-2")
    dropdown = driver.find_element(By.ID, "Sie-sind")
    submit = driver.find_element(By.CSS_SELECTOR, ".submit-button.w-button")


    name.send_keys("Testautomation")
    mail.send_keys(TEST_MAIL)
    nummer.send_keys(TEST_NUMMER)
    select = Select(dropdown)
    time.sleep(2)
    select.select_by_visible_text("Besucher")
    time.sleep(2)
    nachricht.send_keys(MESSAGE)
    confirm.click()
    submit.click()
    time.sleep(5)









### Function callingd ### 

if __name__ == "__main__":
    aussteller(TEST_MAIL,TEST_NUMMER,MESSAGE)
    besucher(TEST_MAIL,TEST_NUMMER,MESSAGE)

