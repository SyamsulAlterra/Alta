num=5

toPrint=""
for i in range(1,num+1):
    for j in range(1,num+1):
        if j<=i:
            toPrint+=str(j)
    print(toPrint)
    toPrint=""

#output
'''
1
12
123
1234
12345
'''