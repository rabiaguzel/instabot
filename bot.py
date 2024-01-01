from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get("https://www.instagram.com")
time.sleep(10)
login=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[2]/p/a')
login.click()
time.sleep(5)
username=browser.find_element(By.NAME,'username')
password=browser.find_element(By.NAME,'password')
username.send_keys('rabiguzel')
password.send_keys('abc123.')
login=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
login.click()
time.sleep(3)
browser.close()
