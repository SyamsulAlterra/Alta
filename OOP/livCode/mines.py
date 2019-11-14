import subprocess as sp
import random

class Cell():
    def __init__(self,default=" "):
        self.__cover='X'
        self.__fill=default

    def getFill(self):
        return self.__fill

    def color(self,char):
        return '\033[31m{c}'.format(c=char)

    def normalize(self,char):
        return '\033[0m{c}'.format(c=char)

    def showCover(self):
        print(self.normalize(self.__cover), end='')

    def showFill(self):
        print(self.color(self.__fill), end='')
        print(self.normalize(''), end='')

class BombCell(Cell):
    def __init__(self):
        super().__init__('!')

class BonusCell(Cell):
    def __init__(self):
        super().__init__('$')

    def color(self,char):
        return '\033[33m{c}'.format(c=char)


class Board():
    def __init__(self):
        self.__boardRow=None
        self.__boardColumn=None
        self.__choosenRow=None
        self.__choosenColumn=None
        self.__choice=None
        self.__playingBoard=None
        self.__score=0
        self.__round=0
        self.__mesage=''
        self.refreshBoard()
        self.start()
    
    def header(self):
        print('''
-------------------------------------
            Guess Game
-------------------------------------
1. Board size
2. Choose cell
98. Refresh Board
99. Exit
-------------------------------------
        ''')

    def refreshBoard(self):
        sp.call('clear', shell=True)

    def exit(self):
        print('')

    def start(self):
        self.header()
        if self.__round != 0:
            print(self.__message,end='')
            print(self.Normal(''))
            print('score: ', self.__score)
            self.showPlayedBoard()
        print('Masukkan pilihan anda: ', end='')
        self.__choice=int(input())


        if self.__choice==99:
            print('''
=====================================
You terminate the game before it ends
       Thank You for Playing
=====================================
            ''')
            self.exit()
        elif self.__choice==98:
            self.refreshBoard()
            self.start()
        elif self.__choice==1:
            if self.__playingBoard==None:
                print('Masukkan jumlah kolom: ', end='')
                self.__boardColumn=int(input())
                print('Masukkan jumlah baris: ', end='')
                self.__boardRow=int(input())
                self.__playingBoard=[ None for i in range(self.__boardRow) ]
                for i in range(self.__boardRow):
                    self.__playingBoard[i]=[ [self.randomizeCell(),0] for i in range(self.__boardColumn) ]
                self.__round+=1
                self.__message=''
                self.refreshBoard()
                self.start()
            else:
                self.refreshBoard()
                print(self.Kuning('You have already created a board, please finish it first'),end='')
                print(self.Normal(''))
                self.start()
        elif self.__choice==2:
            if self.__playingBoard==None:
                self.refreshBoard()
                print(self.Kuning('You are currently don\'t have a board choose option 1 (Board size) to create it'),end='')
                print(self.Normal(''))
                self.start()
            else:
                print('Masukkan kolom yang akan dibuka: ',end='')
                self.__choosenColumn=int(input())-1
                print('Masukkan baris yang akan dibuka: ',end='')
                self.__choosenRow=int(input())-1
                self.guessBoard(self.__choosenRow,self.__choosenColumn)
                if not self.endStatus():
                    self.refreshBoard()
                    self.__round+=1
                    self.start()
                else:
                    self.refreshBoard()
                    self.showPlayedBoard()
                    print('''
==============================
       End of the game
      Your score is {s}
==============================
                    '''.format(s=self.__score))
        else:
            print(self.Kuning('this program has minimum input handling, try to input correctly'))
            print('there is mistake in your input, restart the game')
            print(self.Normal(''))


    def Ijo(self, char):
        return '\033[32m{c}'.format(c=char)
    
    def Normal(self, char):
        return '\033[0m{c}'.format(c=char)

    def Kuning(self,char):
        return '\033[33m{c}'.format(c=char)

    def showPlayedBoard(self):
        top = self.Ijo(' ')+''.join([ str(i+1) for i in range(self.__boardColumn) ])
        print(top, end='')
        print(self.Normal(''))
        for i in range(self.__boardRow):
            print(self.Ijo(str(i+1)),end='')
            print(self.Normal(''),end='')
            for j in range(self.__boardColumn):
                if self.__playingBoard[i][j][1]==0:
                    self.__playingBoard[i][j][0].showCover()
                else:
                    self.__playingBoard[i][j][0].showFill()
            print('')

    def randomizeCell(self):
        randomNumber=random.randint(1,3)
        c=None

        if randomNumber==1:
            c=Cell()
        elif randomNumber==2:
            c=BombCell()
        elif randomNumber==3:
            c=BonusCell()

        return c

    def guessBoard(self,row,column):
        self.__playingBoard[row][column][1]=1
        if self.__playingBoard[row][column][0].getFill()=='$':
            self.__message=self.Kuning('Bonus Cell - Woow')
            print(self.Normal(''))
            self.__score+=10
        elif self.__playingBoard[row][column][0].getFill()=='!':
            self.__message=self.Kuning('Bomb Cell - Wadidaw')
            print(self.Normal(''))
            self.__score-=10
        elif self.__playingBoard[row][column][0].getFill()==' ':
            self.__message=self.Kuning('Regular Cell')
            print(self.Normal(''))
    
    def endStatus(self):
        for i in range(self.__boardRow):
            for j in range(self.__boardColumn):
                if self.__playingBoard[i][j][1]==0:
                    return False
        return True

                
tes=Board()