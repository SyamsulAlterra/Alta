class Cat():
    def __init__(self, name, colorFur, legNum):
        self._name=name
        self._furColor=colorFur
        self.__numOfLeg=legNum
        self._message=''
    
    def constructMesage(self):
        self._message='Saya '+self._name+' dengan detail, '+'warna bulu: '+self._furColor+' dengan jumlah kaki : '+self.__numOfLeg
        return self._message

    def showIdentity(self):
        print(self.constructMesage())

class Fish():
    def __init__(self, type, food):
        self.__type=type
        self._food=food

    def showIdentity(self):
        print('Saya Ikan dengan detail, jenis: '+self.__type+', makanan: '+self._food)

class Flower():
    def __init__(self, type, warna, petalNum):
        self.__type=type
        self._color=warna
        self._NumOfPetal=petalNum

    def showIdentity(self):
        print('Saya bunga dengan detail, jenis: '+self.__type+', color: '+self._color+', num of petal: '+self._NumOfPetal)

class Car():
    def __init__(self, type, warna, tireNum):
        self.__type=type
        self._color=warna
        self._NumOfTire=tireNum

    def showIdentity(self):
        print('Saya mobil dengan detail, Type: '+self.__type+', color: '+self._color+', num of tire: '+self._NumOfTire)

kucing=Cat('Ahmad','hitam','4')
kucing.showIdentity()

paus=Fish('paus','plankton')
cupang=Fish('cupang','cacing')
arwana=Fish('arwana','jangkrik')
sapu2=Fish('sapu-sapu','pelet')
paus.showIdentity()
cupang.showIdentity()
arwana.showIdentity()
sapu2.showIdentity()

print('')

bangkai=Flower('bangkai', 'merah','12')
anggrek=Flower('anggrek', 'putih','8')
mawar=Flower('mawar','merah','3')
melati=Flower('melati','kuning','5')
bangkai.showIdentity()
anggrek.showIdentity()
mawar.showIdentity()
melati.showIdentity()

print('')

sedan=Car('sedan','merah','4')
truk=Car('truk','hijau','6')
tronton=Car('tronton','coklat','12')
angkot=Car('angkot','kuning','4')
sedan.showIdentity()
truk.showIdentity()
tronton.showIdentity()
angkot.showIdentity()

