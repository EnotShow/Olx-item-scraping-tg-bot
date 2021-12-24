def get_token_from_file():
    with open('token.txt', encoding='UTF-8') as file:
        bot_token = file.readlines()
        bot_token = ''.join(bot_token)