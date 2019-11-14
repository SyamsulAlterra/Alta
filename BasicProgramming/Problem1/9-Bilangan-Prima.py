def checkPrima(num):
    identifier=1
    
    if num==1:
        identifier=0 #print("Bukan bilangan prima")
    elif num==2:
        identifier=1 #print("Bilangan prima")
    else:
        for x in range(2,num):
            if num%x == 0:
                identifier=0

    if identifier == 0:
        return ("Bukan bilangan prima")
    else:
        return ("Bilangan prima")

#test case
test=[3,7,10,17,337]

print(checkPrima(3))#Bilangan Prima
print(checkPrima(7))#Bilangan Prima
print(checkPrima(10))#Bukan Bilangan Prima
print(checkPrima(17))#Bilangan Prima
print(checkPrima(337))#Bilangan Prima