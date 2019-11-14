def cariModus(tup):
    modus=tup[0]
    modusAppear=None
    singularity=True
    for num in tup:
        n=tup.count(num)
        if num != modus:
            singularity=False

        if modusAppear == None or n>modusAppear:
            modus=num
            modusAppear=n

    if singularity:
        return -1
    
    return modus
    

#test case
print(cariModus((10,4,5,2,4))) # 4
print(cariModus((5,10,10,6,5))) # 5
print(cariModus((10,3,1,2,5))) # -1
print(cariModus((1,2,3,3,4,5))) # 3
print(cariModus((7,7,7,7,7))) # -1