from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

# Elemanı doğru bir yöntemle buluyoruz
searchInput = driver.find_element(By.NAME, "q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)



driver.close()
