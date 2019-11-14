#cek deret geometri
def tentukanDeretGeometri(arr):
    r=arr[1]/arr[0]
    for i in range(1,len(arr)):
        # print(arr[i]/arr[i-1])
        if arr[i]/arr[i-1] != r:
            return False
    return True
    
#test case
print(tentukanDeretGeometri([1, 3, 9, 27, 81])) # True
print(tentukanDeretGeometri([2, 4, 8, 16, 32])) # True
print(tentukanDeretGeometri([2, 4, 6, 8])) # False
print(tentukanDeretGeometri([2, 6, 18, 54])) # True
print(tentukanDeretGeometri([1, 2, 3, 4, 7, 9])) # False