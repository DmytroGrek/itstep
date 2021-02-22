# по простому
def five_min(*args):
    return min(args)


print(five_min(13, 9, 2, -1, 5))


# с проверкой по типам аргументов
def five_min(*args):
    if all(isinstance(element, (int, float)) for element in args):
        return min(args)
    elif all(isinstance(element, str) for element in args):
        return min(args)
    else:
        print('Mistake, you have different data types!')


print(five_min(13, 9, 2, -1, 5))
print(five_min('13', '5', '7', '2', '0'))
print(five_min('abc', '-1', 'cba', 'qwr', 'lkj'))
print(five_min('abc', -1, 'cba', 7, 'lkj'))
