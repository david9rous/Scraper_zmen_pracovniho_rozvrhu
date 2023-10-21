import requests
from bs4 import BeautifulSoup


webpage = requests.get("https://zsrovniny.bakalari.cz/next/zmeny.aspx")
if webpage.status_code == 200:
    print("Status: OK")
else:
    print("Neco se pokazilo.")
table = BeautifulSoup(webpage.content, 'html.parser')
schedule = table.find_all('table', {'class': 'datagrid'})
text = 'Rouš'
for i in schedule:
    element = i.find(text)
