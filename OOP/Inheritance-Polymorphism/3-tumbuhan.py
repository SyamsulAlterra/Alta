class Plant():
    def __init__(self):
        self._class='parent of all plants'
        self._name='no name'
        self._akar=None
        self._batang=None
        self._daun=None
        self._identity=''

    def constructIdentity(self):
        self._identity='Hi, I\'m '+self._class+'. My name is '+self._name
        return self._identity

    def showIdentity(self):
        print(self.constructIdentity())

class Monocotyle(Plant):
    def __init__(self):
        super().__init__()
        self._class='Monocotyle'
        self._akar='serabut'
        self._batang='no cambium'
        self._daun='tidak menyirip'

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. I have '+self._akar+' root, '+self._batang+' stem, and '+self._daun+' leaf'
        return self._identity

class Dicotyle(Plant):
    def __init__(self):
        super().__init__()
        self._class='Dicotyle'
        self._akar='tunggang'
        self._batang='cambium'
        self._daun='menyirip'

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. I have '+self._akar+' root, '+self._batang+' stem, and '+self._daun+' leaf'
        return self._identity

class Vegetative(Monocotyle):
    def __init__(self,name):
        super().__init__()
        self._class='Vegetative'
        self._reproduction='spora'
        self._name=name

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. I reproduce with '+self._reproduction
        return self._identity

class Generative(Monocotyle):
    def __init__(self, name):
        super().__init__()
        self._class='Generative'
        self._reproduction='flower'
        self._name=name

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. I reproduce with '+self._reproduction
        return self._identity

class FlowerPlant(Dicotyle):
    def __init__(self,name):
        super().__init__()
        self._class='Flower Plant'
        self._accessories='flower'
        self._name=name

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. I have '+self._accessories+' as my accessories'
        return self._identity

class FruitPlant(Dicotyle):
    def __init__(self, name):
        super().__init__()
        self._class='Fruit Plant'
        self._accessories='fruit'
        self._name=name

    def constructIdentity(self):
        self._identity=super().constructIdentity()+'. I have '+self._accessories+' as my accessories'
        return self._identity

lumut=Vegetative('lumut')
cemara=Generative('cemara')
mawar=FlowerPlant('mawar')
mangga=FruitPlant('mangga')

lumut.showIdentity()
cemara.showIdentity()
mawar.showIdentity()
mangga.showIdentity()