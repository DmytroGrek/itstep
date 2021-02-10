while True:
    math_num = input("Введіть число: ")
    if math_num == 'exit':
        break
    if math_num.isdigit():
        math_num = int(math_num)
        if math_num != 0:
            for g in range(1, 11):
                k = g * math_num
                print(f"{g} * {math_num} = {k}")
        else:
            print("Число має бути більше 0")
    else:
        print("Помилка при вводі числа!!!")
