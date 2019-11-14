import re
import subprocess as sp

class Calculator():
    def __init__(self):
        self.__header='+++++++++++++++CALCULATOR+++++++++++++++++++++'
        self.__value1=None
        self.__value2=None
        self.__validValueList=[]
        self.__result=None

    def start(self):
        print(self.__header)
        print('1: Open Calculator')
        print('99: Exit')
        print('Masukan Pilihan Anda:', end=" ")

        choice=input()

        if choice=='1':
            sp.call('clear', shell=True)
            self.inputValues()
        elif choice=='99':
            sp.call('clear', shell=True)
            print("Thank you")
        else:
            sp.call('clear', shell=True)
            print('please enter valid option: 1 to proceed and 99 to exit','\n')
            self.start()

    def inputValues(self):
        
        print(self.__header)
        print('Masukan value 1:', end=" ")
        self.__value1=input()
        print('Masukan value 2:', end=" ")
        self.__value2=input()        

        numberPattern='\A\d+'
        valueList=[self.__value1,self.__value2]
        self.__validValueList=[]
        for value in valueList:
            cek=re.findall(numberPattern, value)
            self.__validValueList+=cek

        # print(self.__validValueList)

        if len(self.__validValueList)<2:
            print('please check both your input, it should be valid number')
            self.inputValues()
        else:
            for i in range(len(self.__validValueList)):
                self.__validValueList[i]=int(self.__validValueList[i])
            self.operation()

    def operation(self):
        
        print(self.__header)
        print('Please Enter Calculation Operation')
        print('1. Addition')
        print('2. Substraction')
        print('3. Multiplication')
        print('4. Division')
        print(self.__header)
        print('Pilihan Anda:', end=" ")
        choice=input()
        numberPattern='\A\d+'
        cek=re.findall(numberPattern,choice)
        
        if cek:
            if int(cek[0])>4 or int(cek[0])<1:
                
                print('please enter number between 1 and 4 (inclusive)')
                self.operation()
            elif int(cek[0])==1:

                self.__result=self.__validValueList[0]+self.__validValueList[1]
                print('hasil:', self.__result)
                self.start()
            elif int(cek[0])==2:

                self.__result=self.__validValueList[0]-self.__validValueList[1]
                print('hasil:', self.__result)
                self.start()
            elif int(cek[0])==3:

                self.__result=self.__validValueList[0]*self.__validValueList[1]
                print('hasil:', self.__result)
                self.start()
            elif int(cek[0])==4:
                if self.__validValueList[1]==0:
                    print('attempt to divide number with zero, please try again')
                    self.inputValues()
                else:
                    self.__result=self.__validValueList[0]/self.__validValueList[1]
                    print('hasil:', self.__result)
                    self.start()
        else:
            
            print('please enter valid number')
            self.operation()



'''
Calculator Testing
'''
tes=Calculator()
tes.start()


'''
Regex Testing
'''
# valueList=[]
# print('Masukan value 1:', end=" ")
# value1=input()
# valueList.append(value1)
# print('Masukan value 2:', end=" ")
# value2=input()
# valueList.append(value2)

# validValueList=[]
# numberPattern='\A\d+'
# for value in valueList:
#     cek=re.findall(numberPattern, value)
#     print(cek)
#     validValueList+=cek

# print(validValueList)