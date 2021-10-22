import requests
from bs4 import BeautifulSoup
import os

if os.path.isfile('last.txt'):
    os.remove('last.txt')

phone = input("[*] Номер телефона : ")
service = "http://phoneradar.ru/phone/"
link = service + phone

         
def get_html(link, params=None):
    r = requests.get(link, params=params)
    return r 
def parse():
    html = get_html(link)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('''Ошибка!
Вы ввели некорректный номер телефона!
Убедитесь, что введённый Вами номер, не содержит лишних символов.''')
        stop()
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('tbody')
    file = open("trash.tr", "w")
    file.write(result.text)
    file.close()
    with open("trash.tr") as a:
        with open("last.txt", 'a') as out:
            for line in filter(lambda x: x != '\n', a):
                out.write(line)
    os.remove('trash.tr')           
    print("Номер:", phone)
    print("\n"+"Результат:"+"\n")
    file1 = open("last.txt", "r")
    while True:
        line = file1.readline()
        if not line:
            break
        print(line.strip())
    file1.close
    print('''
Последний результат сохраняется в файле: last.txt
Он исчезнет при следующем запуске программы.''')
parse()