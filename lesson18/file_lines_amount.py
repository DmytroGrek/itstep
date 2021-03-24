# Напишіть програму file_lines_amount.py, яка вираховує кількість непорожніх рядків
# в файлі lines.txt, який знаходиться в одній директорії з програмою.
with open('lines.txt', 'r') as f:
    non_blank_lines = sum(not line.isspace() for line in f)
print(non_blank_lines)
