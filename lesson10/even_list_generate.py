def even_list_generate(num, number):
    result = []
    for elem in range(num, number + 1):
        if elem % 2 == 0:
            result.append(elem)
    return result
    # return [elem for elem in range(num, number + 1) if elem % 2 == 0]


print(even_list_generate(1, 10))
