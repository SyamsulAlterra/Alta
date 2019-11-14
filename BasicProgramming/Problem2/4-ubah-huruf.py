#fungsi
def ubahHuruf(word):
    hasil=""

    for w in word:
        if w==" ":
            hasil+=" "
        else:
            hasil+=chr(ord(w)+1)

    return hasil

#test case
print(ubahHuruf('wow'))  # xpx
print(ubahHuruf('developer'))  # efwfmpqfs
print(ubahHuruf('keren'))  # lfsfo 
print(ubahHuruf('semangat'))  # tfnbohbu