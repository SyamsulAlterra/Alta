menit=53
def konversiMenit(menit):
    m=int(menit/60)
    s=menit%60
    return str(m)+":"+str(s)

#test case
print(konversiMenit(63))#1:3
print(konversiMenit(124))#2:4
print(konversiMenit(53))#0:53
print(konversiMenit(88))#1:28
print(konversiMenit(120))#2:0