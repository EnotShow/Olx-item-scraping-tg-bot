def get_url_from_file():
    with open('url.txt', encoding='UTF-8') as file:
        user_url = file.readlines()
        user_url = ''.join(user_url)
        return user_url

print(get_url_from_file())
