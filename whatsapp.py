
from http.server import executable
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as ts
import datetime as dt
import sys
from configLocal import BRAVE_PROFILE_PATH

# print(sys.argv)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
options.add_argument(BRAVE_PROFILE_PATH)
driverService = Service(r"C:\Users\otheruser\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=driverService, options=options)

driver.get('https://www.google.com')
# catch element an write
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("clima" + Keys.ENTER)
# precipitation = driver.find_element(By.ID, "wob_rain")

precipitation = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.ID, "wob_rain"))
)
precipitation.click()

timeNow = str(dt.datetime.now())
timeNow = timeNow.replace(':', '-')
timeNow = timeNow.replace('.', '-')
print(timeNow)
loadScreen = f'C:/Users/otheruser/Pictures/{timeNow}.png'
driver.save_screenshot(loadScreen)
driver.get('https://web.whatsapp.com')
with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()


for group in groups:
    search_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    # search_box.send_keys(group)

    search_box = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    search_box.send_keys(group)

    group_path = f'//span[@title="{group}"]'
    group_title = driver.find_element(By.XPATH, group_path)
    group_title.click()
    ts.sleep(1)
    input_send = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    clip_doc = driver.find_element(By.XPATH, '//span[@data-icon="clip"]')
    clip_doc.click()
    # ts.sleep(1)
    # attach_doc = driver.find_element(By.XPATH, '//span[@data-icon="attach-image"]')
    # attach_doc.click()
    ts.sleep(1)
    input_image = driver.find_element(By.XPATH, '//input[@type="file"]')

    input_image.send_keys(loadScreen,Keys.ENTER)

    # pyperclip.copy()


# if we want pass more than 1 group
#  pyperclip.copy(group)
# search_box.send_keys(Keys.CONTROL + "V")
