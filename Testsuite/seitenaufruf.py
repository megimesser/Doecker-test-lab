from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

link = "https://www.wohnbautrend.de/"

driver.get(link)

title = driver.title
options = Options()

driver.implicitly_wait(0.5)



url = "https://www.wohnbautrend.de/"

response = requests.get(url)

options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.wohnbautrend.de/")



if response.status_code == 200:
    print(f"✅ Status {response.status_code} — Seite erreichbar")
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Titel: {driver.title}")
    time.sleep(10)
    driver.quit()
else:
    print(f"❌ Status {response.status_code} — Seitenaufruf fehlgeschlagen")

"""
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")



text_box.send_keys("Selenium")
submit_button.click()



message = driver.find_element(by=By.ID, value="message")
text = message.text
"""


time.sleep(5)
driver.quit()
