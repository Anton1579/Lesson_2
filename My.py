
# 1. Посмотреть документацию к API GitHub, разобраться как вывести
# список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import json
import urllib
import requests
import webbrowser
from pprint import pprint


username = "Anton1579"
url = f"https://api.github.com/users/{username}"
user_date = requests.get(url).json()
pprint(user_date)

with open('api_dz_1.json', 'w') as f:
    f.write(json.dumps(user_date ))

with open('api_dz_1.json') as f:
    print(f.read())

# ------------------------------------
# 2. Изучить список открытых API. Найти среди них любое,
# требующее авторизацию (любого типа). Выполнить запросы к нему,
# пройдя авторизацию. Ответ сервера записать в файл.

#сайт с API, выдает все данные ссайта или владльцы IP http://api.ipstack.com/


given_user = input("Ведите название 'IP' или название сайта: ")
access_key = '00a32023e4d305339fde455f558ca5a9'
service = 'http://api.ipstack.com/'
# headers = {'Usser-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

response = (f'{service}{given_user}?access_key={access_key}')
url = str(response)
print(url)
webbrowser.open(url, new=0, autoraise=True)

sock = urllib.request.urlopen(url)
htmlSource = sock.read()
sock.close()
pprint(htmlSource)
