dimitri={'name':"Dimitri", 'score':90, 'class':'foxes'}
alexei={'name':"Alexei", 'score':85, 'class':'wolves'}
sergei={'name':"Sergei", 'score':100, 'class':'foxes'}
anastasia={'name':"Anastasia", 'score':78, 'class':'wolves'}
alexander={'name':"Alexander", 'score':100, 'class':'foxes'}
alisa={'name':"Alisa", 'score':76, 'class':'wolves'}
vladimir={'name':"Vladimir", 'score':92, 'class':'foxes'}
albert={'name':"Albert", 'score':71, 'class':'wolves'}
viktor={'name':"Viktor", 'score':80, 'class':'tigers'}

def highestScore(students):
    classDict={}
    Max={}
    for stud in students:
        if (stud["class"] in classDict) and (stud["score"]>Max[stud["class"]]):
            classDict[stud["class"]]={"name":stud["name"],"score":stud["score"]}
            Max[stud["class"]]=stud["score"]
        elif not (stud["class"] in classDict):
            classDict[stud["class"]]={"name":stud["name"],"score":stud["score"]}
            Max[stud["class"]]=stud["score"]
    return classDict

# #test case
# test=[[dimitri, alexei, sergei, anastasia],[alexander, alisa, vladimir, albert, viktor]]
# for t in test:
#     print(highestScore(t))

# Test Case 1

print(highestScore([])) # {}

# Test Case 2
print(highestScore([
{
'name' : 'Dimitri',
'score' : 90,
'class' : 'foxes'   
},
{
'name' : 'Alexei',
'score' : 85,
'class' : 'wolves'   
},
{
'name' : 'Sergei',
'score' : 100,
'class' : 'foxes'   
},
{
'name' : 'Anastasia',
'score' : 78,
'class' : 'wolves'   
}
]))

# Test Case 3
print(highestScore([
{
'name' : 'Alexander',
'score' : 100,
'class' : 'foxes'
},
{
'name' : 'Alisa',
'score' : 76,
'class' : 'wolves'
},
{
'name' : 'Vladimir',
'score' : 92,
'class' : 'foxes'
},
{
'name' : 'Albert',
'score' : 71,
'class' : 'wolves'
},
{
'name' : 'Viktor',
'score' : 80,
'class' : 'tigers'
}
]))

