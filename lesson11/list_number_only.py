list_number = ['12', '1g', '300A', 'fgfg', 'dF45d', '1345']
list_number_only = map(int, filter(lambda x: x.isdigit(), list_number))
print(list(list_number_only))
# print(list(map(int, filter(lambda x: x.isdigit(), list_number))))
