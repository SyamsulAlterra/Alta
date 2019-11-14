#fungsi check prima
def checkPrima(num):
    earlyPrime=[2,3,5,7,11,13]
    if num in range(14):
        if num in earlyPrime:
            return True
        return False
    else:
        condition=[]
        for i,prime in enumerate(earlyPrime):
            condition.append(num%prime==0)
        if True in condition:
            return False
        return True


#fungsi extract digit
def extractDigit(num):
    remainder=0
    i=0
    digit=[]
    while(remainder!=num):
        i+=1
        d=((num%(10**i))-remainder)/(10**(i-1))
        digit.append(int(d))
        remainder=num%(10**i)
    return digit


#Soal Full Prima

#fungsi check full prima
def fullPrima(num):
    if checkPrima(num) == True:
        digit=extractDigit(num)
        for d in digit:
            if checkPrima(d)==False:
                return "Tidak"
        return "Ya"
    else:
        return "Tidak"

# #test case
# case=[2,3,11,13,23,29,37,41,43,53,14]
# for c in case:
#     print(fullPrima(c))

print(fullPrima(2))#Ya
print(fullPrima(3))#Ya
print(fullPrima(11))#Tidak
print(fullPrima(13))#Tidak
print(fullPrima(23))#Ya
print(fullPrima(29))#Tidak
print(fullPrima(37))#Ya
print(fullPrima(41))#Tidak
print(fullPrima(43))#Tidak
print(fullPrima(53))#Ya
print(fullPrima(14))#Tidak









