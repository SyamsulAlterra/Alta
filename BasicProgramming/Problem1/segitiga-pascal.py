def factorial(a):
    for i in range(0,a+1):
        if a==0:
            return 1
        else:
            return a*factorial(a-1)

#print(factorial(5))

def pascalElement(a,b):
    return int(factorial(a)/(factorial(b)*factorial(a-b)))

#print(pascalElement(3,1))

def segitigaPascal(n):
    lst=""
    for i in range(n+1):
        for j in range(i+1):
            lst+=" "+str(pascalElement(i,j))
        print(lst)
        lst=""

segitigaPascal(5)

#output
'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''