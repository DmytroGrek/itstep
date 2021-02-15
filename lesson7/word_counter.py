data = input("Enter your text: ")
result = 0

for word in data.split():
    for symbol in word:
        if symbol.isalpha():
            result += 1
            break

print(f'{result} words in text')
