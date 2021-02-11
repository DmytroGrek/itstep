# Сформировать третий список, содержащий элементы общие для двух списков;
simple_list = [1, 2, "i", 4, "5", "6", 7, 8]
list_with = [1, "i1", 7, "i3", "5", "i"]
# list_3 = list(set(simple_list) & set(list_with)) # в одну строку
list_3 = []
for elem in simple_list:
    for elem1 in list_with:
        if elem == elem1:
            list_3.append(elem)
print(list_3)

