def fibonacci(num):
    if num==0:
        return 0

    if num==1:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)
    
#test case
print(fibonacci(0)) # 0
print(fibonacci(2)) # 1
print(fibonacci(9)) # 34
print(fibonacci(10)) # 55
print(fibonacci(12)) # 144