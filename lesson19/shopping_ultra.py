# Напишіть програму shopping_ultra.py, що буде надавати можливість додавати нові списки, видаляти
# вже існуючі, знаходити найдорожчий і найдешевший список з покупками, зчитувати дані при першому вході
# з файлу (де дані серіалізовані) та після завершення роботи серіалізувати та зберігати у файл (формат
# серіалізації json). Більше інформації в файлі з практичною за посиланням
import json


def shopping_ultra():
    shopping_list_example = []
    with open('shopping_list.json', 'r') as food:
        shopping_list_example = json.load(food)

    def add_price():
        while True:
            products_price = input('Enter the product price: ')
            try:
                products_price = float(products_price)
                return products_price
            except ValueError:
                print('Please, use numbers')

    def add_new_list():
        products_list = {}
        user_choose = 'y'
        while user_choose == 'y':
            products_name = input('Enter the product name in the new list: ')
            cost = add_price()
            products_list[products_name] = cost
            user_choose = input('Do you want to add more products?: y or n ')
        shopping_list_example.append(products_list)
        print('\nYour list added')
        for idx, val in products_list.items():
            print("{} {}".format(idx, val))

    def delete_list():
        if shopping_list_example:
            print('We have', len(shopping_list_example), 'lists to delete')
            view_list()
            user_choose = input('\nWhich list do you want to delete? ')
            if user_choose.isdigit():
                user_choose = int(user_choose) - 1
                if user_choose in range(0, len(shopping_list_example)):
                    del shopping_list_example[user_choose]
                    print(f'We removed the list at number {user_choose + 1}')
                else:
                    print('You entered the wrong number')
            else:
                print('Please, use numbers')
        else:
            print('The list is empty, nothing to delete')

    def expensive_list(flag=True):
        if shopping_list_example:
            res = []
            for index, val in enumerate(shopping_list_example):
                d = sum(val.values())
                res.append((index + 1, d))
            if flag:
                result = (max(res, key=lambda x: x[1]))
                print('list number {} with value {} is more expensive'.format(result[0], result[1]))
            else:
                result = (min(res, key=lambda x: x[1]))
                print('list number {} with value {} is more cheaper'.format(result[0], result[1]))
        else:
            print('The list is empty')

    def cheaper_list():
        expensive_list(flag=False)

    def view_list():
        if shopping_list_example:
            # print(json.dumps(shopping_list_example, indent=4))
            for index, val in enumerate(shopping_list_example):
                print('\nList № {}:'.format(index + 1))
                for idx, value in val.items():
                    print("{} {}".format(idx, value))
        else:
            print('The list is empty')

    def user_exit():
        with open('shopping_list.json', 'w') as fod:
            json.dump(shopping_list_example, fod, indent=4)
        return

    mapping = {
            'a': add_new_list,
            'd': delete_list,
            'v': view_list,
            'r': expensive_list,
            'p': cheaper_list,
            'e': user_exit
        }

    key = ''
    while key != 'e':
        key = input('\nChoose an action to work with the shopping list:\n'
                    'a - for adding the new list\n'
                    'd - for delete the list\n'
                    'v - for viewing the list\n'
                    'r - for viewing the expensive list\n'
                    'p - for viewing the cheaper list\n'
                    'e - for exit\n'
                    ).lower()

        if key in mapping:
            mapping[key]()
        else:
            print('You are wrong, try again')


shopping_ultra()
