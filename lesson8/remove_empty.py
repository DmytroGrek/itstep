list_with_strings = [1, ' ', 'fhg', '', '45']

for elem in list_with_strings:
    if elem == '' or elem == ' ':
        list_with_strings.remove(elem)

print(list_with_strings)
