def Dic(arr):
    d={}
    for a in arr:
        if not (a[0] in d):
            d[a[0]]=[a[0],a]
        else:
            d[a[0]]+=[a]
    return d

def initialGroupingDescending(arr):
    d=Dic(arr)
    hurufAwal="abcdefghijklmnopqrstuvwxyz"
    lst=[]
    for h in hurufAwal[-1:-len(hurufAwal):-1]:
        for key in d:
            if key.lower()==h:
                lst.append(d[key])
    return lst

#test case
print(initialGroupingDescending(['Budi', 'Badu', 'Joni', 'Jono']))
# [['J', 'Joni', 'Jono'], ['B', 'Budi', 'Badu']]
print(initialGroupingDescending(['Mickey', 'Yusuf', 'Donald', 'Ali', 'Gong']))
# [['Y', 'Yusuf'], ['M', 'Mickey'], ['G', 'Gong'], ['D', 'Donald'], ['A', 'Ali']]