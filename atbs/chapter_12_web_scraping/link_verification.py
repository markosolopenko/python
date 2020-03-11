from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import time
url = 'https://automatetheboringstuff.com/2e/chapter12/'

# Downloads the URL
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')
counter = 0

# Loop through all links found on the page.
for link in soup.select('a[href]'):

    l = link.get('href')

    # Check for any errors at URL.
    try:
        requests.get(l).raise_for_status()

    # Print any problematic links.
    except Exception as exc:
        print(f'There was a problem at {l} ~ {exc}.')
    counter += 1

# Give feedback once script has been run.
print(f'All done. We looked at {counter} links in total.')