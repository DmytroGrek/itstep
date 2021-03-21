# Напишіть функцію calculate_food_basket, яка отримує кошик споживача
# з продуктами та вартістю цих продуктів в умовних одиницях представлену
# у вигляді словника та курс валюти і повертає вартість усіх продуктів по цьому курсу.
def calculate_food_basket(food_basket: dict, exchange_rate: float) -> float:
    result = sum(food_basket.values()) * exchange_rate
    return result


basket_example = {
    'bread': 1.2,
    'milk': 1.6,
    'potato': 0.4,
    'sunflower oil': 2,
    'meat': 2.4
                  }
print(calculate_food_basket(basket_example, 27.5))

# для себя первое решение через "колено"
# def calculate_food_basket(food_basket: dict, exchange_rate: float) -> float:
#     result = []
#     for elem in food_basket:
#         result.append(food_basket[elem])
#     value = sum(result) * exchange_rate
#     return value
#
#
# basket_example = {
#     'bread': 1.2,
#     'milk': 1.6,
#     'potato': 0.4,
#     'sunflower oil': 2,
#     'meat': 2.4
#                   }
# print(calculate_food_basket(basket_example, 27.5))
