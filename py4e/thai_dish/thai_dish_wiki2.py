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
all_tables[0].findAll('th')

# grabbing text from Beautiful Soup
for item in all_tables[0].findAll('th'):
    print(item.text, item.next_sibling)

# saving all table header in a list
header = [item.text.rstrip() for item in all_tables[15].findAll('th')]
print(header)

# Instead of grabbing all individual cells, grab all rows
all_tables[0].findAll('tr')


# Rice dishes (individual)
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []

# all_tables[0] - loop through to create six columns
for row in all_tables[0].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        a1.append(cells[0].find(text=True))
        a2.append(cells[1].find(text=True))
        a3.append(cells[2].find(text=True))
        a4.append(cells[3].find(text=True))
        a5.append(cells[4].find(text=True))
        a6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
a_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
a_d['Thai name'] = a1
a_d['Thai script'] = a2
a_d['English name'] = a3
a_d['Image'] = a4
a_d['Region'] = a5
a_d['Description'] = a6

# turn dict into dataframe
a_d_df_table = pd.DataFrame(a_d)

# print top 5 records of first table
a_d_df_table.head(5)

#

# Noodle dishes (individual)
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[1].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        b1.append(cells[0].find(text=True))
        b2.append(cells[1].find(text=True))
        b3.append(cells[2].find(text=True))
        b4.append(cells[3].find(text=True))
        b5.append(cells[4].find(text=True))
        b6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
b_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
b_d['Thai name'] = b1
b_d['Thai script'] = b2
b_d['English name'] = b3
b_d['Image'] = b4
b_d['Region'] = b5
b_d['Description'] = b6

# turn dict into dataframe
b_d_df_table = pd.DataFrame(b_d)

# print top 5 records of first table
b_d_df_table.head(5)

#

# Miscellaneous (individual)
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[2].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        c1.append(cells[0].find(text=True))
        c2.append(cells[1].find(text=True))
        c3.append(cells[2].find(text=True))
        c4.append(cells[3].find(text=True))
        c5.append(cells[4].find(text=True))
        c6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
c_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
c_d['Thai name'] = c1
c_d['Thai script'] = c2
c_d['English name'] = c3
c_d['Image'] = c4
c_d['Region'] = c5
c_d['Description'] = c6

# turn dict into dataframe
c_d_df_table = pd.DataFrame(c_d)

# print top 5 records of first table
c_d_df_table.head(5)
