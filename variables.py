# strings

print("yolo")
print('yolo')
empty = ""
print(empty)

multiple_lines = '''
This is a multiple line string
    '''
print(multiple_lines)

# length of a string
print(len(multiple_lines))

batman = 'bruce wayne'
first = batman[0]
print(first)

space = batman[5]
print(space)

last = batman[len(batman) - 1]
print(last)

# slicing - obtain portions of a string (substring) using the indicies
# [start:end]
# [start:end:step] - step is optional - default is 1
my_string = 'this is my string!'
print(my_string[0:4])
print(my_string[8:len(my_string)])

# conditional statement examples if, else, elif
# conditional statement examples if, else, elif
# if <condition>:
#   <code>
# elif <condition>:
#   <code>
# else:
#   <code>


# functions
# def <function_name>(<parameters>):
# once return is executed, the function is exited

def my_print_function():  # no parameters
    print('hello world')
    print('hello worlds')


my_print_function()


def minimum(first, second):
    if (first < second):
        return first
    return second


num1 = 21
num2 = 20

result = minimum(num1, num2)
print(result)

a_string = 'welcome to educative!'
new_string = a_string.replace('welcome to', 'greetings from')
print(a_string)
print(new_string)

llist = ['a', 'b', 'c', 'd']
print('>>'.join(llist))  # join the list elements with the >>
print('<<'.join(llist))  # join the list elements with the <<
print(', '.join(llist))  # join the list elements with the comma and space

# lambda functions - like arrow functions in JS
# lambda <parameters>: <expression>
# triple = lambda num: num * 3  # assigning the lambda to a variable


def triple(num): return num * 3  # assigning the lambda to a variable


print(triple(10))
