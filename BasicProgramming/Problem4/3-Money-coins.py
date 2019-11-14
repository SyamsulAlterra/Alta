#output kembalian
def convertToCoin(value):
    availableCoin=[10000,5000,2000,1000,500,200,100,50,20,10,1]
    change=[]
    
    for i in range(len(availableCoin)):
        remainder=value%availableCoin[i]
        if remainder != value:
            qty=int((value-remainder)/availableCoin[i])
            for j in range(qty):
                change.append(availableCoin[i])
            value=remainder
    return change

#test case
print(convertToCoin(543))
# output : [500, 20, 20 , 1, 1, 1]
print(convertToCoin(7752))
# output : [5000, 2000, 500, 200, 50, 1, 1]
print(convertToCoin(37454))
# output : [10000, 10000, 10000, 5000, 2000, 200, 200, 50, 1, 1, 1, 1]