cars = ["Honda", "civic", 2022]
print(cars)

# selecting an index
print(cars[1])

# get the length
print(len(cars))

# type cast to a list with the list() method
num_seq = range(0, 10)
num_list = list(num_seq)  # cast the range into a list type
print(num_list)

num_seq = range(3, 50, 3)
print(list(num_seq))

# sequential indexing - going deeper into the index
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]

print(world_cup_winners[1])
print(world_cup_winners[1][1])  # only access Spain from the 1 index
print(world_cup_winners[1][1][0])  # only access the first letter of spain

# merge list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
merge = a + b
print(merge)

# using the extend list method to add b to the end of a and create one list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a.extend(b)
print(a)


# adding elements to list - append method adds to the end
a = [1, 2, 3, 4, 5]
a.append(15)
print(a)

empty_list = []
empty_list.append(1)
empty_list.append("text")
empty_list.append(3)
print(empty_list)

# insert method - add items to specific index (index, newElement)
a = [1, 2, 3, 4, 5]
a.insert(2, 20)
print(a)

# pop method - remove items from list from the end
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
last_house = houses.pop()
print(f"popped item {last_house}")
print(houses)

# remove method - remove a specific item
a = [1, 2, 3, 4, 5]
a.remove(4)
print(a)

# slicing
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[0:3]) # print from specified index

# index method - return the index value of given item
a = [1, 2, 3, 4, 5]
print(a.index(5)) # return the index of value 5