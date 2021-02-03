# Напишіть програму fizzerbuzzer.py, користувач вводить число в діапазоні від 1 до 100,
# якщо число кратне 3 виводиться слово Fizz, якщо кратне 5 слово Buzz, якщо
# число кратне 3 та 5 одночасно виводить FizzBuzz, якщо жодна з умов не виконується нічого не виводити.
# В разі якщо дані від користувача не валідні (не в потрібному діапазоні або не є числом)
# вивести повідомлення з помилкою.
try:
    user_number = int(input("Введите число от 1 до 100: "))
    if not 1 <= user_number <= 100:
        print("You are out of range")
    elif user_number % 3 == 0 and user_number % 5 == 0:
        print("FizzBuzz")
    elif user_number % 3 == 0:
        print("Fizz")
    elif user_number % 5 == 0:
        print("Buzz")
except ValueError:
    print("Please, enter correct data!")
