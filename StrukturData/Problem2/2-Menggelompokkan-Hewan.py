a1=["ayam","kucing","bebek","bangau","zebra"]
test=[["cacing","ayam","kuda",'anoa','kancil'],['cacing','ayam','kuda','anoa','kancil','unta','cicak'],a1]

def groupAnimals(lst):
    d={}
    hurufAwal="abcdefghijklmnopqrstuvwxyz"
    for l in lst:
        if l[0] in d:
            d[l[0]].append(l)
        else:
            d[l[0]]=[l]

    result=[]
    for h in hurufAwal:
        for key in d:
            if h==key:
                result.append(d[key])
    return result



print(groupAnimals(['cacing', 'ayam', 'kuda', 'anoa', 'kancil']))
# [['ayam', 'anoa'], ['cacing'], ['kuda', 'kancil']]
print(groupAnimals(['cacing', 'ayam', 'kuda', 'anoa', 'kancil', 'unta', 'cicak']))
# [['ayam', 'anoa'], ['cacing', 'cicak'], ['kuda', 'kancil'], ['unta']]