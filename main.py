from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time

from data_importers import get_urls_from_file


# Функция парсер, которая парсит первый элемент с выдачи OLX
def get_scrap(code_list='No list', index='Null'):
    print('Код лист :', code_list)
    ua = UserAgent

    title_list = []
    href_list = []
    # Если ссылки есть продолжает работу, иначе возвращает ошибку
    try:
        urls = get_urls_from_file()
        for i in urls:
            req = requests.get(
                url=i,
                headers={'user-agent': f'ua.random'}
            ).text
            # Импортируем парсер
            soup = BeautifulSoup(req, 'lxml')
            # Получаем названия и ссылку первого элемент из списка выдачи и добавляем его в лист
            # Если его нет возвращаем "None"
            try:
                get_title = soup.find(class_='lheight22 margintop5').find('a')
            # TODO узнать какой ексепшн
            except Exception:
                title_list.append('None')
            else:
                title_list.append(get_title.text.strip())
            get_href = soup.find(class_='space rel').find_all('a')
            for i in get_href:
                href_list.append(i.get('href'))
            print('get_scrap titles ', title_list)
        # Если не получаем список на вход, возвращает список названий
        if code_list == 'No list':
            print('Возвращает лист', title_list)
            return title_list
        # Если получает список на вход(мы отправляем только списки содержащие единицы)
        elif 1 in code_list:
            for i in code_list:
                if i == 1:
                    current_titles[index] = title_list[index]
                    to_sent = f'{title_list[index]} {href_list[index]}'
                    index += 1
                    print('Данные для отправки', to_sent)
                    return to_sent

    except AttributeError('None attributes') as e:
        return Exception(e)


# Переменная которая подготавливает данные которые нужно отправить пользователю
def prepare_to_sent():
    func_current_title = current_titles
    answer = []
    index = 0
    for i in get_scrap():
        answer.append(0)
        print('Prepare to sent answer append 0')
    current_req = get_scrap
    for i in func_current_title:
        for j in current_req():
            if i[index] == j[index]:
                index += 1
                time.sleep(1)
                continue
            elif i[index] != j[index]:
                answer[index] = 1
                print(f'{answer} ответ от prepare to sent {index}')
                return answer, index


# Переменная которая получает данные нужные для отправки и отправляет их боту
def sent_to_user():
    change_finder, index = prepare_to_sent()
    to_sent = get_scrap(code_list=change_finder, index=index)
    return to_sent


# Функция останавливает отправку парсов пользователю
def stop_scraping():
    exit(sent_to_user())


# Конец функций

# Глобальная переменная которая при запуске получает список значений, затем лишь изменяет их
current_titles = get_scrap()
print('Current titles задана', current_titles)

