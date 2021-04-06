# Напишіть клас Country, що має містити поля: назва країни, назва столиці, континент, кількість населення
# країни, назви міст. Реалізуйте методи для задання значень полів, додайте мінімальну валідацію в методах,
# щоб неможливо було записати не валідні дані в поля класа.
class Country:

    continents = ['Eurasia', 'Africa', 'North America', 'South America', 'Australia', 'Antarctica']

    def __init__(self, country_name):
        self.country_name = country_name
        self.capital_name = None
        self.continent = None
        self.population = None
        self.cities_name = []

    def set_population(self, number):
        if number.isdigit():
            self.population = number
        else:
            print('Please, use digit')

    def set_capital_name(self, name):
        if name.isalpha():
            self.capital_name = name
        else:
            print('Write with a capital letter')

    def set_continent(self, name):
        if name in Country.continents:
            self.continent = name

    def set_cities_name(self, name):
        if name.istitle():
            self.cities_name.append(name)
        else:
            print('Write with a capital letter')


if __name__ == "__main__":
    ua = Country('Ukraine')
    print(ua.country_name)
    ua.set_continent('Eurasia')
    print(ua.continent)
    print(ua.set_continent('sfvvdv'))
    ua.set_capital_name('Kyiv')
    print(ua.capital_name)
    ua.set_cities_name('Lviv')
    ua.set_cities_name('poltava')
    print(ua.cities_name)
    ua.set_population('46000')
    print(ua.population)
    print(ua.set_population('dva'))
