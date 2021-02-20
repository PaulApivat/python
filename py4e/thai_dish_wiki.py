# coding: utf-8
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import ssl


url = "https://en.wikipedia.org/wiki/List_of_Thai_dishes"
s = requests.Session()
response = s.get(url, timeout=10)
response


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
soup.title.string

# This is only the first table
right_table = soup.find('table', {"class": "wikitable sortable"})
print(right_table)

# Too many non-Thai cuisines
right_div = soup.find('div', {"class": "mw-content-ltr"})

right_div2 = soup.find('div', {"class": "mw-parser-output"})


# Find ALL Tables - there are 16 tables
all_table = soup.findAll('table', {"class": "wikitable sortable"})

# First td of last table
all_table[15].find('td')
# Find all td of last table
all_table[15].findAll('td')

len(all_table[15].findAll('td'))  # 102

all_table[15].findAll('td')[0]  # <td>Cha dam yen </td>

# Find all table headers in the Last table
all_table[15].findAll('th')

# grabbing text from Beautiful Soup
for item in all_table[15].findAll('th'):
    print(item.text, item.next_sibling)

# saving all table header in a list
header = [item.text.rstrip() for item in all_table[15].findAll('th')]

# grab all cells
for item in all_table[15].findAll('td'):
    print(item.text, item.next_sibling)

table_body = [item.text.rstrip() for item in all_table[15].findAll('td')]

# Instead of grabbing all individual cells, grab all rows
all_table[15].findAll('tr')

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []

# loop through to create six columns
for row in all_table[15].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        c1.append(cells[0].find(text=True))
        c2.append(cells[1].find(text=True))
        c3.append(cells[2].find(text=True))
        c4.append(cells[3].find(text=True))
        c5.append(cells[4].find(text=True))
        c6.append(cells[5].find(text=True))


# append dictionary with corresponding data list
d['Thai name'] = c1
d['Thai script'] = c2
d['English name'] = c3
d['Image'] = c4
d['Region'] = c5
d['Description'] = c6
