# coding: utf-8
import xml.etree.ElementTree as ET
input = '''
<stuff>
   <users>
      <user x="2">
          <id>001</id>
          <name>Paul</name>
      </user>
      <user x="7">
          <id>009</id>
          <name>Marvin</name>
      </user>
   </users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
lst
type(lst[0])
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
    
