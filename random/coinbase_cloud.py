import http.client
import json

#conn = http.client.HTTPSConnection("www.api.coinbasecloud.net/eth2/v1/validators")
conn = http.client.HTTPSConnection("www.coinbase.com")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'apikey': 'apikey'
}
conn.request("GET", "/validators?limit=10&page=1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))