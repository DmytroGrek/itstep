def bubble_sort(num_list, reverse=False):
    n = len(num_list)
    for i in range(n):
        for j in range(n - i - 1):
            if reverse:
                if num_list[j] < num_list[j + 1]:
                    temp = num_list[j]
                    num_list[j] = num_list[j + 1]
                    num_list[j + 1] = temp
            else:
                if num_list[j] > num_list[j + 1]:
                    temp = num_list[j]
                    num_list[j] = num_list[j + 1]
                    num_list[j + 1] = temp
    return num_list


list_num = [4, 2, 1, 3, 7, 0]
print(bubble_sort(list_num, True))
