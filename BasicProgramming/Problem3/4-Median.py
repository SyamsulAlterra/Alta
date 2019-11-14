#cari median
def cariMedian(arr):
    totalNum=len(arr)
    if totalNum%2 == 0:
        index1=int(len(arr)/2)
        index2=int(index1-1)
        return (arr[index1]+arr[index2])/2
    else:
        index=int((len(arr)-1)/2)
        return arr[index]

#test case
print(cariMedian([1, 2, 3, 4, 5])) # 3
print(cariMedian([1, 3, 4, 10, 12, 13])) # 7
print(cariMedian([3, 4, 7, 7, 10])) # 7
print(cariMedian([1, 3, 3])) # 3
print(cariMedian([7, 7, 8, 8])) # 7.5
