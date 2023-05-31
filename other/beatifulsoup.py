from bs4 import BeatifulSoup
import requests

# загрузка HTML страницы
url = 'https://www.python.prg/'
response = requests.get(url)
html_code = response.text

# создание обьекта BeatifulSoup для парсинга
soup = BeatifulSoup(html_code, 'html.parser')

# получение заголовка страницы
title = soup.title.text
print(f'Title of the page: {title}')

# получение всех ссылок на странице
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# поиск элемента по id
logo = soup.find(id='python-logo')
print(logo['src'])

# поиск элемента по классу
menu_links = soup.find_all(class_='tier-1')
for link in menu_links:
    print(link.text)

