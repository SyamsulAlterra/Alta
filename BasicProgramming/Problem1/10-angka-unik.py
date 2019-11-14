lst=["1",'2','3','4','5','6','7','8','9','0']

givenString="5900967"
def angkaUnik(givenString):
    result=[]
    for i in lst:
        appearance=0
        for num in givenString:
            if num==i:
                appearance+=1

        if appearance==1:
            result.append(i)

    return result

#test case
test=["1234123","76523752","112723335"]
print(angkaUnik("1234123"))#[4]
print(angkaUnik("76523752"))#[3,6]
print(angkaUnik("112723335"))#[5,7]
