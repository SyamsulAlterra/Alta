class Animals():
    def __init__(self, name='Binatang'):
        self._class='parent of all animals'
        self._name=name
        self._food=None
        self._teeth=None
        self._identity=''

    def constructIdentity(self):
        self._identity='Hi I\'m '+ self._class+'. My name is '+self._name
        return self._identity

    def showIdentity(self):
        print(self.constructIdentity())

class Herbivor(Animals):
    def __init__(self, name):
        super().__init__(name)
        self._food='tumbuhan'
        self._class='Herbivor'
        self._teeth='tumpul'

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. My food is '+self._food+' and I have '+self._teeth+' teeth'
        return self._identity

class Carnivor(Animals):
    def __init__(self, name):
        super().__init__(name)
        self._food='daging'
        self._class='Carnivor'
        self._teeth='tajam'

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. My food is '+self._food+' and I have '+self._teeth+' teeth'
        return self._identity

class Omnivor(Animals):
    def __init__(self, name):
        super().__init__(name)
        self._food='semua'
        self._class='Omnivor'
        self._teeth='tajam dan tumpul'

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. My food is '+self._food+' and I have '+self._teeth+' teeth'
        return self._identity
        
class Horse(Herbivor):
    def __init__(self, name):
        super().__init__(name)

class Goat(Herbivor):
    def __init__(self, name):
        super().__init__(name)

class Tiger(Carnivor):
    def __init__(self, name):
        super().__init__(name)

class Lion(Carnivor):
    def __init__(self, name):
        super().__init__(name)

class Chicken(Omnivor):
    def __init__(self, name):
        super().__init__(name)

class Duck(Omnivor):
    def __init__(self, name):
        super().__init__(name)

animal=Animals()
animal.showIdentity()

kuda=Horse('kuda')
kambing=Goat('kambing')
macan=Tiger('macan')
singa=Lion('singa')
ayam=Chicken('ayam')
bebek=Duck('bebek')
kuda.showIdentity()
kambing.showIdentity()
macan.showIdentity()
singa.showIdentity()
ayam.showIdentity()
bebek.showIdentity()



    