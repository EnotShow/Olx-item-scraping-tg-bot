# Функция делает список из наших ссылок, которые хранятся в 'url.txt' для дальнейшего использования
def get_urls_from_file():
    user_urls = []
    try:
        with open('data/url.txt', encoding='UTF-8') as file:
            lines = file.readlines()
            for i in lines:
                user_urls.append(i.strip())

        return user_urls
    except AttributeError('None attributes') as e:
        print(e)
        return Exception(e)


def get_token_from_file():
    with open('data/token.txt', encoding='UTF-8') as file:
        bot_token = file.readlines()
        bot_token = ''.join(bot_token)
        return bot_token
