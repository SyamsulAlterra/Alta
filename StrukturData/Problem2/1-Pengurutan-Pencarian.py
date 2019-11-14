#test case
a1=["min",[1,1,1],[8,15,17,9]]
a2=["max",[4,8,9,12],[33,88,99,11]]
a3=["min",[1,2,2,2,2,2],[67,45,55]]
a4=["max",[6,4,2,8,10,2],[6,5,13,23]]
a5=["min",[5,11,18,16],[3,1,8,13]]
test=[a1,a2,a3,a4,a5]

def Max(arr):
    Max=None
    for num in arr:
        if Max==None or num>Max:
            Max=num
    return Max

def Min(arr):
    Min=None
    for num in arr:
        if Min==None or num<Min:
            Min=num
    return Min

def statistik(kata, arr1, arr2):
    kata=kata.lower()
    if kata=="max":
        m1=Max(arr1)
        m2=Max(arr2)
    elif kata=="min":
        m1=Min(arr1)
        m2=Min(arr2)
    
    print(m1,m2)

statistik('min', [1, 1, 1], [8, 15, 17, 9]) # 1 8
statistik('max', [4, 8, 9, 12], [33, 88, 99, 11]) # 12 99
statistik('min', [1, 2, 5, 2, 2], [67, 45, 55]) # 1 45
statistik('max', [6, 2, 4, 10, 8, 2], [6, 5, 13, 23]) # 10 23 
statistik('min', [5, 11, 18, 6], [3, 1, 8, 13]) # 5 1 

    