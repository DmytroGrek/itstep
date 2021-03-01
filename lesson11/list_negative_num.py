list_number = [1, 2, -1, -3, -4, 0]
list_negative_num = filter(lambda x: x < 0, list_number)
print(list(list_negative_num))

# print(list(filter(lambda x: x < 0, list_number)))
