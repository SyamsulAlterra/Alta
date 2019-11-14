#cek angka prima
def angkaPrima(num):
    if num == 1:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
    
    return True

#test case
print(angkaPrima(1))  # False
print(angkaPrima(3)) # True
print(angkaPrima(7)) # True
print(angkaPrima(6)) # False
print(angkaPrima(23)) # True
