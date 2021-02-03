# Напишіть програму analyze_number.py, користувач вводить число,
# а програма повертає інформацію про число, а саме це парне чи не парне число
# та позитивне чи негативне це число.
user_number = int(input("Enter the integer number \n"))
if user_number % 2 == 0:
    parity_number = "even"
else:
    parity_number = "odd"
if user_number > 0:
    positivity = "positive"
elif user_number < 0:
    positivity = "negative"
else:
    positivity = "its zero"
print(user_number,  positivity, parity_number, "number")
