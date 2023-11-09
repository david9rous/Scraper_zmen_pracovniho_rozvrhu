import requests
from bs4 import BeautifulSoup


url = requests.get("https://zsrovniny.bakalari.cz/next/zmeny.aspx")
if url.status_code == 200:
    print("Status: OK")
else:
    print("Neco se pokazilo.")
soup = BeautifulSoup(url.content, 'html.parser')
tables = soup.find_all('table', {'class': 'datagrid'})
text = 'ABD'
for table in tables:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            if text in cell.text():
                print('Nalezeno')
