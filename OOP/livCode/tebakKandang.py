import random

class Kandang():
    def __init__(self,default='X'):
        self.__huruf=default
    
    def warna(self, char):
        return '\033[31m{c}'.format(c=char)

    def normalize(self,char):
        return '\033[0m{c}'.format(c=char)

    def getHuruf(self):
        return self.__huruf

    def setHuruf(self,h):
        self.__huruf=h

    def showKandang(self):
        for i in range(3):
            if i==1:
                print('|'+ self.warna(self.getHuruf())+self.normalize('|'))
            else:
                print('|||')
        

class KandangKambing(Kandang):
    def __init__(self):
        super().__init__()
        self.setHuruf('K')

class KandangBebek(Kandang):
    def __init__(self):
        super().__init__()
        self.setHuruf('B')

    def warna(self,char):
        return '\033[33m{c}'.format(c=char)

class KandangZebra(Kandang):
    def __init__(self):
        super().__init__()
        self.setHuruf('Z')

    def warna(self, char):
        return '\033[34m{c}'.format(c=char)


class Board():
    def __init__(self):
        self.__listKandang=[]
        self.__jumlahKandang=0
        self.__tebakan=None
        self.__kandangDibuka=None

    def Kuning(self,char):
        return '\033[33m{c}'.format(c=char)

    def Biru(self, char):
        return '\033[34m{c}'.format(c=char)

    def Ijo(self, char):
        return '\033[32m{c}'.format(c=char)
    
    def Merah(self, char):
        return '\033[31m{c}'.format(c=char)

    def Normal(self, char):
        return '\033[0m{c}'.format(c=char)

    def showMenu(self):
        print('===================')
        print('Tebak Kandang')
        print('===================')
        print('1. Main')
        print('99. Exit')
        print('===================')
        print('Pilih menu: ', end='')
        pilihan=input()
        pilihan=int(pilihan)

        if pilihan == 1:
            print('masukkan jumlah kandang: ', end='')
            self.__jumlahKandang=int(input())
            self.__listKandang=[ [Kandang(), 0] for i in range(self.__jumlahKandang) ]
            # self.__listKandang[0]=[KandangBebek(), 0]
            # self.__listKandang[1]=[KandangZebra(), 0]
            # self.__listKandang[2]=[KandangKambing(), 0]
            
            self.randomizeKandang()
        else:
            print('Terima kasih telah bermain tebak kandang')

    def showPilihanKandang(self):
        for i in range(self.__jumlahKandang):
            if self.__listKandang[i][1]==0:
                Kandang(str(i+1)).showKandang()
                # print(self.__listKandang[i][1])
            else:
                self.__listKandang[i][0].showKandang()
                # print(self.__listKandang[i][1])
            print('')

    def tebakKandang(self):
        self.showPilihanKandang()
        print('Pilih kandang yang ingin dibuka: ', end='')
        self.__kandangDibuka=int(input())-1
        print('==Pilihan==')
        print(self.Biru('K')+self.Normal(': Kambing'))
        print(self.Merah('Z') +self.Normal(': Zebra'))
        print(self.Kuning('B') +self.Normal(': Bebek'))
        print('Masukan tebakan: ',end='')
        self.__tebakan=input()
        if self.__listKandang[self.__kandangDibuka][0].getHuruf().lower() == self.__tebakan.lower():
            self.__listKandang[self.__kandangDibuka][1]=1
            self.showPilihanKandang()
            print(self.Ijo('Tebakan benar'))
            print(self.Normal(''))
        else:
            self.showPilihanKandang()
            print(self.Kuning('Tebakan salah'))
            print(self.Normal(''))
        self.randomizeKandang()

            
    def randomizeKandang(self):
        for i in range(self.__jumlahKandang):
            nilaiAcak=random.randint(1,3)
            k=None
            if nilaiAcak==1:
                k=KandangKambing()
            elif nilaiAcak==2:
                k=KandangBebek()
            elif nilaiAcak==3:
                k=KandangZebra()
            else:
                print('never enter this')

            if self.__listKandang[i][1] == 0:
                self.__listKandang[i]=[k, 0]

    def winCheck(self):
        for i in range(self.__jumlahKandang):
            if self.__listKandang[i][1]==0:
                return False
        return True

    def start(self):
        self.showMenu()
        while not self.winCheck():
            self.tebakKandang()

        self.showPilihanKandang()
        print('Selamat anda berhasil menebak seluruh kandang')



tes=Board()
tes.start()


# print(random.randint(0,3))