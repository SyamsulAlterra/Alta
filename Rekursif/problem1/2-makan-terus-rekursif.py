def makanTerusRekursif(waktu,jumlahMakan=0):
    if waktu==0:
        return jumlahMakan
        
    if waktu <= 15:
        return jumlahMakan+1

    waktu=waktu-15
    return makanTerusRekursif(waktu,jumlahMakan+1)


#test case
# test=[66,100,90,10,0,16]
# for t in test:
#     print(makanTerusRekursif(t))

print(makanTerusRekursif(66)) # 5
print(makanTerusRekursif(100)) # 7
print(makanTerusRekursif(90)) # 6
print(makanTerusRekursif(10)) # 1
print(makanTerusRekursif(0)) # 0