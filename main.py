import requests
import json
import lxml
import sys
'''from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow'''

#from bs4 import BeautifulSoup



#
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}




def zapros(site, url):#Получение сайта
    try:
        print('Получение HTML')
        site= requests.get(url, headers=headers)#, timeout=5)
        print('Complete')
        return(site.text)


    except requests.ConnectionError as e:
        print("Ошибка подключения к интернету.")
        print(str(e))

    except requests.Timeout as e:
        print("Время ожидания истекло.")
        print(str(e))

    except requests.RequestException as e:
        print("Возникла непредвиденная ошибка!")
        print(str(e))

    except KeyboardInterrupt:
        print("Кто-то закрыл принудительно программу.")


def get_url(url):
    site = None
    #url = 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'
    while site == None:
        site = zapros(site, url)
    return site

def pars(url):
    dic = json.loads(get_url(url))
    dic = dic['data']
    slovar = dict()

    list_name = list()
    for i in range(len(dic)):
        # print(dic[i])
        slovar[dic[i]['name']] = (dic[i]['rank'], dic[i]['price'])
        list_name.append(dic[i]['name'])
    return list_name, slovar


url = 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'
list_name, slovar = pars(url)
print(list_name)

