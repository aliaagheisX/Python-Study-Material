#SECTION __init__ && Attributes && Methods && Self
class car:
    #attributes
    vehicle = "Car"

     # instance attribute to inialize attributes
     # run as soon as the object is created 
    def __init__(self, name, speed, color) :
        self.name = name
        self.speed = speed
        self.color = color
    #Methods
    def Drive(self) :
        print(f"Start Driving The {self.color} {self.name}...")
    def __str__(self) :
        return f"{self.name} - {self.color} - {self.speed}"

my_car = car("Volvo", 210, "Red")

print(my_car.name)                          #Volvo
my_car.name = "BMW"; print(my_car.name)     #BMW

print(my_car)  #BMW - Red - 210


#SECTION Inheritance
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        s = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        area = (s*(s-self.sides[0])*(s-self.sides[1])*(s-self.sides[2])) ** 0.5
        return area

shape = Triangle()
shape.inputSides()
print(shape.sides) 
print(f"The area of the triangle is {shape.findArea():.2f}")


#SECTION overriden
class person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def print(self) :print(f"This is just a person")

class student(person):
    def __init__(self, name, age) : person.__init__(self, name, age)
    #overriden the print function in person
    def print(self) :print(f"This is just a student")

p1 = person("Pixels", 8)
p2 = student("Pixels", 8)
p1.print()
p2.print()

print(isinstance(p2,person))        #True
print(isinstance(p2,student))       #True
print(isinstance(p1,student))       #False

print(issubclass(person, student))  #False
print(issubclass(student, person))  #True


#SECTION polymorphism
class Cat:
    def makeSound(self) : print("Miaw Miaw Miaw...")

class Dog:
    def makeSound(self) : print("Hoow Hoow Hoow...")

c = Cat()
d = Dog()

c.makeSound()
d.makeSound()


#SECTION Encapsulation
#Protects : _ (convention not a rule)
#Private : __
 
class Base:
    def __init__(self):
        self.a = "Pixels"
        self._b = "Pixels"
        self.__c = "Pixels"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self) 
        #print(self.__c)# ! Error
        print(self._b)

 
 
# Driver code
obj1 = Base()
print(obj1.a)


