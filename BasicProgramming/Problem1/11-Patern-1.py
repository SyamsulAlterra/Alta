def patter1(num):
    for i in range(num):
        line=""
        for j in range(num):
            if j>i:
                line+=" "
            else:
                line+="*"
        print(line)

patter1(5)
#output
'''
*
**
***
****
*****
'''