num=5

for i in range(num):
    line=""
    for j in range(num):
        if j<num-i:
            line+=" "
        else:
            line+="*"
    print(line)

#output
'''
    *
   **
  ***
 ****
*****
'''