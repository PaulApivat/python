# coding: utf-8
import xml.etree.ElementTree as ET
data = '''
<person>
   <name>Paul</name>
   <phone type="intl">
   +1 789 345 1234
   </phone>
   <email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Phone:', tree.find('phone').text)
print('Phone Attr:', tree.find('phone').get('type'))
