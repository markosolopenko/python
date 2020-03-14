from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Open Browser
driver_path = '/home/marko/Downloads/chromedriver_linux64/chromedriver'
browser = webdriver.Chrome(driver_path)
browser.get('https://mail.google.com/mail/u/0/#inbox')
# Enter Email
email = browser.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys("kauchuk1613@gmail.com")
# Click buttom
click = browser.find_element_by_xpath('//*[@id="identifierNext"]/span').click()
time.sleep(10)
# Enter Password
password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("********")
# Click for login
login = browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()