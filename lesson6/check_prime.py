# Напишіть програму check_prime.py, що у відповідь на введене число
# користувачем дасть відповідь чи число просте.
while True:
    prime_num = (input("Введіть натуральне число більше 1: "))
    if prime_num == 'exit':
        break
    if prime_num.isdigit():
        prime_num = int(prime_num)
        if prime_num > 1:
            count = 0
            for g in range(1, prime_num + 1):
                if prime_num % g == 0:
                    count += 1
            if count == 2:
                print("просте")
            else:
                print("непросте")
        else:
            print("Число має бути більше 1")
    else:
        print("Помилка при вводі числа!!!")
