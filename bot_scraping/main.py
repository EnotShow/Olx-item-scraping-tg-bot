from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time


# def get_url_from_file():
#     with open('url.txt', encoding='UTF-8') as file:
#         user_url = file.readlines()
#         user_url = ''.join(user_url)


def get_item(code):
    url = 'https://www.olx.ua/otdam-darom/?search%5Bfilter_float_price%3Afrom%5D=free&search%5Bprivate_business%5D=private&search%5Border%5D=created_at%3Adesc'
    ua = UserAgent
    req = requests.get(
        url=url,
        headers={'user-agent': f'ua.random'}
    ).text

    # with open('result.html', 'w', encoding='UTF-8') as file:
    #     file.write(req.text)

    #  with open('result.html', encoding='UTF-8') as file:
    #      scr = file.read()

    soup = BeautifulSoup(req, 'lxml')

    get_href = soup.find(class_='space rel').find_all('a')
    get_title = soup.find(class_='lheight22 margintop5').find('a')

    if code == 1:
        for i in get_href:
            return f'{get_title.text.strip()} {i.get("href")}'
    elif code == 0:
        return get_title.text.strip()


def send_to_user():
    product_title = get_item(0)
    while True:
        if get_item(0) == product_title:
            time.sleep(10)
        elif get_item(1):
            result = get_item(1)
            return result
        else:
            return 'Обработчик вернул ошибку !!!'
