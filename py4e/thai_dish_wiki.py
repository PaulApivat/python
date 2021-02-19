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
