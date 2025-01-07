from selenium import webdriver

driver = webdriver.Chrome()

url = "http://sadikturan.com"

driver.get(url)

input("Sayfayı kapatmak için Enter'a basın...")
driver.quit()  # Programı bitirdiğinizde tarayıcıyı kapatır