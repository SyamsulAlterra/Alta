def hour(num): #rekursif jam
    if num<3600:
        return 0
    
    num=num-3600
    return 1+hour(num)

def minutes(num): #rekursif menit
    if num<60:
        return 0
    
    num=num-60
    return 1+minutes(num)

def recursiveFormatDuration(num):
    if num<1 or num>86400:
        return "angka diluar ketentuan, masukkan angka 1-86400 inklusif"

    h=hour(num)
    if h!=0:
        stringH=str(h)+" jam "
    else:
        stringH=""

    m=minutes(num%3600)
    if m!=0:
        stringM=str(m)+" menit "
    else:
        stringM=""

    s=(num%3600)%60
    if s!=0:
        stringS=str(s)+" detik "
    else:
        stringS=""

    return stringH+stringM+stringS


print(recursiveFormatDuration(86400)) # 24 jam
print(recursiveFormatDuration(60)) # 1 menit
print(recursiveFormatDuration(6)) # 6 detik
print(recursiveFormatDuration(3660)) # 1 jam 1 menit
print(recursiveFormatDuration(62)) # 1 menit 2 detik
print(recursiveFormatDuration(7324)) # 2 jam 2 menit 4 detik
    