from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import request
import bs4
import random
import time

browser = webdriver.Chrome('/home/marko/Downloads/chromedriver_linux64/chromedriver')
browser.get('https://play2048.co/')

# Start the game
start = browser.find_element_by_xpath('/html/body/div[3]/div[2]/a').click()

moves = [Keys.LEFT, Keys.DOWN, Keys.RIGHT, Keys.UP]
while True:
    time.sleep(1)
    browser.find_element_by_css_selector('body').send_keys(random.choice(moves))