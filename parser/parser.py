from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=10).install()))
url = 'https://animevost.org/tip/tv/2959-kaminaki-sekai-no-kamisama-katsudou.html'
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
timer = soup.body
swag = timer.table('div', id='nexttime')
for t in swag:
    h = t.getText()
    pass
    print(h)
