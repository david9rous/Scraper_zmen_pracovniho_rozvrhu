"""Scrapes the school website for changes in the schedule and prints them in the terminal."""


from datetime import date
import re
import requests
from bs4 import BeautifulSoup


url = requests.get("https://zsrovniny.bakalari.cz/next/zmeny.aspx")
if url.status_code == 200:
    print("Status: OK")
else:
    print("Neco se pokazilo.")
soup = BeautifulSoup(url.content, 'html.parser')
tables = soup.find_all('table', {'class': 'datagrid'})
SEARCHED_TEXT = 'Rouš'
for table in tables:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            if SEARCHED_TEXT in cell.text:
                sub_info = row.get_text()
            else:
                sub_info = 'Neni zadna zmena.'
sub_info = ' '.join(sub_info.split())
sub_info = re.split(f'({SEARCHED_TEXT})', sub_info)
print(sub_info)
TODAY_DATE = str(date.today())
with open('data/stored_sub_info.txt', 'a+', encoding="utf-8") as file:
    file.seek(0)
    contents = file.read()
    if TODAY_DATE not in contents:
        file.write('Datum: \n')
        file.write(TODAY_DATE)
        file.write('\n')
        file.write('Zmeny: \n')
        for i in sub_info:
            file.write(str(i))
        file.write('\n\n')
