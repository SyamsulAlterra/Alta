
def arrToDic(arr):
    dic={}
    key=["firstName","lastName","gender","birthYear"]
    for i,item in enumerate(arr):
        dic[key[i]]=item

    if len(dic)==len(key):
        dic[key[3]]=2019-arr[3]
    elif len(dic)<=len(key):
        dic[key[3]]="Invalid"
        
    return dic

def changeMe(bigArray):
    for i,arr in enumerate(bigArray):
        print(i+1,arr[0],arr[1]+":")
        print(arrToDic(arr))
#test case
changeMe([['Christ', 'Evans', 'Male', 1982], ['Robert', 'Downey', 'Male']])

'''
1 Chris Evans:
{'firstName': 'Christ', 'lastName': 'Evans', 'gender': 'Male', 'age': 37 }
2 Robert Downey:
{'firstName': 'Robert', 'lastName': 'Downey', 'gender': 'Males', 'age':'invalid'}
'''