# return keyword ends function execution

def minimum(first, second):
    if (first < second):
        return first
    return second

num1 = 10
num2 = 35

result = minimum(num1, num2)
print(result)

def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print(number)


rec_count(5)