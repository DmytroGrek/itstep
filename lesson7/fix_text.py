data = input("Enter your text: ")
flag = False
result = ''

for symbol in data:
    if symbol == '.':
        flag = True
    if flag and symbol.isalpha():
        symbol = symbol.upper()
        flag = False
    result += symbol

print(result)
