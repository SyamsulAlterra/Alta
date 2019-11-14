listBarang=[
    ["Sepatu Stacattu", 1500000],
    ["Baju Zoro",500000],
    ["Baju H&N",250000],
    ["Sweater Uniklooh",175000],
    ["Casing Handphone",50000]
]

def shoppingTime(memberId, money):
    nota={"memberId":memberId, "money":money, "listPurchased":[], "changeMoney":0}

    if memberId=="":
        return "Mohon maaf, toko X hanya berlaku untuk member saja"
    elif money<50000:
        return "Uang tidak cukup"

    for i,barang in enumerate(listBarang):
        if money>=barang[1]:
            nota["listPurchased"].append(barang[0])
            nota["changeMoney"]=money-barang[1]
            break
    
    for barang in listBarang:
        if nota["changeMoney"]>=barang[1] and not (barang[0] in nota["listPurchased"]):
            nota["listPurchased"].append(barang[0])
            nota["changeMoney"]-=barang[1]

    return nota

#test case
# test=[['1820RzKrnWn08',2475000],['82Ku8Ma742',170000],['',2475000],['234JdhweRxa53',15000],['','']]
# for t in test:
#     print(shoppingTime(t[0],t[1]))

print(shoppingTime('1820RzKrnWn08',2475000))
# {'memberId': '1820RzKrnWn08', 
# 'money': 2475000, 
# 'listPurchased': ['Sepatu Stacattu', 'Baju Zoro', 'Baju H&N', 'Sweater Uniklooh', 'Casing Handphone'], 
# 'changeMoney': 0}

print(shoppingTime('82Ku8Ma742',170000))
'''
{'memberId': '82Ku8Ma742', 
'money': 170000, 
'listPurchased': ['Casing Handphone'], 
'changeMoney': 120000}
'''

print(shoppingTime('',2475000))
# Mohon maaf, toko X hanya berlaku untuk member saja
print(shoppingTime('234JdhweRxa53', 15000))
# Mohon maaf, uang tidak cukup
print(shoppingTime('', ''))
# Mohon maaf, toko X hanya berlaku untuk member saja
