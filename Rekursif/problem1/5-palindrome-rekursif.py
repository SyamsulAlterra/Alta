def palindromeRecursive(sentence):
    if len(sentence)==1:
        return True

    if sentence[0] == sentence[-1]:
        sentence=sentence[1:len(sentence)-1]
        return palindromeRecursive(sentence)
    else:
        return False

#test case
print(palindromeRecursive('katak')) # true
print(palindromeRecursive('blanket')) # false
print(palindromeRecursive('civic')) # true
print(palindromeRecursive('kasur rusak')) # true
print(palindromeRecursive('mister')) # false