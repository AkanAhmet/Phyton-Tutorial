import re

pattern = r"spam" # r means raw here
text = "eggspamsausagespam"
print(f"Current Pattern : {pattern}  Current Text: {text}")
if re.match(pattern,text):
    print("Pattern Matched")
else:
    print("Pattern Not matched")

search = re.search(pattern,text)
if re.search(pattern,text):
    print("Search Matched")
else:
    print("Search Not matched")

print(f"Start : {search.start()} \nEnd : {search.end()} \nSpan: {search.span()}, \nGroup: {search.group()}")

print(f"Findall results:  {re.findall(pattern,text)}")

newText = re.sub(pattern, "plant", text)
print ( f"Other important  method is 'sub'. Result : {newText}")
#--------------------META CHARECTERS-----------------------------------------------------------------

pattern2 = r"gr.y"

if re.match(pattern2,"grey"):
    print("Pattern Matched")
else:
    print("Pattern Not matched")

pattern3 = r"^gr.y$"
#The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline, and end with y.
if re.match(pattern3,"grey"):
    print("Pattern Matched")
else:
    print("Pattern Not matched")
#-------------------------------------CHARECTER CLASSES-------------------------------------------------------------

pattern4 = r"^[A-Z].[0-9]$" # [^0-9] it means shold not be entirely composed of digits

if re.match(pattern4, "Ad2"):
    print("Pattern Matched")
else:
    print("Pattern Not matched")

# More Regex codes will be added later.