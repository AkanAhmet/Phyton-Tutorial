import this

"""  PEP Suggestions : 
- modules should have short, all-lowercase names;
- class names should be in the CapWords style;
- most variables and function names should be lowercase_with_underscores;
- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
- names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.
 lines shouldn't be longer than 80 characters;
- 'from module import *' should be avoided;
- there should only be one statement per line.
PEP 8 also recommends using spaces around operators and after commas to increase readability. """

if __name__ == "__main__":
    print("Im not imported by other class")

def myFunc(x, y = 7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)

myFunc(1,2,3,4,5, ahmet= 6, akan =7)

a,b,*c,d = [1,2,3,4,5,6]
print(a)
print(b)
print(c)
print(d)

a,b = [3,5] # Swap
b,a = a,b

x = 7
y = 8 if x <= 9 else 11

for i in range(4):
    if i == 5:
        break
else:
    print("Unbroken")