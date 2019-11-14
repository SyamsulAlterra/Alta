def Dic(arr):
    d={}
    for a in arr:
        if not (a in d):
            d[a]=1
        elif a in d:
            d[a]=d[a]+1
    dict={}
    for key in d:
        if d[key] not in dict:
            dict[d[key]]=[key]
        elif d[key] in dict:
            dict[d[key]]+=[key]

    return dict

def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1]<arr[j]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr


def mostFrequentItem(arr):
    dic=Dic(arr)
    lst=[]
    for d in dic:
        lst.append(d)

    lst=sort(lst)

    string=""
    for l in lst:
        for index in range(len(dic[l])):
            string+=dic[l][index]+"("+str(l)+") "
    
    return string

#test case
print(mostFrequentItem(['asus', 'asus', 'samsung', 'iphone', 'iphone', 'asus', 'asus']))
# samsung(1), iphone(2), asus(4)
print(mostFrequentItem(['9','b','b','c','9','9','b','9','2','2']))
# c(1), 2(2), b(3), 9(4)
print(mostFrequentItem(['book', 'laptop', 'iPod']))
# book(1), laptop(1), iPod(1)