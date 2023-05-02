from sys import getsizeof
from array import array
from collections import deque


zeros = [0] * 100
# 100 count 0

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combine = list1+list2
print(combine)

######################

numbers1 = list(range(20))
numbers2 = list(range(5, 20))
print(numbers1, numbers2)

chars = list("mostafa olyai")
print(chars)
######################

# chars[::5] print from 0 => 5 => 10 =>....
print(chars[2], chars[-3], chars[2:-2], chars[::5], chars[8::])
print(numbers1[::-1], numbers1[-8::])
######################

first, *other, second, third = numbers1
print(first, second, third, other)
############################

letters = ["a", "a", "b", "c"]
# enumerate(leeters) gives us tupple ,(0,"a")(1,"b")(2,"c")
for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)
##############################
letters.append("d")
print(letters)

letters.insert(0, "b")
print(letters)

print(letters.pop())
print(letters.pop())
print(letters.remove("a"))
# print(letters.remove("z"))#error

# del letters[0:1]
# print(letters)

# letters.clear()
# print(letters)
#############################

print(letters.index("a"))
# print(letters.index("z"))#error
print(letters.count("a"))
###################################################

list3 = [7, 9, 1, 4, 3]
print(sorted(list3), list3.sort(reverse=True), list3)
##########################
# tuple
list4 = [
    ("a", 8),
    ("b", 3),
    ("c", 9)
]


def sort_item(item):
    return item[1]


list4.sort(key=sort_item)
print(list4)

# lambda
items = [("a", 8), ("b", 3), ("c", 9)]


items.sort(key=lambda item: item[1])
print(items)
###################################################
######### map ################
x = list(map(lambda item: item[1]*2, items))
# [expression for item in items]
x1 = [item[1]*2 for item in items]
print(x, x1)
###################################################
######### filter ################
y = list(filter(lambda item: item[1] >= 5, items))
y1 = [item for item in items if item[1] >= 5]
print(y, y1)
##############################################

a = [1, 2, 3]
b = [10, 20, 30]
print(list(zip(a, b)))
print(list(zip(a, b, "abc")))
#######################################################
######## Stack ################
# developed by list
################### Queue ###############

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()

print(queue)
##############################################
################### Tuple ###############
point1 = ()
point2 = 1  # int
point3 = 1,  # tuple
point4 = (1, 2)
point5 = 1, 2

concat = point4+point5
iterate3 = point5*3

listtt = [1, 2]
point6 = tuple(listtt)
point6 = tuple("mosi")
point7 = point6[0:2]
o, p, i, *U = point6

print(point1, point2, point3, point4, point5,
      point6, point7, concat, iterate3, o, p, i)
########################################################
x = 10
y = 20

temp = y
y = x
x = temp
print(x, y)

# python
x = 10
y = 20

x, y = y, x
print(x, y)
###########################################################
############### Array #######################

numbers = array("i", [1, 2, -1])
print(numbers)
########################################################
############### Set #######################
# set tartib nadare
numbers = array("i", [1, 1, 2, 2, -1])
print(set(numbers))  # {1, 2, -1}
numbers1 = set(numbers)
numbers2 = {1, -1, 5}

print(numbers1 & numbers2)  # eshterak
print(numbers1 | numbers2)  # ejtema
print(numbers1 - numbers2)  # difference
# semantic difference, or first set or sec set not both
print(numbers1 ^ numbers2)
########################################################
############### Hash - Dic #######################
point = {'x': 1, 'y': 2}
point2 = dict()
print(point['y'])

# for
for key in point.items():
    print(key)

for key, value in point.items():
    print(key, value)

# dic comprehension
values = {x: x*2 for x in range(5)}
print(values)

# generator
# hameye values1 dakhele ram rikhte nemishe dar har tekrar miad oun lahze tolid mishe
values1 = (x*2 for x in range(5))
print(values1)
for x in values1:
    print(x)


# compare size
values = [x*2 for x in range(10000)]
values1 = (x*2 for x in range(10000))  # generator doesn't have len()
print(getsizeof(values), getsizeof(values1))
###############################################################
# unpacking operator for all iterrable
values = [1, 2, 3, 4]
values1 = [*values]
print(*values, values1)

first = {"x": 1}
second = {"y": 2}
combined = {**first, "b": 9, **second}
print(combined)
