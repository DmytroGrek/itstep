# Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное
# пользователем. Используйте алгоритм бинарного поиска.
numbers = [1, 8, 15, 35, 3, 89, 25, 10, 7, 41]
numbers.sort()
print(numbers)

while True:
    value = input('Enter your digits or "e" for exit: ').lower()
    if value == 'e':
        break
    try:
        value = int(value)
    except ValueError:
        print('Please input digits or "e"')
        continue

    mid = len(numbers) // 2
    low = 0
    high = len(numbers) - 1

    while numbers[mid] != value and low <= high:
        if value > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value in list")
    else:
        print("ID =", mid)
