while True:
    num_pyramid = input("Введіть кількість рядків пірамідки: ")
    if num_pyramid == "exit":
        break
    if num_pyramid.isdigit():
        num_pyramid = int(num_pyramid)
        for i in range(1, num_pyramid * 2, 2):
            line = i * "*"
            print(line.center(num_pyramid * 3))
    else:
        print("Помилка при вводі кількості рядків!!!")
