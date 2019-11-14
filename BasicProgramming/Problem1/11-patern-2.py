num=5

base=num+num-2

lst=""
print(lst)
for i in range(num):
    #for k in range(i+1):
    for j in range(base+1):
        if j in range(num-1-i, num+i, 2):
            lst+="*"
        else:
            lst+=" "
    print(lst)
    lst=""

#output
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""