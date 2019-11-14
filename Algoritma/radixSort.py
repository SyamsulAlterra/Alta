arr=[123,321,487,908,123,465,987,46,762,12389]

def findMax(arr):
    Max=None
    for num in arr:
        if Max==None or num>Max:
            Max=num
    return Max

def checkDigit(num):
    i=0
    remainder=0
    while (remainder!=num):
        i+=1
        remainder=num%(10**i)
    return i

def digit(i,num):
    return int((num%(10**i)-num%(10**(i-1)))/(10**(i-1)))

def radix(arr):
    digitMax=checkDigit(findMax(arr))
    currentDigit=0
    while(currentDigit<=digitMax):
        currentDigit+=1
        lst=[[],[],[],[],[],[],[],[],[],[]]
        for num in arr:
            numberDigit=digit(currentDigit,num)
            if checkDigit(num)<currentDigit:
                lst[0].append(num)
            else:
                lst[numberDigit].append(num)
        arr=[]
        for l in lst:
            arr+=l
        print(lst)
    return arr


print(radix(arr))
