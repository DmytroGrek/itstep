# Сформировать третий список, содержащий элементы обоих списков без повторений;
simple_list = [1, 2, "i", 4, "5", "6", 7, 8]
list_with = [1, "i1", 7, "i3", "5", "i"]
list_3 = list(set(simple_list + list_with))
print(list_3)

