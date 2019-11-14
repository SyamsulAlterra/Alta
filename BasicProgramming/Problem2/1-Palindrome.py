#fungsi
def palindrome(word):
    p=""
    for c in word:
        p=c+p
    return (p == word)

#check test case
print(palindrome('katak')) # True
print(palindrome('blanket')) # False
print(palindrome('civic')) # True
print(palindrome('kasur rusak')) # True
print(palindrome('mister')) # False