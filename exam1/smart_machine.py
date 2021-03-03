user_number = input("Введіть число: ")
try:
    user_number = int(user_number)
    if user_number < 100:
        print(user_number / 10)
    else:
        print(user_number / 20)
except:
    print("Некоректные данные")