import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import ssl
import pandas as pd


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


# Find ALL Tables - there are 16 tables
all_tables = soup.findAll('table', {"class": "wikitable sortable"})
print(all_tables)


# Find all table headers in the Last table
all_tables[15].findAll('th')

# grabbing text from Beautiful Soup
for item in all_tables[15].findAll('th'):
    print(item.text, item.next_sibling)

# saving all table header in a list
header = [item.text.rstrip() for item in all_tables[15].findAll('th')]
print(header)
