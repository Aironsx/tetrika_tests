import os

import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('url')

animals = {}
statistics = {}


def get_data(url):
    """
    Get page for parsing
    :param url:
    :return:
    """
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    links = soup.find('div', id='mw-pages').find_all('a')
    parse_data(links)


def parse_data(data):
    """
    Data parse and writing in dict
    :param data:
    :return:
    """
    flag = False
    for i in data:
        if i.text == 'Следующая страница':
            next_url = 'https://ru.wikipedia.org/' + i.get('href')
            flag = True
            continue
        if i.text != 'Предыдущая страница':
            animals[i.text[0]] = animals.get(i.text[0], [])
            animals[i.text[0]].append(i.text)
    if flag:
        get_data(next_url)


def get_statistic():
    """
    Collecting statistic
    :return:
    """
    for key in animals:
        statistics[key] = statistics.get(key, [])
        statistics[key].append(len(animals[key]))
    write_data(statistics, 'statistics')


def write_data(data, name):
    """
    Write data in json
    :param data:
    :param name:
    :return:
    """
    with open(f'{name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_data(url)
    write_data(animals, 'animals')
    get_statistic()
    with open('statistics.json') as file:
        json_data = json.load(file)
        print(json_data)
