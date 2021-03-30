# Реалізуйте клас Автомобіль. Необхідно зберігати в полях класу:
# назву моделі, рік випуску, виробник, об’єм двигуна, колір автівки та ціну.
# Реалізуйте окремі доступи до полів атрибутів за допомогою методів.
class Car:

    def __init__(self, model_name, year_car, manufacturer, engine, color, price):
        self.model_name = model_name
        self.year_car = year_car
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def get_model_name(self):
        return self.model_name

    def get_year_car(self):
        return self.year_car

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine(self):
        return self.engine

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def view_info(self):
        print(self.get_model_name(),
              self.get_year_car(),
              self.get_manufacturer(),
              self.get_engine(),
              self.get_color(),
              self.get_price())


auto = Car('CX80', 2015, 'Volvo', '2.5TDI', 'Red', 14500)
auto.view_info()
# варианты для себя, разбирался как работает
# auto.year_car = 2021
# print(auto.year_car)
# print(auto.manufacturer)
# auto.price = 25000
# print(auto.price)
# auto.view_info()
# print(auto.get_year_car())
