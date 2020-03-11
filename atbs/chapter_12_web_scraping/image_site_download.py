from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import time
import os
# browser = webdriver.Chrome('/home/marko/Downloads/chromedriver_linux64/chromedriver')
# browser.get('https://identity.flickr.com/login?redir=https%3A%2F%2Fwww.flickr.com%2F')
# time.sleep(10)
# # put mail
# mail = browser.find_element_by_xpath('//*[@id="login-email"]').send_keys('kauchuk1613@gmail.com')
# # continue
# cont = browser.find_element_by_xpath('//*[@id="login-form"]/button').click()
# time.sleep(10)
# # put password
# password = browser.find_element_by_xpath('//*[@id="login-password"]').send_keys('vfhrecz199713')
# #log in
# log = browser.find_element_by_xpath('//*[@id="login-form"]/button').click()
# find certain photos
# time.sleep(10)
# find = browser.find_element_by_xpath('//*[@id="search-field"]').send_keys('Christian Benetel')
# submit
# submit = browser.find_element_by_link_text('Dimitry Roulland')
# try:
#     find_photos = browser.find_element_by_id('#yui_3_16_0_1_1583938239630_657')
#     print('Found <%s> element with that class name!' % (find_photos.tag_name))
# except:
#     print("Was not able to find an element with that name.")