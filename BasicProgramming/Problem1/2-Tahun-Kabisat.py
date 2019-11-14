def TahunKabisat(y):    
    if y%4 == 0 and y%100 != 0:
        return("Tahun Kabisat")
    elif y%4 == 0 and (y%100 == 0 and y%400 == 0):
        return("Tahun Kabisat")
    else:
        return("Bukan Tahun Kabisat")

#test case
print(TahunKabisat(1804))#Tahun Kabisat
print(TahunKabisat(1803))#Bukan Tahun Kabisat
print(TahunKabisat(2400))#Tahun Kabisat
print(TahunKabisat(2490))#Bukan Tahun Kabisat