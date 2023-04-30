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
