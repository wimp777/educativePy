class Employee:
    # define properties must be assigned to something
    id = 3789
    salary = 2000
    department = "IT"

e = Employee()

print("ID =", e.id)
print("Salary =", e.salary)
print("Department =", e.department)

print('')
# creating properties outside of a class
class New_Employee:
    # define properties must be assigned to something
    id = None
    salary = None
    department = None

f = New_Employee()
# assigning values to properties of f
f.id = 500
f.salary = 2500
f.department = "HR"

print("ID =", f.id)
print("Salary =", f.salary)
print("Department =", f.department)
print('')

#
#
# Initialize Objects
#
#

class initialize_employee:

    team = "Texans" # class variable outside of the initializer

    def __init__ (self, id, salary, department):
        self.id = id
        self.salary = salary
        self.department = department

# creating object of initialize_employee with default (__init__) parameters
steve = initialize_employee(9999,2500,"HR")

print("initialized object output:")
print(steve.id)
print(steve.salary)
print(steve.department)

print('')

# class methods - Class methods are accessed using the class name and can be accessed without creating a class object.
class Player:
    teamName = 'Dynamo' # class variable

    def __init__(self, name):
        self.name = name # create instance variable

    @classmethod
    def getTeamName(cls): # cls referes to the class like self refers to the object of the class
        return cls.teamName

print(Player.getTeamName())
print('')

# static method - static methods can be accessed using the class name or the object name
class Player:
    teamName = 'Liverpool' # class variable

    def __init__(self, name):
        self.name = name # create instance variables

    @staticmethod
    def demo():
        print("I am a static method")

p1 = Player('lol')
p1.demo()
Player.demo()
print('')

# access modifiers

# public attributes - can be accessed inside and outside the class
class public_attr:
    def __init__(self, id, salary):
        # all properties are public
        self.id = id
        self.salary = salary

    def displayID(self):
        print("ID:", self.id)

steve = public_attr(2500, 6000)
steve.displayID()
print(steve.salary)
print('')

# private attributes - can't be accessed directly from outside the class only from inside the class
class private_arre:
    def __init__(self,id, salary):
        self.id = id
        self.__salary = salary # private attribute defined with the __

steve =private_arre(100, 2500)
print("ID:", steve.id)
#print("Salary:", steve.__salary) # will cause error because private
print('')

class private_method:
    def __init__(self, id, salary):
        self.id = id
        self.__salary = salary
    
    def displaySalary(self): # public method - can access the private salary property
        print("salary:", self.__salary)

    def __displayID(self): # private method with __name
        print("id:", self.id)

steve = private_method(10,2500)
steve.displaySalary()
#steve.__displayID() # will throw error because private
print('')

class access_private:
    def __init__(self, id, salary):
        self.id = id
        self.__salary = salary # private property

steve = access_private(10,5000)
print(steve._access_private__salary) # access the private property by using the class name prefix
print('')


# code challenge 1
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z

        return (a + b + c)

p = Point(2,4,5)
print(p.sqSum())
print('')

# code challenge 2
class Student:
    def __init__(self,name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
    def totalObtained(self):
        mark1 = self.phy
        mark2 = self.chem
        mark3 = self.bio

        return(mark1 + mark2 + mark3)

    def percentage(self):
        pct_mark = (self.totalObtained() / 300) * 100
        return pct_mark

s = Student('joe',10,20,50)
print("Total obtained:", s.totalObtained())
print("percent mark: ", s.percentage())
print('')

#
# information hiding
#

# getter method allows reading a properties value
# # setter method allows modifying a properties value        
      
class User:
    def __init__(self, username=None):
        self.__username = username # private property

    def setUsername(self, x): # setter of the private property
        self.__username = x

    def getUsername(self): # getter of private property
        return (self.__username)

steve = User('steve1')
print('Before setting:', steve.getUsername())
steve.setUsername('steve2')
print('After setting:', steve.getUsername())

# encapsulation - refers to the concept of binding data and the methods operating on that data in a single unit, which is also called a class
# For encapsulating a class, all the properties should be private and any access to the properties should be through methods such as getters and setters
class User2:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if ((self.__username.lower() == username.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__username.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")

#
# Inheritance
#
print('')
# child class has all public attributes of the parent class
# Parent Class (Super Class or Base Class): This class allows the reuse of its public properties in another class.
# Child Class (Sub Class or Derived Class): This class inherits or extends the superclass

""" class ParentClass:
    # attributes of parent class

class ChildClass(ParentClass):
    # attributes of chile class """

class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)

obj1 = Car("Honda", "red", "2022", 4)
obj1.printCarDetails()
print('')
# The use of super() comes into play when we implement inheritance. It is used in a child class to refer to the parent class without explicitly naming it

class superVehicle:
    fuelCap = 90

class superCar(superVehicle):
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class with super()
        print("Fuel cap from the Vehicle class", super().fuelCap)

        # accessing fuelCap from the child class using self
        print("Fuel cap from the superCar child class", self.fuelCap)

obj1 = superCar()
obj1.display()
print('')

#
# Polymorphism -  refers to the same object exhibiting different forms and behaviors
#

# In effect, polymorphism cuts down the work of the developer. When the time comes to create more specific subclasses with certain unique attributes and behaviors
# the developer can alter the code in the specific areas where the responses differ. All other pieces of the code can be left untouched

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calc area
    def getArea(self):
        return (self.width * self.height)

class Circle:
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calc area
    def getArea(self):
        return (self.radius * self.radius * 3.142)

shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
