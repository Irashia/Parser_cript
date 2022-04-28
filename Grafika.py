import sys
import requests
import json
import lxml

from PyQt5 import uic  # Импортируем uic
#from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUIui.ui', self)  # Загружаем дизайн
        self.setFixedSize(620, 600)
        url = 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'
        list_name, slovar = pars(url)
        self.list_name = list_name
        self.slovar = slovar

        #self.slovar = slovar
        #self.list_name = list_name

        self.Spisok1.addItems(list_name)#Вставить сюда список имен
        self.Spisok2.addItems(list_name[::-1])
        self.Spisok1.setEditable(True)
        self.Spisok2.setEditable(True)

        self.value_1.setText('0')#Колво монет
        self.value_2.setText('0')#Колво монет

        self.price_1.setText('0')
        self.price_2.setText('0')
        #print(self.value_1.text())#Вывод значения value

        self.Complete.setPlaceholderText('Я получу')

        self.pushButton.clicked.connect(self.converter)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def converter(self):
        #c = CurrencyConverter()
        currency_1 = self.Spisok1.currentText()#По списку имен найти ценность
        currency_2 = self.Spisok2.currentText()
        if currency_2 not in self.list_name and currency_1 not in self.list_name:
            return

        value_1 = self.value_1.text()
        value_2 = self.value_2.text()
        try:
            value_1, value_2 = int(value_1), int(value_2)

        except:
            print('error')
            return

        print('ok')
        output_1, output_2 = self.slovar[currency_1][1], self.slovar[currency_2][1]
        self.price_1.setText(str(output_1))
        self.price_2.setText(str(output_2))

        print(type(output_1))
        value_1 *= output_1
        value_2 *= output_2
        if output_2 == 0: return
        print(str(value_1 / value_2))
        self.Complete.setText(str(value_1 / value_2))


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

    '''if site.status_code == 200:
        return site
    else:
        return None'''

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

if __name__ == '__main__':
    '''url = 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'
    list_name, slovar = pars(url)
    print(list_name)'''
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())



