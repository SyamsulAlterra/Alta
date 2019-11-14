
def naikAngkot(arg):
    rute=["a","b","c","d","e","f"]
    hasilNarik=[]
    for penumpang in arg:
        dataPenumpang={}
        dataPenumpang["penumpang"]=penumpang[0]
        dataPenumpang["naikDari"]=penumpang[1]
        dataPenumpang["tujuan"]=penumpang[2]
        totalRute=rute.index(penumpang[2].lower())-rute.index(penumpang[1].lower())
        dataPenumpang["bayar"]=2000*totalRute
        hasilNarik.append(dataPenumpang)
    return hasilNarik

#test case
print(naikAngkot([['Dimitri','B','F'],['Icha','A','B']]))
'''
[{'penumpang': 'Dimitri', 'naikDari': 'B', 'tujuan': 'F', 'bayar': 8000}, 
{'penumpang': 'Icha', 'naikDari': 'A', 'tujuan': 'B', 'bayar': 2000}
]
'''
print(naikAngkot([]))
'''
[]
'''
