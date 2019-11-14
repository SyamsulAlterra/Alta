def getDigit(num):
    i=0
    remainder=0
    digit=[]
    while (remainder!=num):
        i+=1
        d=(num%(10**i)-num%(10**(i-1)))/(10**(i-1))
        digit.append(int(d))
        remainder=num%(10**i)
    return digit

def totalDigitRekursif(num):
    if num<10:
        #print("base")
        return num

    numString=getDigit(num) #tidak boleh pake str(num)
    total=0
    for n in numString:
        total+=totalDigitRekursif(n)

    return total

    #print("rekursif")
    

#test case
print(totalDigitRekursif(512)) # 8
print(totalDigitRekursif(1542)) # 12
print(totalDigitRekursif(5)) # 5
print(totalDigitRekursif(21)) # 3
print(totalDigitRekursif(11111)) # 5