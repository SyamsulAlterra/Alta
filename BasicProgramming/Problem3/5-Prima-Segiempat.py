#cari prima selanjutnya
def nextPrime(prime):
    prime+=1
    earlyPrime=[2,3,5,7,11,13]
    if prime in range(14):
        for p in range(prime,14):
            if p in earlyPrime:
                return p
            else:
                p+=1 

    cond1=prime%2==0
    cond2=prime%3==0
    cond3=prime%5==0
    cond4=prime%7==0
    cond5=prime%11==0
    cond6=prime%13==0
    while cond1==True or cond2==True or cond3==True or cond4==True or cond5==True or cond6==True:
        prime+=1
        cond1=prime%2==0
        cond2=prime%3==0
        cond3=prime%5==0
        cond4=prime%7==0
        cond5=prime%11==0
        cond6=prime%13==0
    return prime
        
#print segi empat
def primaSegiEmpat(p,q,prime):
    total=0
    for i in range(q):
        toPrint=""
        for j in range(p):
            prime=nextPrime(prime)
            total+=prime
            toPrint+=" "+str(prime)
        print(toPrint)
    print("Total:",total)

#test case
primaSegiEmpat(2,3,13)
'''
17 19
23 29
31 37
Total: 156
'''

primaSegiEmpat(5,2,1)
'''
2 3 5 7 11
13 17 19 23 29
Total: 129
'''


