# Добавьте к заданию 1 подсчет количества раз, когда
# название фрукта является частью элемента. Например:
# banana, apple, bananamango, mango, strawberry-banana.
# В примере выше banana встречается три раза.
fruit = ('apple', 'apple', 'apricot', 'apple-banana', 'bananaapple')
user = input('Введите фрукт: ').lower()
counter = 0
for i in fruit:
    if user in i:
        counter += 1
print(counter)
