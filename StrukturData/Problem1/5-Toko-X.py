windi={"name":"Windi", "product":"Sepatu Stacattu", "amount":2}
vanessa={"name":"Vanessa", "product":"Sepatu Stacattu", "amount":3}
aing={"name":"aing", "product":"Baju Zoro", "amount":1}
rani={"name":"Rani", "product":"Sweater Uniklooh", "amount":2}
devi={"name":"Devi", "product":"Baju Zoro", "amount":1}
lisa={"name":"Lisa", "product":"Baju Zoro", "amount":1}

listBarang=[
    ["Sepatu Stacattu", 1500000,10],
    ["Baju Zoro",500000,2],
    ["Sweater Uniklooh",175000,1]
]



def countProfit(buyers):
    if buyers==[]:
        return []

    detailSepatu={"product":"Sepatu Stacattu", "shoppers":[], "leftOver":listBarang[0][2], "totalProfit":0}
    detailBaju={"product":"Baju Zoro", "shoppers":[], "leftOver":listBarang[1][2], "totalProfit":0}
    detailSweater={"product":"Sweater Uniklooh", "shoppers":[], "leftOver":listBarang[2][2], "totalProfit":0}
    profit={"Sepatu Stacattu":detailSepatu, "Baju Zoro":detailBaju, "Sweater Uniklooh":detailSweater}
    for buyer in buyers:
        good=buyer["product"] #apa yang dibeli?
        for barang in listBarang: #muter di stock
            if good==barang[0]: #kalo ada distock
                if buyer["amount"]<=barang[2]: #kalo stock cukup
                    profit[good]["shoppers"].append(buyer["name"])
                    profit[good]["leftOver"]=barang[2]-buyer["amount"]
                    barang[2]=barang[2]-buyer["amount"]
                    profit[good]["totalProfit"]+=buyer["amount"]*barang[1]
                # else:                       #kalo stock tidak cukup
                #     profit[good]["shoppers"]+=[]
                #     profit[good]["leftOver"]=barang[2]
                #     profit[good]["totalProfit"]+=0
    return [detailSepatu, detailBaju, detailSweater]

#test case
# test=[[windi, vanessa, rani], [windi, vanessa, rani, devi, lisa]]
# for t in test:
#     print(countProfit(t))

print(countProfit([
    {'name':'Windi', 'product':'Sepatu Stacattu', 'amount': 2},
    {'name':'Vanessa', 'product':'Sepatu Stacattu', 'amount': 3},
    {'name':'Rani', 'product':'Sweater Uniklooh', 'amount': 2}

]))
'''
[{'product': 'Sepatu Stacattu', 'shoppers': ['Windi', 'Vanessa'], 'leftOver': 5, 'totalProfit': 7500000}, {'produ
ct': 'Baju Zoro', 'shoppers': [], 'leftOver': 2, 'totalProfit': 0}, 
{'product': 'Sweater Uniklooh', 'shoppers': [], 'leftOver': 1, 'totalProfit': 0}]

'''

# Test Case 2
print(countProfit([
{'name':'Windi', 'product':'Sepatu Stacattu', 'amount': 8},
{'name':'Vanessa', 'product':'Sepatu Stacattu', 'amount': 10},
{'name':'Rani', 'product':'Sweater Uniklooh', 'amount': 1},
{'name':'Devi', 'product':'Baju Zoro', 'amount': 1},
{'name':'Lisa', 'product':'Baju Zoro', 'amount': 1}
]))

# Test Case 3
print(countProfit([
{'name':'Windi', 'product':'Sepatu Naikki', 'amount': 5}
]))

# Test Case 4
print(countProfit([])) # []

