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
subs_table = soup.find('th', string='Změny v rozvrzích učitelů')
table = subs_table.find_parent('table')
SEARCHED_TEXT = 'Kadlecová'
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        if SEARCHED_TEXT in cell.text:
            sub_info = row

# sub_info_list = []
# for line in sub_info:
#     sub_info_list.append(line)
# sub_info = ' '.join(sub_info.split())
# sub_info = re.split(f'({SEARCHED_TEXT})', sub_info)
# if sub_info[0] == '':
    # sub_info = sub_info[1:]
print(sub_info)
