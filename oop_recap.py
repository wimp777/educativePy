# Properties are variables that contain information regarding the object of a class
# Methods are like functions that have access to properties (and other methods) of a class. Methods can accept parameters and return values. They are used to perform an action on an object of a class

# declare a class - must start with a letter or underscore, should only by comprised of numbers, letters, or underscores
class ClassName:
    pass


# create an instance of a class
instance = ClassName()


class Employee:
    # defining the properties and assigning values to them
    ID = 1234
    salary = 2500
    department = "IT"


# create an instance of the Employee class
Steve = Employee()
# create a new attribute for the instance outside of the class
Steve.title = "Manager"

# print the properties of the instance
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department", Steve.department)
print("Title", Steve.title)


# class initialzer - the initializer is used to initialize an object of a class. It’s a special method that outlines the steps that are performed when an object of a class is created in the program
# __init__
# self - the self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. It does not have to be named self, you can call it whatever you like - self is just convention


class Employee_2:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


class Employee_3:
    # default initializer with optional parameters
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee_2 class with default parameters
Josh = Employee_2(1234, 2500, "IT")
print("ID:", Josh.ID)
print("Salary:", Josh.salary)
print("Department:", Josh.department)

# class and instance variables


class Player:
    team = "Texans"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

# implement methods in a class - A method is a group of statements that performs some operations and may or may not return a result


class Employee3:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


Jerry = Employee3(1234, 2500, "IT")

print('ID:', Jerry.ID)
print('Salary:', Jerry.salary)
print('Department:', Jerry.department)
print('Tax:', Jerry.tax())
print('salary per day', Jerry.salaryPerDay())

# method overloading - refers to making a method perform different operations based on the nature of its arguments

# class methods - Class methods are accessed using the class name and can be accessed without creating a class object


class Player2:
    teamName = 'Texans'  # class variable

    def __init__(self, name):
        self.name = name  # creating instance variable

    @classmethod  # class method decorator
    def getTeamName(cls):  # cls is used to access class variable similar to self
        return cls.teamName


print(Player2.getTeamName())

# static class methods - can be accessed using the class name or object name - They are used as utility functions inside the class or when we do not want the inherited classes to modify a method definition
# It does not use a reference to the object or class, so we do not have to use self or cls. We can pass as many arguments as we want and use this method to perform any function without interfering with the instance or class variables


class Player3:
    teamName = 'Saints'  # class variable

    def __init__(self, name):
        self.name = name  # creating instance variable

    @staticmethod  # static method decorator
    def demo():
        print('i am a static method')


p1 = Player3('lol')
p1.demo()
Player3.demo()

# access modifiers - public, private, protected
# public - can be accessed from anywhere by default
# private - can only be accessed from within the class


class privateEmployee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # private property


steve = privateEmployee(1234, 2500)
print("ID: ", steve.ID)
# print("salary", steve.__salary)  # this will throw an error


class privateMethod:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # private property

    def displaySalary(self):  # public method to access private property
        print("Salary:", self.__salary)

    def __displayID(self):  # private method
        print("ID", self.ID)


keith = privateMethod(1234, 2500)
keith.displaySalary()
# keith.__displayID()  # this will throw an error


# challenge - square numbers and return sum
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x**2 + self.y**2 + self.z**2)


sum = Point(1, 3, 5)
print(sum.sqSum())

# challenge 2


class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return (self.phy + self.chem + self.bio)

    def percentage(self):
        return (self.totalObtained() / 300) * 100


studentTest = Student('mark', 50, 100, 75)
print(studentTest.totalObtained())
print(studentTest.percentage())

# challenge 3 - calculator


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num1 * self.num2)

    def divide(self):
        return (self.num2 / self.num1)


#
# information hiding
#
