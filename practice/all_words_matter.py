# lesson 7
# Task 1
word_list = "Минздрав, Центр общественного здоровья в сотрудничестве с ВОЗ и " \
            "ЮНИСЕФ уже провели первый этап оценки холодовой цепочки для транспортировки и сохранности вакцин." \
            " Государство способно обеспечить всю логистику." \
            " Для сверхнизких температур государство уже привлекло частную компанию."
l_1 = word_list.split(".")
print(l_1)
print(len(l_1)-1)
l_2 = word_list.count(",")
print(l_2)
l_3 = word_list.count(".")
print(l_3)
# Task 2 with title
l_4 = word_list.title()
print(l_4)
# Task 2 with split, capitalize
word = word_list.split()
text = []
for letter in text:
    t = letter.capitalize()
    text.append(t)
print(*text)
