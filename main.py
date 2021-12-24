from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time


# Функция делает список из наших ссылок, которые хранятся в 'url.txt' для дальнейшего использования
def get_urls_from_file():
    user_urls = []
    try:
        with open('url.txt', encoding='UTF-8') as file:
            lines = file.readlines()
            for i in lines:
                user_urls.append(i.strip())

        return user_urls
    except AttributeError('None attributes') as e:
        print(e)
        return Exception(e)


# Переменная которая получает данные нужные для отправки и отправляет их боту(TODO переименовать)
def aggregator():
    # product_title = get_item(0)
    # while True:
    #     if get_item(0) == product_title:
    #         time.sleep(10)
    #     elif get_item(1):
    #         result = get_item(1)
    #         return result
    #     else:
    #         return 'Обработчик вернул ошибку !!!'
    change_finder = sent_to_user()
    to_sent = get_item(change_finder)
    return to_sent


# Функция парсер, которая парсит первый элемент с выдачи OLX
def get_item(code_list=[False]):
    print(code_list)
    ua = UserAgent
    # Если ссылки есть продолжает работу, иначе возвращает ошибку
    try:
        urls = get_urls_from_file()
        title_list = []
        href_list = []
        for i in urls:
            req = requests.get(
                url=i,
                headers={'user-agent': f'ua.random'}
            ).text
            # Импортируем парсер
            soup = BeautifulSoup(req, 'lxml')
            # Получаем названия и ссылку первого элемент из списка выдачи
            get_href = soup.find(class_='space rel').find_all('a')
            get_title = soup.find(class_='lheight22 margintop5').find('a')
            # Получаем список из названий и ссылок
            title_list.append(get_title.text.strip())
            for i in get_href:
                href_list.append(i.get('href'))
            # Код который использовался раньше
            # if code == 1:
            #     for i in get_href:
            #         return f'{get_title.text.strip()} {i.get("href")}'
            # elif code == 0:
            #     return get_title.text.strip()
        # Если не получаем список на вход, возвращает список названий
        if code_list == [False]:
            return title_list
        # Если получает список на вход(мы отправляем только списки содержащие единицы)
        elif 1 in code_list:
            index = 0
            for i in code_list:
                if i == 1:
                    current_titles[index] = title_list[index]
                    to_sent = f'{title_list[index]} {href_list[index]}'
                    print(to_sent)
                    return to_sent

    except AttributeError('None attributes') as e:
        return Exception(e)


# Глобальная переменная которая при запуске получает список значений, затем лишь изменяет их
current_titles = get_item()
print(current_titles)


# Переменная которая подготавливает данные которые нужно отправить пользователю (TODO переименовать)
def sent_to_user():
    current_titlesF = current_titles
    answer = []
    for i in get_item():
        answer.append(0)
    while True:
        index = 0
        current_req = get_item()
        for i in current_titlesF:
            for j in current_req:
                if i[index] == j[index]:
                    index += 1
                    time.sleep(1)
                    continue
                elif i[index] != j[index]:
                    answer[index] = 1
                    index += 1
                    return answer
