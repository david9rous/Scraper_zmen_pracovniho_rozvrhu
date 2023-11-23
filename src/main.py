"""Scrapes the school website for changes in the schedule and prints them in the terminal."""


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
                print(row.prettify())
                with open('stored_information.csv', 'a') as file:
                    file.write(row)
                    