# Напишіть реалізацію збереження працівників за допомогою ООП зі завдання 2 Заняття 17. Зберігайте
# інформацію в файл (можете використовувати json)

import re
import json


class InfoStaff:

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
        }
    ]

    def __init__(self):
        self.data = []

    @staticmethod
    def validation(regx, value):
        return bool(re.match(regx, value))

    def get_value(self, meta_field):
        while True:
            value = input(meta_field['description'])
            is_valid = self.validation(meta_field['regexp'], value)
            if not is_valid:
                continue
            return value

    def add_user(self):
        user_data = {}
        for meta_field in self.required_fields:
            value = self.get_value(meta_field)
            user_data[meta_field['name']] = value
        self.data.append(user_data)
        self.user_exit()

    @staticmethod
    def view_data():
        with open('staff_database.json', 'r') as staff:
            view_staff = json.load(staff)
            for index, val in enumerate(view_staff, start=1):
                print('\nEmployee № {}:'.format(index))
                for i in val:
                    print(i + ': ', end='')
                    print(view_staff[index-1][i], end='\n')

    def user_exit(self):
        with open('staff_database.json', 'r') as staff:
            view_staff = json.load(staff)
            view_staff += self.data
        with open('staff_database.json', 'w') as staff:
            json.dump(view_staff, staff, indent=4)

    def run(self):
        mapping = {
            '1': self.add_user,
            '2': self.view_data,
            'e': self.user_exit
        }
        choose = ''
        while choose != 'e':
            choose = input(
                    "Choose an action to work with the company database:\n"
                    "1 - add company users\n"
                    "2 - show all company users\n"
                    "e - Exit: \n"
                            ).lower()

            if choose in mapping:
                mapping[choose]()
            else:
                print('You are wrong, try again')


if __name__ == '__main__':
    main = InfoStaff()
    main.run()
