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

#

# Curries (Shared Dishes)
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[3].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        d1.append(cells[0].find(text=True))
        d2.append(cells[1].find(text=True))
        d3.append(cells[2].find(text=True))
        d4.append(cells[3].find(text=True))
        d5.append(cells[4].find(text=True))
        d6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
d_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
d_d['Thai name'] = d1
d_d['Thai script'] = d2
d_d['English name'] = d3
d_d['Image'] = d4
d_d['Region'] = d5
d_d['Description'] = d6

# turn dict into dataframe
d_d_df_table = pd.DataFrame(d_d)

# print top 5 records of first table
d_d_df_table.head(5)

#

# Soups (Shared Dishes)
e1 = []
e2 = []
e3 = []
e4 = []
e5 = []
e6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[4].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        e1.append(cells[0].find(text=True))
        e2.append(cells[1].find(text=True))
        e3.append(cells[2].find(text=True))
        e4.append(cells[3].find(text=True))
        e5.append(cells[4].find(text=True))
        e6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
e_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
e_d['Thai name'] = e1
e_d['Thai script'] = e2
e_d['English name'] = e3
e_d['Image'] = e4
e_d['Region'] = e5
e_d['Description'] = e6

# turn dict into dataframe
e_d_df_table = pd.DataFrame(e_d)

# print top 5 records of first table
e_d_df_table.head(5)

#

# Saladf (Shared Dishes)
f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[5].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        f1.append(cells[0].find(text=True))
        f2.append(cells[1].find(text=True))
        f3.append(cells[2].find(text=True))
        f4.append(cells[3].find(text=True))
        f5.append(cells[4].find(text=True))
        f6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
f_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
f_d['Thai name'] = f1
f_d['Thai script'] = f2
f_d['English name'] = f3
f_d['Image'] = f4
f_d['Region'] = f5
f_d['Description'] = f6

# turn dict into dataframe
f_d_df_table = pd.DataFrame(f_d)

# print top 5 records of first table
f_d_df_table.head(5)
