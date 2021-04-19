# Напишіть метаклас CustomMeta, який буде додавати до всіх початку назви всіх методів текст method_. І також
# додати новий атрибут class_name який буде зберігати назву класу який створюється, в нижньому регістрі.
class CustomMeta(type):
    def __new__(mcs, class_name, bases, attrs):
        attributes = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                attributes[key] = value
            else:
                attributes['method_' + key] = value
        attributes['class_name'] = class_name.lower()
        return super().__new__(mcs, class_name, bases, attributes)


class Auto(metaclass=CustomMeta):

    def __init__(self):
        self.name = 'name'

    @staticmethod
    def auto1():
        print('Auto1')

    @staticmethod
    def auto2():
        print('Auto2')


if __name__ == "__main__":
    a = Auto()
    print(dir(a))
    print(a.__dict__)
    print(a.class_name)
    a.method_auto1()
    a.method_auto2()
