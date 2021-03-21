# Продовжимо працювати із даними з попереднього завдання, на цей раз
# ми допоможемо людям швидко перевіряти, що найдорожче в кошику, а що
# найдешевше. Вам потрібно написати функцію, яка буде повертати множину (set)
# з назвами найдешевших чи найдорожчих продуктів, може виникнути питання чому
# множину, а все через те що в категорію най може потрапити декілька продуктів.
# Функція приймає словник з кошиком, а також прапорець bool типу, який вказує на
# те найдорожчі чи найдешевші шукати.

def find_most_in_food_basket(food_basket: dict, max_cost=True) -> set:
    res = []
    for key in food_basket:
        if max_cost:
            result = max(food_basket.values())
        else:
            result = min(food_basket.values())
        if food_basket[key] == result:
            res.append(key)
    return set(res)


big_basket = {
    'bread': 1.2,
    'milk': 1.6,
    'potato': 0.4,
    'sunflower oil': 2,
    'meat': 2.4,
    'eggs': 0.4,
    'fish': 2.4
                }
print(find_most_in_food_basket(big_basket))
print(find_most_in_food_basket(big_basket, max_cost=False))
