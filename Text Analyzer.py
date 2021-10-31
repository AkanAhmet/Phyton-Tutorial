def countOfChars(char,text):
    count = 0
    for i in text:
        if i == char:
            count+=1
    return count        

def findLongestWord(text):
    wordsInText = text.split(" ")
    max = 0
    currentIndex = 0
    for i in wordsInText:
        count = 0
        for k in i:
            count+=1
        if count > max:
            max = count
            currentIndex = i
    return currentIndex

file = open("document.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl. 
Rkcyvpvg vf orggre guna vzcyvpvg. 
Fvzcyr vf orggre guna pbzcyvpngrqa. 
Syng vf orggre guna arfgrq. 
Fcenfr fv orggre guna q""")
file.close()
filename = "document.txt"
with open(filename) as f:
    text = f.read()
alphabet = "abcdefghijklmnopqrstuvwxyz"

text = text.lower()

for char in alphabet:
    perc = 100 * countOfChars(char,text) / len(text)
    print( "Amount of {x} - {z}. Usage rate : % {y}". format(x = char , z =countOfChars(char,text),  y = round(perc,2)))

print("Longest word in Text is, {x}".format(x=findLongestWord(text)))