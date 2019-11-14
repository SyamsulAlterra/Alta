#fungsi check palindrome
def palindromeCheck(num):
    if num<10:
        return True
    remainder=0
    lst=[]
    i=0
    while(remainder!=num):
        i+=1
        toAppend=(num%(10**i)-remainder)/(10**(i-1))
        lst.append(toAppend)
        remainder=num%(10**i)

    palindrome=0

    for i in range(len(lst)):
        palindrome+=lst[i]*(10**(len(lst)-i-1))
    return int(palindrome)==int(num)

#cari angka palindrome selanjutnya
def angkaPalindrome(num):
    a=num+1
    while(palindromeCheck(a)==False):
        a+=1

    return a

#test case
print(angkaPalindrome(8)) # 9
print(angkaPalindrome(10)) # 11
print(angkaPalindrome(117)) # 121
print(angkaPalindrome(175)) # 181
print(angkaPalindrome(1000)) # 1001
