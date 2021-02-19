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


right_table = soup.find('table', {"class": "wikitable sortable"})
print(right_table)
