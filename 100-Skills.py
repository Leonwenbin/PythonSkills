#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: wenbin
@file: 100-Skills.py
@time: 2021/07/17/15/28
"""
import ast
import heapq
from enum import Enum

# skill-01
numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")

# skill-02
one, two, three, four, five = numbers
print(one, four, five)

# skill-03
scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]

print(heapq.nlargest(3, scores))  # [91, 87, 82]
print(heapq.nsmallest(5, scores))  # [15, 33, 33, 49, 51]

# skill-04
print(numbers)
print(*numbers)


def sum_of_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total


print(sum_of_numbers(*numbers))

# skill-05
_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)

# skill-06


# skill-07
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# skill-07
dictionary = {'a': 2, 'b': 3}
squared_dictionary = {key: num * num for (key, num) in dictionary.items()}
print(squared_dictionary)


# skill-08


class Status(Enum):
    NO_STATUS = -1
    NOT_STARTED = 0
    IN_PROCESS = 1
    COMPLETED = 2


print(Status.IN_PROCESS.name)
print(Status.COMPLETED.value)

# skill-09
name = 'leon'
print(name * 3)

# skill-10
x = 3
print(1 < x < 10)

# skill-11
first_dictionary = {'name': 'Fan', 'location': 'Guangzhou'}
second_dictionary = {'name': 'Fan', 'surname': 'Xiao', 'location': 'Guangdong, Guangzhou'}

result = first_dictionary | second_dictionary

print(result)

# skill-12
books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')
print(books.index('Mastery'))

# skill-13
input_num = "[1,2,3]"


def string_to_list(string):
    return ast.literal_eval(string)


print(string_to_list(input_num))


# skill-14
def subract(a, b):
    return a - b


print(subract(1, 3))
print(subract(b=3, a=1))

print('I', 'Love', 'you', sep='/')

dictionary_a = {"a": 1, "b": 2}
dictionary_b = {"c": 3, "d": 4}

merged = {**dictionary_a, **dictionary_b}

print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(ord('"'))
print(bool("Strings"))
print(bool(""))
print(complex(10, 3))
print(hex(235423))

my_list = [1, 2, 3, 4]
odd = filter(lambda x: x % 2 == 1, my_list)
print(list(odd))
print(my_list)

squared = map(lambda x: x ** 2, my_list)
print(list(squared))


def get_address():
    return 'localhost:8081'


def get_address():
    return 'localhost:8082'


def get_address():
    return 'localhost:8083'


print(get_address())




