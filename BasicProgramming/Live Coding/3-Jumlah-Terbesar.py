#Soal Maximum Sequence

#fungsi max sequence
def maxSequence(lst):
    Max=None
    for i in range(len(lst)):
        new=0
        for j in range(i,len(lst)):
            new=lst[j]+new
            if Max==None or new>Max:
                Max=new
    return Max

#test case
print(maxSequence([-2,1,-3,4,-1,2,1,-5,4]))#6
print(maxSequence([-2,-5,6,-2,-3,1,5,-6]))#7
print(maxSequence([-1,2,10,3,5,-7,-4,12,-1,-2,-3]))#21


