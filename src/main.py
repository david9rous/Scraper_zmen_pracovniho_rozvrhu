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
sub_info = sub_info.replace('\n', ' ')
print(sub_info)
today_date = str(date.today())
with open('stored_information.csv', 'a') as file:
    file.write('Datum: \n')
    file.write(today_date)
    file.write('\n')
    file.write('Zmeny: \n')
    file.write(sub_info)
    file.write('\n\n')
