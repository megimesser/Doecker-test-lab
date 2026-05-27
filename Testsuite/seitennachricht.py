from selenium import webdriver
import time
import requests
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time




driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)



driver.get("https://www.wohnbautrend.de")

title = driver.title
print(title)

field_1 = driver.find_element(by=By.CLASS_NAME, value="w-input")
field_1.send_keys("Selenium")
#submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


time.sleep(30)

driver.implicitly_wait(100)

