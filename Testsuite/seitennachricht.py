from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

test_mail = "anything@uvvtkqpz.mailosaur.net"
testnummer = "01602986882"
message = "Dies ist eine automatisch generierte Nachricht zur Testautomation"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

def aussteller(test_mail, testnummer, message):
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
    mail.send_keys(test_mail)
    nummer.send_keys(testnummer)
    select = Select(dropdown)
    select.select_by_visible_text("Option 1")
    nachricht.send_keys(message)
    confirm.click()
    submit.click()
    time.sleep(5)







### Function callingd ### 

if __name__ == "__main__":
    aussteller(test_mail,testnummer,message)

