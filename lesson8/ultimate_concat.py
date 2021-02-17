first_list = ["Neo", "Trinity", "Mouse"]
second_list = ["Matrix", "Forever", "Alone"]
output_list = []

for elem in first_list:
    for elem_1 in second_list:
        result = f'{elem} {elem_1}'  # result = elem + ' ' + elem_1 еще вариант
        output_list.append(result)

print(output_list)
