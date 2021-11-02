class Animal:
    def __init__(self,colour = "White"):
        self.colour = colour
    def print():
        print(colour)
    def speak(self):
        print("Im an animal !")
    def forInstances(self):
        print("My superclass is Animal")


class Dog(Animal):
    def speak(self):
        print("Im a dog")  
        super().forInstances() 
         

duman= Animal("grey")
print(duman.colour)
duman.speak()


Sibirya = Dog("Black")
print(Sibirya.colour)
Sibirya.speak()


#------------------------------------------------------------------------------------------------------------------------------
class Sphere:
    pi = 3.14
    def __init__(self, r = 1):
        self.r = r
    def circumference(self):
        return 2 * self.pi * self.r
    def area(self):
        return self.pi * self.r * self.r

sphere1 = Sphere(2)
print(" Area = {x} , Circumference = {y}".format ( x = sphere1.area(), y = sphere1.circumference()))
sphere1.r = 3
print(" Area = {x} , Circumference = {y}".format ( x = sphere1.area(), y = sphere1.circumference()))

#------------------------------------------MAGIC METHODS---------------------------------------------------------------------

class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

first = Vector2D(5,7)
second= Vector2D(3,9)
result = first + second
print(f"{result.x}+{result.y}" )
#-----------------------------------------GETTER / SETTERS------------------------------------------------------------------
class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password")
            if(password == "ahmet" ):
                self._pineapple_allowed = value
            else:
                raise ValueError("Intruder !")
pizza = Pizza(["cheese","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
#------------------------------------------------------------------------------------------------------------------------------