# по простому много строк
def remove_int(values_list, num):
    result = []
    for elem in values_list:
        if elem != num:
            result.append(elem)
    return result


print(remove_int(['dfd', 58, 'aaa', 'aaa', 'aaa'], 'aaa'))


# посложнее
def remove_int(values_list, num):
    return [elem for elem in values_list if elem != num]


print(remove_int(['dfd', 58, 58, 58, 'aaa'], 58))
