# coding: utf-8
class PartyAnimal:
    lst = [0, 99, 'fish', 'egg']
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
        
s = PartyAnimal("Sally")
s.party()
s.x
s.lst
type(s.lst)
s.lst.append('burger')
s.lst
j = FootballFan("Jim")
j.party()
j.touchdown()
j.lst
j.lst[2]
for item in j.lst:
    print(item)
    
