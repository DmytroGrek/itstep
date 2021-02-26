def sum_min_10(list_num, start=0, end=0):
    # print(f'{start} {list_num[start:start+10]} {sum(list_num[start:start+10])}') # для отображения, что происходит
    if start == len(list_num)-10:
        return end
    else:
        if sum(list_num[start:start+10]) < sum(list_num[end:end+10]):
            end = start

        return sum_min_10(list_num, start+1, end)


list_num_1 = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 90, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            91, 92, 93, 94, 95, 96, 97, 98, 99
            ]

print(sum_min_10(list_num_1))
