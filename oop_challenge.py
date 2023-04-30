# Challenge 1: Implement Rectangle Class Using the Encapsulation
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

# Challenge 1 tests:
rec = Rectangle(3,4)
print(rec.area())
print(rec.perimeter())

# Challenge 2: Implement the Complete Student Class
class Student:
    # not defining initalizer so setting defined properties to None
    __name = None
    __rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

# Challenge 2 tests:
s = Student()
s.setName("Jeff")
print(s.getName())
s.setRollNumber(100)
print(s.getRollNumber())

class Circle:
    # Insert your code here
    def __init__(self, radius=None):
        self.radius = radius

    def print_area(self):
        print(3.14 * self.radius)

obj = Circle(7)
obj.print_area()

# inheritence challenges
""" class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate
 """

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        # write code here
        pass

    def deposit(self, amount):
        # write code here
        pass

    def getBalance(self):
        # write code here
        pass


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        # write code here
        pass


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
    