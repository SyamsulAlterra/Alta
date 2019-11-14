#Soal Convert To ASCII

#convert character to ASCII
def charToAscii(char):
    return ord(char)

#calculate total ASCII in string
def totalAscii(string):
    total=0
    for i in string:
        total+=charToAscii(i)
    return total
    

#compare ASCII of two string
def stringAcak(string1, string2):
    total1=totalAscii(string1)
    total2=totalAscii(string2)

    return total1==total2

#test case

print(stringAcak("malang","agmlan"))#True
print(stringAcak("alterra","rerlata"))#True
print(stringAcak("python","nothyd"))#False
print(stringAcak("python","nothyp"))#True
