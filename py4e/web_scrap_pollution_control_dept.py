# coding: utf-8
from urllib.request import Request, urlopen
req = Request('http://aqmthai.com/web/home.php', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
webpage
type(webpage)
list(webpage, .iterbytes())
len(webpage)
webpage[100]
webpage[99]
webpage[0]
webpage
