# Напишіть програму equals.py, яка чекає від користувача 2 числа,
# якщо вони рівні вона виводить слово EQUALS.
# Якщо числа різні виводить через пробіл більше число потім менше.
# Якщо користувач вводить невірні дані виводить попередження Am i a Joke to You?

try:
    number_1 = int(input("Введете 1е число: "))
    number_2 = int(input("Введете 2е число: "))
    if number_1 == number_2:
        print("EQUALS")
    elif number_1 > number_2:
        print(number_1, number_2)
    else:
        print(number_2, number_1)
except:
    print("Am i a Joke to You?")
