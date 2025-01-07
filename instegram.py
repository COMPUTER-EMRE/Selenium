from instegramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Instegram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)

        # Kullanıcı adı ve şifre giriş alanlarını bulup bilgi gönderiyoruz
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)

        # Giriş butonuna tıklıyoruz
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()
        time.sleep(10)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)

        # Takipçi linkini bulup tıklıyoruz
        self.browser.find_element(By.XPATH, "//a[contains(@href,'/followers')]").click()
        time.sleep(2)

        # Takipçi listesini içeren pencereyi bekleyip yüklenene kadar bekliyoruz
        try:
            follower_list = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul"))
            )
        except:
            print("Takipçi listesi yüklenemedi.")
            self.browser.quit()
            return

        # Scroll yapmak için yüksekliği sabitliyoruz
        last_height, new_height = 0, 1
        while last_height != new_height:
            last_height = self.browser.execute_script("return arguments[0].scrollHeight", follower_list)
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_list)
            time.sleep(2)
            new_height = self.browser.execute_script("return arguments[0].scrollHeight", follower_list)

        # Tüm takipçileri alıyoruz
        followers = follower_list.find_elements(By.CSS_SELECTOR, "li")

        for user in followers:
            # Takipçinin profil linkini alıyoruz
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            print(link)

# Kullanıcı adı ve şifre ile giriş yapıp takipçileri listeleyen fonksiyonları çalıştırıyoruz
instegram = Instegram(username, password)
instegram.signIn()
instegram.getFollowers()
