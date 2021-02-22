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

# Salad (Shared Dishes)
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

#

# Fried and Stir-Fried Dishes (Shared Dishes)
g1 = []
g2 = []
g3 = []
g4 = []
g5 = []
g6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[6].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        g1.append(cells[0].find(text=True))
        g2.append(cells[1].find(text=True))
        g3.append(cells[2].find(text=True))
        g4.append(cells[3].find(text=True))
        g5.append(cells[4].find(text=True))
        g6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
g_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
g_d['Thai name'] = g1
g_d['Thai script'] = g2
g_d['English name'] = g3
g_d['Image'] = g4
g_d['Region'] = g5
g_d['Description'] = g6

# turn dict into dataframe
g_d_df_table = pd.DataFrame(g_d)

# print top 5 records of first table
g_d_df_table.head(5)

#

# Deep-Fried Dishes (Shared Dishes)
h1 = []
h2 = []
h3 = []
h4 = []
h5 = []
h6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[7].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        h1.append(cells[0].find(text=True))
        h2.append(cells[1].find(text=True))
        h3.append(cells[2].find(text=True))
        h4.append(cells[3].find(text=True))
        h5.append(cells[4].find(text=True))
        h6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
h_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
h_d['Thai name'] = h1
h_d['Thai script'] = h2
h_d['English name'] = h3
h_d['Image'] = h4
h_d['Region'] = h5
h_d['Description'] = h6

# turn dict into dataframe
h_d_df_table = pd.DataFrame(h_d)

# print top 5 records of first table
h_d_df_table.head(5)

#

# Grilled Dishes (Shared Dishes)
i1 = []
i2 = []
i3 = []
i4 = []
i5 = []
i6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[8].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        i1.append(cells[0].find(text=True))
        i2.append(cells[1].find(text=True))
        i3.append(cells[2].find(text=True))
        i4.append(cells[3].find(text=True))
        i5.append(cells[4].find(text=True))
        i6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
i_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
i_d['Thai name'] = i1
i_d['Thai script'] = i2
i_d['English name'] = i3
i_d['Image'] = i4
i_d['Region'] = i5
i_d['Description'] = i6

# turn dict into dataframe
i_d_df_table = pd.DataFrame(i_d)

# print top 5 records of first table
i_d_df_table.head(5)

#

# Steamed or Blanched Dishes (Shared Dishes)
j1 = []
j2 = []
j3 = []
j4 = []
j5 = []
j6 = []

# all_tables[1] - loop through to create six columns
for row in all_tables[9].findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        j1.append(cells[0].find(text=True))
        j2.append(cells[1].find(text=True))
        j3.append(cells[2].find(text=True))
        j4.append(cells[3].find(text=True))
        j5.append(cells[4].find(text=True))
        j6.append(cells[5].find(text=True).rstrip())  # ignore italics

# create dictionary
j_d = dict([(x, 0) for x in header])

# append dictionary with corresponding data list
j_d['Thai name'] = j1
j_d['Thai script'] = j2
j_d['English name'] = j3
j_d['Image'] = j4
j_d['Region'] = j5
j_d['Description'] = j6

# turn dict into dataframe
j_d_df_table = pd.DataFrame(j_d)

# print top 5 records of first table
j_d_df_table.head(5)
