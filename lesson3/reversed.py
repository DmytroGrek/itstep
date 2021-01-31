rev_user = input("Введіть будь-які символи: \n")
rev = rev_user [::-1]
print(rev)

# не уверен, что так правильно в "принт" передавать, но работает
rev_user = input("Введіть будь-які символи: \n")
print(rev_user [::-1])


rev_user = input("Введіть будь-які символи: \n")
print(*reversed(rev_user), sep='')
