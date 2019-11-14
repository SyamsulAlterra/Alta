arr=[43,1,1,1,1,1,4,8,6,6,6,6,123,321,487,908,123,465,987,46,762,12389,10,22,33,15,44,63,72,95,789,0,80,79,65,32]

def split(arr):
    if arr==[]:
        return [],[]
    pivot=int(len(arr)/2)
    #print(pivot)
    lst1=[]
    lst2=[arr[pivot]]
    lstBig=[]
    for i,num in enumerate(arr):
        if i!=pivot:
            if num<arr[pivot]:
                lst1.append(num)
            else:
                lst2.append(num)
    return lst1, lst2

def quickSort(arr,nTimes=10):    
    result=[]
    a,b=split(arr)
    result.append(a)
    result.append(b)
    arr=result
    for i in range(nTimes):
        result=[]
        for num in arr:
            a,b=split(num)
            result.append(a)
            result.append(b)
        arr=result
    
    result=[]

    for num in arr:
        result+=num
    
    return result

print(quickSort(arr))