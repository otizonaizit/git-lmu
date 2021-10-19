def get_credentials():
    username = input('Type username: ')
    password = input('Type password: ')
    return username, password

username, password = get_credentials()
print(username, password)

