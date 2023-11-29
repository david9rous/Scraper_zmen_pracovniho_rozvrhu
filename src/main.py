"""Scrapes the school website for changes in the schedule and prints them in the terminal."""


from datetime import date
import requests
from bs4 import BeautifulSoup


response = requests.get("https://zsrovniny.bakalari.cz/next/zmeny.aspx")
if response.status_code == 200:
    print("Status: OK")
else:
    print("Neco se pokazilo.")
soup = BeautifulSoup(response.content, 'html.parser')
subs_table = soup.find('th', string='Změny v rozvrzích učitelů')
table = subs_table.find_parent('table')
SEARCHED_TEXT = 'Rouš'
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        if SEARCHED_TEXT in cell.text:
            sub_info = row
        else:
            sub_info = 'Beze zmen.'
sub_info_list = []
if sub_info != 'Beze zmen.':
    for data in sub_info.find_all('tr'):
        sub_info_list.append(data.get_text().split())
else:
    sub_info_list.append(sub_info)
for i in sub_info_list:
    print(i)
TODAY_DATE = str(date.today())
with open('../data/stored_sub_info.txt', 'a+', encoding="utf-8") as file:
    file.seek(0)
    contents = file.read()
    if TODAY_DATE not in contents:
        file.write('Datum: \n')
        file.write(TODAY_DATE)
        file.write('\n')
        file.write('Zmeny: \n')
        for i in sub_info_list:
            file.write(str(i))
            file.write('\n')
        file.write('\n')
