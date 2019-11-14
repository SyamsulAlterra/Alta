class Vehicles():
    def __init__(self, name):
        self._name=name
        self._withEngine='\'no engine\''
        self._type='Parent of all vehicles'
        self._message=None
        
    def constructSentence(self):
        self._message = "Hi, I'm " + self._type +". My name is "+ self._name + ". My engine status is "+self._withEngine
        return self._message

    def identifyMyself(self):
        print(self.constructSentence())

class Bikes(Vehicles):
    def __init__(self, name):
        super().__init__(name)
        self._type='Bike'
        self._wheelCount=2
        
    def constructSentence(self):
        self._message=super().constructSentence()+'. I have '+str(self._wheelCount)+' wheel(s)'
        return self._message


class PedalBikes(Bikes):
    def __init__(self, name):
        super().__init__(name)
        self._type='Pedal Bike'


class MotorBikes(Bikes):
    def __init__(self, name):
        super().__init__(name)
        self._withEngine='\'with engine\''
        self._type='Motor Bike'

class Cars(Vehicles):
    def __init__(self, name):
        super().__init__(name)
        self._withEngine='\'with engine\''
        self._type='Car'
        self._wheelCount=4
        
    def constructSentence(self):
        self._message=super().constructSentence() + '. I have '+str(self._wheelCount)+' wheel(s)'
        return self._message

class SportCars(Cars):
    def __init__(self, name):
        super().__init__(name)
        self._type='Sport Car'
        self._engineType='V8'

    def constructSentence(self):
        self._message=super().constructSentence()+". My engine type = "+self._engineType
        return self._message 

class PickupCars(Cars):
    def __init__(self, name):
        super().__init__(name)
        self._type='Pickup Car'
        self._engineType='Solar'

    def constructSentence(self):
        self._message=super().constructSentence()+". My engine type = "+self._engineType
        return self._message

class Busses(Vehicles):
    def __init__(self, name):
        super().__init__(name)
        self._type='Busses'
        self._withEngine='\'with engine\''
        self._wheelCount=4

    def constructSentence(self):
        self._message=super().constructSentence()+'. I have '+str(self._wheelCount)+" wheel(s)"
        return self._message

class Busses(Vehicles):
    def __init__(self, name):
        super().__init__(name)
        self._type='Bus'
        self._withEngine='\'with engine\''
        self._wheelCount=4

    def constructSentence(self):
        self._message=super().constructSentence()+'. I have '+str(self._wheelCount)+" wheel(s)"
        return self._message

class PrivateBusses(Busses):
    def __init__(self, name):
        super().__init__(name)
        self._type='Bus [Private Bus]'

class PublicBusses(Busses):
    def __init__(self, name):
        super().__init__(name)
        self._type='Bus [Public Bus]'

a=Vehicles('Gerobak')
a.identifyMyself()

b=PedalBikes('Pedal Bike')
b.identifyMyself()

c=MotorBikes('Motor Bike')
c.identifyMyself()

d=SportCars('Sport Car')
d.identifyMyself()

e=PickupCars('Pickup Car')
e.identifyMyself()

g=PublicBusses('Transjakarta')
g.identifyMyself()

f=PrivateBusses('School Bus')
f.identifyMyself()