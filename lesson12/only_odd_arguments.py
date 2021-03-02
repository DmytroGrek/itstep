def only_odd_arguments(func):
    def wrapper(*args):
        flag = True
        for arg in args:
            if arg % 2 == 0:
                flag = False
        if flag:
            return func(*args)
        else:
            print('Please add odd numbers!')
    return wrapper


@only_odd_arguments
def add(a, b):
    return a + b


@only_odd_arguments
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(add(5, 5))
print(multiply(1, 4, 3, 5, 7))
