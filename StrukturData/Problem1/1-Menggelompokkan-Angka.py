def mengelompokkanAngka(arr):
    genap=[]
    ganjil=[]
    tiga=[]
    for num in arr:
        if num%2 == 0 and num%3!=0:
            genap.append(num)
        elif num%2 ==1 and num%3 !=0:
            ganjil.append(num)
        elif num%3==0:
            tiga.append(num)
    return [genap,ganjil,tiga]

#test case
print(mengelompokkanAngka([2, 4, 6]))   
# [ [2, 4], [], [6]]
print(mengelompokkanAngka([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [ [2, 4, 8], [1, 5, 7], [3, 6, 9]]
print(mengelompokkanAngka([100, 151, 122, 99, 111]))
# [ [100, 122], [ 151 ], [ 99, 111 ]]
print(mengelompokkanAngka([]))
# [ [], [] , []]
