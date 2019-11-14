import subprocess as sp

class Position():
    def __init__(self):
        self.__name=None
        self.__totalShip=4
        self.__map=[ ['.','.','.','.'] for i in range(4) ]
        self.__guessedMap=[ ['.','.','.','.'] for i in range(4) ]
        self.placeShip()
        self.__row=None
        self.__column=None

    def checkAvailableShip(self,row,column):
        if self.__map[row][column]=='s':
            return True
        return False

    def inputPos(self,no):
        print('Enter your ship number {num}: '.format(num=(no+1)), end='')
        pos=input()
        try:
            self.__row=int(pos[0])-1
            self.__column=int(pos[1])-1
            if (self.__row>3 or self.__row<0) or (self.__column>3 or self.__column<0):
                print('enter number between 1 and 4')
                self.inputPos(no)
            elif self.checkAvailableShip(self.__row, self.__column):
                print('You have already placed ship there, please enter another position')
                self.inputPos(no)
        except:
            print('your position is invalid')
            self.inputPos(no)


    def placeShip(self):
        self.__map=[ ['.','.','.','.'] for i in range(4) ]
        print('Enter your name: ',end='')
        self.__name=input()
        for i in range(4):
            print(i)
            self.inputPos(i)
            self.__map[self.__row][self.__column]='s'
        
        print('=====================')
        print('this is your ship position')
        self.getPos()
        print('Enter to continue')
        dummy=input()
        sp.call('clear', shell=True)


    def getName(self):
        return self.__name

    def getPos(self):
        for i in range(len(self.__map)):
            print(self.__map[i])

    def getGuessedPos(self):
        for i in range(len(self.__guessedMap)):
            print(self.__guessedMap[i])

    def takeMissile(self,row,column):
        if self.__map[row][column]=='s':
            self.__guessedMap[row][column]='x'
        else:
            self.__guessedMap[row][column]='o'

    def stayAlive(self):
        self.__totalShip=4
        for i in range(4):
            for j in range(4):
                if self.__guessedMap[i][j] == 'x' and self.__map[i][j]=='s':
                    self.__totalShip-=1

        if self.__totalShip>0:
            return True
        else:
            return False

class Game():
    def __init__(self):
        self.__pos1=Position()
        self.__pos2=Position()
        self.__round=0

    def attack(self,p1,p2):
        p2.getGuessedPos()
        print('choose your opponent location: ', end='')
        loc=input()
        row=int(loc[0])-1
        column=int(loc[1])-1
        p2.takeMissile(row, column)
        print('position '+ loc +' is attacked')
        p2.getGuessedPos()
        print('Enter to continue')
        dummy=input()
        sp.call('clear', shell=True)
        if not p2.stayAlive():
            print(p1.getName()+' win the game')
        

    def start(self):
        while self.__pos1.stayAlive() and self.__pos2.stayAlive():
            self.__round+=1
            if self.__round%2 == 1:
                print('player 1 turn')
                self.attack(self.__pos1, self.__pos2)
            else:
                print('player 2 turn')
                self.attack(self.__pos2, self.__pos1)
            
battlefield=Game()
battlefield.start()
        