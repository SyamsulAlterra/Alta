def dominoCard(handCard, deskCard):
    outputCandidate=[]
    for h in  handCard:
        if h[0] == deskCard[0] or h[1] == deskCard[1] or h[0]==deskCard[1] or h[1]==deskCard[0]:
            outputCandidate.append(h)
    
    print(outputCandidate)

    Max=None
    choosenCard=None
    for output in outputCandidate:
        new=output[0]+output[1]
        if Max==None or new>Max:
            Max=new
            choosenCard=output

    if choosenCard:
        return "keluarkan kartu ["+str(choosenCard[0])+","+str(choosenCard[1])+"]"
    
    return "tutup 1 kartu"

#test case
print(dominoCard([[3,3], [6,5], [3,4], [2,1]], [3,5])) # "keluarkan kartu [6,5]"
print(dominoCard([[3,3], [6,5], [3,4], [2,1]], [1,3])) # "keluarkan kartu [3,4]"
print(dominoCard([[2,4], [6,6], [3,6]], [1,5])) # "tutup 1 kartu"