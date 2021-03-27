# coding: utf-8
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)


class PartyMonster:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


q = PartyMonster('Quincy')
m = PartyMonster('Miya')
q.party()
m.party()
q.party()
