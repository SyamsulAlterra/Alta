#hitung digit bilangan
def countDigit(num):
    digit=1
    remainder=num%(10**digit)
    while(remainder!=num):
        digit+=1
        remainder=num%(10**digit)

    return digit

# cek faktor dan hitung digit masing-masing faktor
def digitPerkalianMinimum(num):
    i=1
    a=1
    b=1
    while(i*i<num):
        if num%i ==0:
            a=i
            b=int(num/i)
        i+=1
    
    return countDigit(a)+countDigit(b)

#test case
print(digitPerkalianMinimum(24)) # 2
print(digitPerkalianMinimum(90)) # 3
print(digitPerkalianMinimum(20)) # 2
print(digitPerkalianMinimum(179)) # 4
print(digitPerkalianMinimum(1)) # 2