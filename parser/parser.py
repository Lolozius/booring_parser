import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BoringParser:
    """
    Пока нет идей куда применить в будущем не забыть чё нить своять
    (Внешнее приложение)
    """
    def __init__(self, link):
        self.link = link

    def parser(self):
        """
        Парсер подцепляет таймер с карточки странницы animevost
        """
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=10).install()))
        driver.get(self.link)
        try:
            requests.head('https://animevost.org/')
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            timer = soup.body.table('div', id='nexttime')
            for t in timer:
                h = t.getText()
                print(h)
        except requests.ConnectionError:
            print('Я днс не чувствую..')


time_value = BoringParser(input())
time_value.parser()
