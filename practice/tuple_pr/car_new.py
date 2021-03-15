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
