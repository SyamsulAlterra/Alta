def faktorBilangan(num):
    message=""
    for i in range(1,num+1):
        if num%i==0:
            message+=" "+str(i)
    return message

#test case
print(faktorBilangan(6))#(1,2,3,6)
print(faktorBilangan(12))#(1,2,3,4,6,12)
print(faktorBilangan(14))#(1,2,7,14)
print(faktorBilangan(16))#(1,2,4,8,16)
print(faktorBilangan(20))#(1,2,4,5,10,20)
