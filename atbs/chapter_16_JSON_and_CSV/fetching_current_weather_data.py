APPID = 'e702f4bf6130a9c2b8963294ddfd1c9f'


import sys
import json
import requests
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()



location = ''.join(sys.argv[1:])
url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % ('ISO 3166-2:UA', APPID)
response = requests.get(url)
response.raise_for_status()
print(response)
#weatherData = json.loads('response.txt')

#w = weatherData['list']

