dimitri={'name':"Dimitri", 'score':90, 'class':'foxes'}
alexei={'name':"Alexei", 'score':85, 'class':'wolves'}
sergei={'name':"Sergei", 'score':74, 'class':'foxes'}
anastasia={'name':"Anastasia", 'score':78, 'class':'wolves'}
alexander={'name':"Alexander", 'score':100, 'class':'foxes'}
alisa={'name':"Alisa", 'score':76, 'class':'wolves'}
vladimir={'name':"Vladimir", 'score':92, 'class':'foxes'}
albert={'name':"Albert", 'score':71, 'class':'wolves'}
viktor={'name':"Viktor", 'score':80, 'class':'tigers'}


def graduates(students):
    bachelors={}
    for stud in students:
        if stud['score'] >= 75 and not (stud["class"] in bachelors):
            bachelors[stud["class"]]=[{"name":stud["name"], "score":stud["score"]}]
        elif stud['score'] >= 75 and stud["class"] in bachelors:
            bachelors[stud["class"]]+=[{"name":stud["name"], "score":stud["score"]}]
    return bachelors


#test case
# test=[[dimitri, alexei, sergei, anastasia], [alexander, alisa, vladimir, albert, viktor]]
# for t in test:
#     print(graduates(t))

# Test Case 1
print(graduates([])) # {}

# Test Case 2
print(graduates([
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
'score' : 74,
'class' : 'foxes'   
},
{
'name' : 'Anastasia',
'score' : 78,
'class' : 'wolves'   
}
]))

# Test Case 3
print(graduates([
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