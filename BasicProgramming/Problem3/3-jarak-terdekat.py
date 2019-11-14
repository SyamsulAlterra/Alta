#cari target terdekat
def targetTerdekat(arr):
    lsto=[]
    lstx=[]
    for i in range(len(arr)):
        if arr[i]=="o":
            lsto.append(i)
        elif arr[i]=="x":
            lstx.append(i)

    minimal=None
    for o in lsto:
        for x in lstx:
            check=abs(o-x)
            if minimal==None or minimal>check:
                minimal=check
                
    if minimal==None:
        minimal=0
    return minimal

#test case
print(targetTerdekat([' ', ' ', 'o', ' ', ' ', 'x', ' ', 'x'])) # 3 
print(targetTerdekat(['o', ' ', ' ', ' ', 'x', 'x', 'x'])) # 4 
print(targetTerdekat(['x', ' ', ' ', ' ', 'x', 'x', 'o', ' '])) # 1 
print(targetTerdekat([' ', ' ', 'o', ' '])) # 0 
print(targetTerdekat([' ', 'o', ' ','x', 'x', ' ', ' ', 'x'])) # 2 