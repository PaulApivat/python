# coding: utf-8
import json
import requests

r = requests.get('https://api.crypto51.app/coins.json')

print(r.json())
type(r.json())
dct = dict()
dct = r.json()
