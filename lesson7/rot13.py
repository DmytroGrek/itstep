data = input("Enter your text: ")

mapper = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
)
result = ''
for letter in data:
    if letter in mapper[0]:
        index = mapper[0].index(letter)
        result += mapper[1][index]

print(result)
