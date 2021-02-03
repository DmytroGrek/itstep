try:
    user_number = float(input("Enter number: "))
    arithmetic_operation = input("Enter arith.operation: ")
    user_number_1 = float(input("Enter number: "))
    symbol = ("+", "-", "/", "*")
    if arithmetic_operation not in symbol:
        print("Please, enter correct arithmetic operation")
    if arithmetic_operation == "+":
        print(user_number + user_number_1)
    elif arithmetic_operation == "-":
        print(user_number - user_number_1)
    elif arithmetic_operation == "*":
        print(user_number * user_number_1)
    elif arithmetic_operation == "/":
        print(user_number / user_number_1)
except ValueError:
    print("Please use numbers")
except ZeroDivisionError:
    print("Division by zero is not allowed")
