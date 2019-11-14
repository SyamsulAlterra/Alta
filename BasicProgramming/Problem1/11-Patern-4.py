num=5

for i in range(1,num+1):
    toPrint=""
    end=int(i*(i+1)/2)
    a=list(j for j in range(end+1-i,end+1))
    for x in a:
        toPrint+=" "+str(x)
    print(toPrint)
    toPrint=""

#output
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''        