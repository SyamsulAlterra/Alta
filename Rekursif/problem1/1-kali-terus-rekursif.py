def getDigit(num):
    i=0
    remainder=0
    digit=[]
    while (remainder!=num):
        i+=1
        d=(num%(10**i)-remainder)/(10**(i-1))
        digit.append(int(d))
        remainder=num%(10**i)
    return digit

def kaliTerusRekursif(num):
    if num<10:
        return num
    
    numList=getDigit(num)  #tidak boleh pake str(num) -> pake getDigit(buatan sendiri)
    total=1
    for num in numList:
        total=total*int(num)

    return kaliTerusRekursif(total)


#test case
print(kaliTerusRekursif(66)) # 8
print(kaliTerusRekursif(3)) # 3
print(kaliTerusRekursif(24)) # 8
print(kaliTerusRekursif(654)) # 0
print(kaliTerusRekursif(1231)) # 6