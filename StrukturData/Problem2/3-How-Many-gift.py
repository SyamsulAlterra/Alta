def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1]<arr[j]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

def howManyGifts(maxBudget, gifts):
    gifts=sort(gifts)
    total=0
    for i,gift in enumerate(gifts):
        total+=gift
        if total>maxBudget:
            return i
    return i

#test case
print(howManyGifts(30000, [15000, 12000, 5000, 3000, 10000])) # 4
print(howManyGifts(10000, [2000, 2000, 3000, 1000, 2000, 10000])) # 5
print(howManyGifts(4000, [7500, 1500, 2000, 3000])) # 2
print(howManyGifts(50000, [25000, 25000, 10000, 15000])) # 3
print(howManyGifts(0, [10000, 3000])) # 0