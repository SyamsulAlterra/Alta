#fungsi bantuan cari digit
def getDigit(num):
    i=0
    remainder=0
    digit=[]
    while (remainder!=num):
        i+=1
        d=(num%(10**i)-num%(10**(i-1)))/(10**(i-1))
        digit.append(int(d))
        remainder=num%(10**i)
    return digit

#fungsi pasangan terbesar
def pasanganTerbesar(num):
    digit=getDigit(num)
    m=None
    for i in range(len(digit)-1):
        twoDigit=digit[i]+digit[i+1]*10
        if m==None or twoDigit>m:
            m=twoDigit

    return m

#test case
print(pasanganTerbesar(641573)) # 73
print(pasanganTerbesar(12783456)) # 83
print(pasanganTerbesar(910233)) # 91
print(pasanganTerbesar(71856421)) # 85
print(pasanganTerbesar(79918293)) # 99
