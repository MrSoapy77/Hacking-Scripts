from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path to the chromedriver
# executable on your computer. Use a raw string (r'...') on Windows so
# backslashes are not treated as escape sequences.
CHROMEDRIVER_PATH = r'C:\path\to\chromedriver.exe'

# Selenium 4 no longer accepts the driver path as a positional argument.
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH))

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Friend\'s Name"'

# Replace the below string with your own message
string = "Message sent using Python!!!"

# How many times to send the message
MESSAGE_COUNT = 1

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for _ in range(MESSAGE_COUNT):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
