# Напишіть клас buildingExtended, який буде наслідуваний від building та розширити його тим, що в
# цей клас буде зберігати квартири (екземпляри класа Apartment). Додати методи підрахунку кількості
# квартир, кількості людей, які живуть в будинку та додавання нової квартири з будинку.
from building import Building
from apartment import Apartment


class BuildingExtended(Building):

    def __init__(self,  name, number_floors, height, area, city_name):
        super().__init__(name, number_floors, height, area, city_name)
        self.flats = []   # new_flat,n_f1,n_f2

    def count_flat(self):
        return len(self.flats)

    def count_inhabitants(self):
        res = 0
        for i in self.flats:
            res += int(i.inhabitants)
        return res

    def add_flat(self, number_flat, inhabitants, number_floor, area_flat):
        new_flat = Apartment(number_flat, inhabitants, number_floor, area_flat)
        self.flats.append(new_flat)


if __name__ == "__main__":
    bilding = BuildingExtended('Park Town', '9', '30', '1200', 'Kyiv')
    bilding.add_flat('1', '4', '2', '100')
    bilding.add_flat('15', '3', '7', '72')
    print(bilding.count_flat())
    print(bilding.count_inhabitants())
    bilding_1 = BuildingExtended('Oasis', '16', '50', '3800', 'Lviv')
    bilding_1.add_flat('353', '1', '15', '48')
    bilding_1.add_flat('354', '3', '15', '56')
    bilding_1.add_flat('3554', '4', '15', '80')
    print(bilding_1.count_flat())
    print(bilding_1.count_inhabitants())
