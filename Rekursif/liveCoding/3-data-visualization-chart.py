def generateBarChart(arr):
    if len(arr)<1:
        print("please enter valid and not zero array\n")
        return

    maxValue=max(arr)
    if maxValue>=10 or min(arr)<0:
        print("""please enter valid element in an array. Valid element has range 0-9\n""")
        return

    arrBuffer=arr[:]

    for i in range(maxValue,-1,-1):
        string=str(i)+"|"
        fill=" III "
        blank="     "
        if i==0:
            for j in range(len(arr)):
                string+="-("+str(arr[j])+")-"
            print(string)
        else:
            maxArr=max(arrBuffer)
            for j in range(len(arr)):
                if arrBuffer[j]!=maxArr:
                    string+=blank
                else:
                    string+=fill
                    arrBuffer[j]-=1
            print(string)

generateBarChart([3, 6, 4, 7, 2])
'''
7|                III      
6|      III       III      
5|      III       III      
4|      III  III  III      
3| III  III  III  III      
2| III  III  III  III  III
1| III  III  III  III  III
0|-(3)--(6)--(4)--(7)--(2)-
'''

generateBarChart([9, 8, 7, 0, 1, 2, 3])
'''
9| III                               
8| III  III                          
7| III  III  III                     
6| III  III  III                     
5| III  III  III                     
4| III  III  III                     
3| III  III  III                 III
2| III  III  III            III  III
1| III  III  III       III  III  III
0|-(9)--(8)--(7)--(0)--(1)--(2)--(3)-
'''

generateBarChart([1, 2, 3, 4, 5, 4, 3, 2, 1])
'''
5|                     III                     
4|                III  III  III                
3|           III  III  III  III  III           
2|      III  III  III  III  III  III  III      
1| III  III  III  III  III  III  III  III  III
0|-(1)--(2)--(3)--(4)--(5)--(4)--(3)--(2)--(1)-
'''
        