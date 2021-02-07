rainbow_colors = ("RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "PURPLE")
user_color = (input("Введите цвет: ")).upper()
if user_color in rainbow_colors:
    index = rainbow_colors.index(user_color)
    if index != 0:
        print(rainbow_colors[index - 1])
    if index != 6:
        print(rainbow_colors[index + 1])
