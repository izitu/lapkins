# скачиваем каталог собак - смотрим параметры
# https://lapkins.ru/dog/
import requests, bs4, openpyxl

prefix = 'https://lapkins.ru'
base_url = 'https://lapkins.ru/dog/'
headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
s0 = session.get(base_url, headers=headers)

b = bs4.BeautifulSoup(s0.text, "html.parser")
dogs_urls = b.select('.poroda-element')

wb = openpyxl.Workbook()

# добавляем новый лист
wb.create_sheet(title='Первый лист', index=0)
# получаем лист, с которым будем работать
sheet = wb['Первый лист']
# заголовок
cell = sheet.cell(row=1, column=1)
cell.value = 'Порода'
cell = sheet.cell(row=1, column=2)
cell.value = 'URL'
cell = sheet.cell(row=1, column=3)
cell.value = 'Агрессивность'
cell = sheet.cell(row=1, column=4)
cell.value = 'Активность'
cell = sheet.cell(row=1, column=5)
cell.value = 'Дрессировка'
cell = sheet.cell(row=1, column=6)
cell.value = 'Линька'
cell = sheet.cell(row=1, column=7)
cell.value = 'Потребность в уходе'
cell = sheet.cell(row=1, column=8)
cell.value = 'Дружелюбность'
cell = sheet.cell(row=1, column=9)
cell.value = 'Здоровье'
cell = sheet.cell(row=1, column=10)
cell.value = 'Стоимость содержания'
cell = sheet.cell(row=1, column=11)
cell.value = 'Отношение к одиночеству'
cell = sheet.cell(row=1, column=12)
cell.value = 'Интеллект'
cell = sheet.cell(row=1, column=13)
cell.value = 'Шум'
cell = sheet.cell(row=1, column=14)
cell.value = 'Охранные качества'

r = 2


for item in dogs_urls:
    name = item.text.strip()
    url = prefix + item.get('href')
    print(name, url)

    s = session.get(url, headers=headers)
    bs = bs4.BeautifulSoup(s.text, "html.parser")
    info_blocks = bs.select('.spo')

    cell = sheet.cell(row=r, column=1)
    cell.value = name
    cell = sheet.cell(row=r, column=2)
    cell.value = url
    k = 3
    #print(info_blocks)
    for kachva in info_blocks:
        print(kachva.select('.s-title')[0].text)
        print(kachva.select('.s-text')[0].text)
        posr = kachva.select('.s-text')[0].text.find('/')
        raiting = kachva.select('.s-text')[0].text[posr-1:posr]
        cell = sheet.cell(row=r, column=k)
        cell.value = raiting


        k = k + 1

    r = r + 1
    #print(bs.select('.spo')[1].select('.s-title')[0].text)
    #print(bs.select('.spo')[1].select('.s-text')[0].text)

wb.save('dogs.xlsx')

#print(dogs_urls)
