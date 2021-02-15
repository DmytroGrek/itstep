data = input('Enter your string: ')
data = data.replace(' ', '')
result = data[::-1]
if result == data:
    print('Palindrome')
else:
    print('not Palindrome')
