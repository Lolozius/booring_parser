from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from requests import Session
from bs4 import BeautifulSoup


url = 'https://animevost.org/tip/tv/2959-kaminaki-sekai-no-kamisama-katsudou.html'
ses = Session()
response = ses.get(url)
with open('test.html', 'w') as r:
    r.write(response.text)
