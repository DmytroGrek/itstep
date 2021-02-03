months_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
               7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
               }
try:
    month = int(input("Введите число от 1 до 12: "))
    print(months_dict[month])
except:
    print("You made a mistake, repeat with numbers from 1 to 12")
