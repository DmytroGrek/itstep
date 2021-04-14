# Створіть клас building, який має такі властивості, як назва, кількість поверхів, висота будівлі, площа та місто
# де будівля побудована. Реалізуйте валідацію значень через property.
class Building:
    def __init__(self, name: str, number_floors: str, height: str, area: str, city_name: str):
        self.name = name
        self.number_floors = number_floors
        self.height = height
        self.area = area
        self.city_name = city_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.istitle():
            self.__name = value
        else:
            raise ValueError('Name starts with a capital letter')

    @name.deleter
    def name(self):
        del self.__name

    @property
    def number_floors(self):
        return self.__number_floors

    @number_floors.setter
    def number_floors(self, value):
        if value.isdigit():
            self.__number_floors = value
        else:
            raise ValueError('Use digit')

    @number_floors.deleter
    def number_floors(self):
        del self.__number_floors

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            raise ValueError('Use digit')

    @height.deleter
    def height(self):
        del self.__height

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        if value.isdigit():
            self.__area = value
        else:
            raise ValueError('Use digit')

    @area.deleter
    def area(self):
        del self.__area

    @property
    def city_name(self):
        return self.__city_name

    @city_name.setter
    def city_name(self, value):
        if value.istitle():
            self.__city_name = value
        else:
            raise ValueError('Name starts with a capital letter')

    @city_name.deleter
    def city_name(self):
        del self.__city_name
