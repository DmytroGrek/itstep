# Напишіть програму, що буде створювати базу користувачів компанії, вам потрібно дати змогу
# додавати користувачів та відображати список всіх доданих. Під час додавання користувача, має бути 5
# основних полів (Прізвище, Ім’я, Посада, Номер телефону та електронна адреса), які вам потрібно
# валідувати за допомогою регулярних виразів і в разі, якщо формат чи дані не відповідають просити ввести їх
# повторно. Підказка. Прізвище та ім’я мають писатися з великої, номер телефону має певну кількість цифр, електронна
# адреса також має свій формат запису, це все потрібно валідувати.

import re
import json


def main():
    data = []
    required_fields = [
        {
            'name': 'first_name',
            'description': 'Please input your first_name, it should starts with Capital letter: ',
            'regexp': r'[A-Z]{1}[a-z]{1,}\b'
        },
        {
            'name': 'last_name',
            'description': 'Please input your last_name, it should starts with Capital letter: ',
            'regexp': r'[A-Z]{1}[a-z]{1,}\b'
        },
        {
            'name': 'position',
            'description': 'Please input your Position: ',
            'regexp': r'^[a-zA-Z\s]{3,}$'
        },
        {
            'name': 'phone_number',
            'description': 'Please input your Phone Number in the format +38 0XX XXX XX XX: ',
            'regexp': r'\+38\s0\d{2}\s\d{3}\s\d{2}\s\d{2}\b'
        },
        {
            'name': 'email',
            'description': 'Please input your Email: ',
            'regexp': r'^([a-z]|[0-9]|\-|\_|\+|\.)+\@([a-z]|[0-9]){2,}\.[a-z]{2,}(\.[a-z]{2,})?$'
        }]

    def validation(regx, value):
        return bool(re.match(regx, value))

    def get_value(meta_field):
        while True:
            value = input(meta_field['description'])
            is_valid = validation(meta_field['regexp'], value)
            if not is_valid:
                continue
            return value

    def add_user():
        user_data = {}
        for meta_field in required_fields:
            value = get_value(meta_field)
            user_data[meta_field['name']] = value
        data.append(user_data)

    def view_data():
        print(json.dumps(data, indent=4))

    def run():
        while True:
            choose = input(
                    "Choose an action to work with the company database:\n"
                    "1 - add company users\n"
                    "2 - show all company users\n"
                    "e - Exit: \n"
                            ).lower()
            if choose == 'e':
                break
            if choose not in ['1', '2']:
                print('Please input digit from 1 to 2')
                continue

            if choose == '1':
                add_user()

            elif choose == '2':
                view_data()

    return run()


main()
