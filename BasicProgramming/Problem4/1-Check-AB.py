#check jarak a dan b
def checkAB(sentence):
    lsta=[]
    lstb=[]
    for i in range(len(sentence)):
        if sentence[i]=="a":
            lsta.append(i)
        elif sentence[i]=="b":
            lstb.append(i)
    
    for a in lsta:
        for b in lstb:
            if abs(a-b)==4:
                return True
    
    return False

#test case
print(checkAB('lane borrowed')) # True
print(checkAB('i am sick')) # False
print(checkAB('you are boring')) # True
print(checkAB('barbarian')) # True
print(checkAB('bacon and meat')) # False

