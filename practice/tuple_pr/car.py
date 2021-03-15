# Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0
# до N раз). Пользователь вводит с клавиатуры название производителя и слово для замены. Необходимо заменить
# в кортеже все элементы с этим названием на слово для замены. Совпадение по названию должно быть полным.

# сделал сначала так, но решение через индексы не давали покоя...
model_car = ('Opel', 'Bugatti', 'Bentley', 'Ferrari', 'Lamborghini', 'Maserati', 'Opel', 'Porsche', 'Opel')
user_model = input("Enter your model: ").title()
user_model_change = input("Enter replacement model: ").title()
model_car1 = list(model_car)
if user_model in model_car:
    for elem in model_car1:
        index = model_car1.index(elem)
        if model_car1[index] == user_model:
            model_car1[index] = user_model_change
else:
    print("We don't have such a model")
model_car1 = tuple(model_car1)
print(model_car1)

# с утра решил переделать ...
model_car = ('Opel', 'Bugatti', 'Bentley', 'Ferrari', 'Lamborghini', 'Maserati', 'Opel', 'Porsche', 'Opel')
user_model = input("Enter your model: ").title()
user_model_change = input("Enter replacement model: ").title()
model_car1 = list(model_car)
if user_model in model_car:
    res = [elem.replace(user_model, user_model_change) for elem in model_car1]
    res = tuple(res)
    print(res)
else:
    print("We don't have such a model")

# оставляю для себя, начинаю писать код как ниже, а потом переделываю в List comprehensions
# res = []
# for elem in model_car1:
#     h = elem.replace(user_model, user_model_change)
#     res.append(h)
# print(res)