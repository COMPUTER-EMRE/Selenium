from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()
        time.sleep(2)

    def getFollowers(self):
        self.browser.get("https://github.com/COMPUTER-EMRE?tab=followers")
        time.sleep(2)

        # Doğru CSS seçiciyi kullanarak elemanları buluyoruz
        items = self.browser.find_elements(By.CSS_SELECTOR, ".Link--secondary")

        # Her elemandaki ismi takipçi listesine ekliyoruz
        for i in items:
            self.followers.append(i.text)  # 'i' bir WebElement olduğundan, i.text ile metni alıyoruz

github = Github(username, password)
github.signIn()
github.getFollowers()
print(github.followers)

# # Takipçi listesinin açılmasını bekle
        # try:
        #     dialog = WebDriverWait(self.browser, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='link'] ul"))
        #     )
        # except Exception as e:
        #     print("Takipçi listesi yüklenemedi:", e)
        #     return

        # # Takipçileri listele
        # followers = dialog.find_elements(By.CSS_SELECTOR, "li")
        # for user in followers:
        #     username = user.find_element(By.CSS_SELECTOR, "span a").text
        #     print(username)

