sentence="xooxo"

def xo(sentence):
    o=sentence.count("o")
    x=sentence.count("x")
    return o==x

#test case
print(xo("xoxoxo"))#True
print(xo("xoooxo"))#False
print(xo("oxo"))#False
print(xo("xxxooo"))#True
print(xo("xoxooxxo"))#True