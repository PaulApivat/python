from dateutil import rrule
from datetime import datetime
import requests

# Code Gist: https://gist.github.com/kikura3/b3847100817764fadc63e5c5cae8275d
# context: Merge Impact - Energy Consumption by Kiruba
# https://www.twigblock.com/projects/eth-merge-analysis/t/em-energy-change

# ethereum merge happens Sept 15th 
start = '20220101'
end = '20220926'

DIGITCONOMIST_URL = 'https://digiconomist.net/wp-json/mo/v1/ethereum/stats/'

result = []

for dt in rrule.rrule(rrule.DAILY,
                      dtstart=datetime.strptime(start, '%Y%m%d'), 
                      until=datetime.strptime(end, '%Y%m%d')):
    
    dt_s = dt.strftime('%Y%m%d')
    url = DIGITCONOMIST_URL + dt_s

    response = requests.get(url)
    output = response.json()
    if len(output) != 0:
        data = output[0]
        data['date'] = dt_s
        result.append(data)
    else:
        print('data missing for ', dt_s)

# print(result)