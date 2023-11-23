"""Scrapes the school website for changes in the schedule and prints them in the terminal."""


from datetime import date
import requests
from bs4 import BeautifulSoup


url = requests.get("https://zsrovniny.bakalari.cz/next/zmeny.aspx")
if url.status_code == 200:
    print("Status: OK")
else:
    print("Neco se pokazilo.")
soup = BeautifulSoup(url.content, 'html.parser')
tables = soup.find_all('table', {'class': 'datagrid'})
SEARCHED_TEXT = 'Hoppová'
for table in tables:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            if SEARCHED_TEXT in cell.text:
                sub_info = row.get_text()
SUB_INFO = ' '.join(sub_info.split())
print(SUB_INFO)
TODAY_DATE = str(date.today())
with open('src/stored_sub_info.csv', 'a+', encoding="utf-8") as file:
    # contents = file.read()
    # print(contents)
    # if contents.__contains__(today_date) is False:
    file.write('Datum: \n')
    file.write(TODAY_DATE)
    file.write('\n')
    file.write('Zmeny: \n')
    file.write(SUB_INFO)
    file.write('\n\n')
