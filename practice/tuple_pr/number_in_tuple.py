# Есть кортеж с целыми числами. Нужно вывести статистику по количеству цифр в элементах кортежа. Например:
# ■ Одна цифра — 3 элемента;
# ■ Две цифры — 4 элемента;
# ■ Три цифры — 5 элементов.
number = (1, 3, 7, 56, 78, 112, 556, 789, 78, 98, 456, 789)

mapping = {
    1: "Одна цифра",
    2: "Две цифры",
    3: "Три цифры",
    4: "Четыре цифры"
    }

result = {}
number_in_list = list(map(str, number))
print(number_in_list)

for num in number_in_list:
    key = len(num)
    if key not in result:
        result[key] = 1
    else:
        result[key] += 1
for key, value in result.items():
    print(f"{mapping.get(key)} - {value} элемента")
