# Напишіть клас myrange, який буде являтися власною реалізацію range. Клас при ініціалізації приймає число
# до якого сформувати послідовність та крок, з яким його робити. Можете не враховувати варіанти з від’ємними числами.
# В реалізації вам допоможуть ітератори та __next__.
class Myrange:
    def __init__(self, num, step):
        self.num = num
        self.step = step
        self.next = 0

    def __next__(self):
        if self.next >= self.num:
            raise StopIteration
        next_digit = self.next
        self.next += self.step
        return next_digit

    def __iter__(self):
        result = []
        digit = 0
        while digit <= self.num:
            result.append(digit)
            digit += self.step
        return iter(result)


if __name__ == "__main__":
    custom_range = Myrange(15, 2)
    print(next(custom_range))
    print(next(custom_range))
    print(next(custom_range))
    print(next(custom_range))
    for i in custom_range:
        print(i, end=' ')
