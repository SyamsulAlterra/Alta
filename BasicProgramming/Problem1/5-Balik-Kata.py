def balikKata(sentence):
    message=""
    for i in sentence[-1:-len(sentence)-1:-1]:
        message+=i
    return message

#test case
test=["John Doe","Hello World and Coders"]

print(balikKata("John Doe"))#"eoD nhoJ"
print(balikKata("Hello World"))#"sredoC dna dlroW olleH"