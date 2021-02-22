def remove_int_ext(values_list, num):
    result = []
    result_1 = 0
    for elem in values_list:
        if elem != num:
            result.append(elem)
        else:
            result_1 += 1
    return f'{result} \nКількість видалень: {result_1}'


print(remove_int_ext(['dfd', 58, 58, 'aaa'], 58))
