from functools import reduce

list_number = [1, 2, -1, -3, 9, -7, -5]
multiply = reduce(lambda a, b: a * b, list_number)
print(multiply)
# print(reduce(lambda a, b: a * b, list_number))
