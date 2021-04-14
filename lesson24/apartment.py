# Реалізуйте клас Apartment, який буде мати властивості номер квартири, кількість жителів квартири,
# поверх та площа квартири. Використайте property, для задання та зміни параметрів.
class Apartment:
    def __init__(self, number_flat, inhabitants, number_floor, area_flat):
        self.number_flat = number_flat
        self.inhabitants = inhabitants
        self.number_floor = number_floor
        self.area_flat = area_flat

    @property
    def number_flat(self):
        return self.__number_flat

    @number_flat.setter
    def number_flat(self, value):
        if value.isdigit():
            self.__number_flat = value
        else:
            raise ValueError('Use digit')

    @number_flat.deleter
    def number_flat(self):
        del self.__number_flat

    @property
    def inhabitants(self):
        return self.__inhabitants

    @inhabitants.setter
    def inhabitants(self, value):
        if value.isdigit():
            self.__inhabitants = value
        else:
            raise ValueError('Use digit')

    @inhabitants.deleter
    def inhabitants(self):
        del self.__inhabitants

    @property
    def number_floor(self):
        return self.__number_floor

    @number_floor.setter
    def number_floor(self, value):
        if value.isdigit():
            self.__number_floor = value
        else:
            raise ValueError('Use digit')

    @number_floor.deleter
    def number_floor(self):
        del self.__number_floor

    @property
    def area_flat(self):
        return self.__area_flat

    @area_flat.setter
    def area_flat(self, value):
        if value.isdigit():
            self.__area_flat = value
        else:
            raise ValueError('Use digit')

    @area_flat.deleter
    def area_flat(self):
        del self.__area_flat
