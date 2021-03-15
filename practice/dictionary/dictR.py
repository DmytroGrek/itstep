# Ми продовжуємо допомагати нашим фанатам подорожувати і створимо для них автоматизацію
# для записування країни та столиці країни. Потрібно реалізувати можливість додавати
# нові країни з столицями, робити пошук по назві міста чи країни, навіть в разі неповного
# введення та видалення.
# Choose action
# 1 - add new Country -> Capital pair
# 2 - remove pair
# 3 - find info
#
# Enter number:
# 3
# Enter full or part of name:
# K
# Founded variants:
# Kazakhstan -> Nur-Sultan
# Ukraine -> Kyiv
# Korea -> Seoul
#
# Enter number:
# 1
# Enter country name:
# France
# Enter capital name:
# Paris
#
# Enter number:
# 2
# Enter country name:
# Franc
# Country not found, enter full name
# France
# We remove France -> Paris pair

def main():
    country_dict = {'france': 'paris', 'poland': 'warsaw', 'germany': 'berlin', 'egypt': 'cairo'}

    def add_country():
        country = input('Enter country name:\n')
        capital = input('Enter capital name:\n')
        country = country.strip().lower()
        country_dict[country] = capital.strip().lower()
        print(country_dict)

    def remove_pair():
        message = 'Enter country name to remove:\n'
        count = 0
        while True:
            country_name = input(message)
            country_name = country_name.strip().lower()

            if country_name in country_dict:
                print(f"We remove {country_name.capitalize()} -> {country_dict[country_name].capitalize()}")
                del country_dict[country_name]
                print(country_dict)
                break
            else:
                if count == 1:
                    print('Country not found')
                    break
                count += 1
                print('Country not found')
                message = 'Enter full country name to remove:\n'

    def country_find():
        country = input('Enter full or part of name:\n')
        country = country.strip().lower()
        result = {}

        for key, value in country_dict.items():
            if key.startswith(country) or value.startswith(country):
                result[key] = value

        if result:
            print('Found variants:')
            for i in result:
                print(f"{i.capitalize()} -> {result[i].capitalize()}")
        else:
            print("Sorry, no result found")

    def run():
        while True:
            choose = input(
                    "Choose action:\n"
                    "1 - add new Country -> Capital pair\n"
                    "2 - remove pair\n"
                    "3 - find info\n"
                    "4 - show all\n"
                    "e - Exit: \n"
                            ).lower()
            if choose == 'e':
                break
            if choose.isdigit():
                choose = int(choose)
                if 1 > choose or choose > 4:
                    print('Please input digit from 1 to 4')
            else:
                print('Please input digit')
                continue

            if choose == 1:
                add_country()

            elif choose == 2:
                remove_pair()

            elif choose == 3:
                country_find()

            elif choose == 4:
                print(country_dict)

    return run()


main()
