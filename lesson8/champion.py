iteration = 1
repeated_amount = []

while True:
    data = input(f'Введіть кількість повторів в підході №{iteration}, або stop для припинення: ')
    if data.lower() == 'stop':
        break
    elif not data.isdecimal():
        print('Помилка вводу даних. Введіть число.')
        continue

    repeated_amount.append(int(data))
    iteration += 1

print(f"Кількість підходів: {len(repeated_amount)}")
print(f"Загальна кількість повторень: {sum(repeated_amount)}")
print(f"Максимальна кількість повторень: {max(repeated_amount or [0])}")
print(f"Мінімальна кількість повторень: {min(repeated_amount or [0])}")
print(f"Средня кількість повторень: {(sum(repeated_amount) / len(repeated_amount)) if repeated_amount else 0}")
