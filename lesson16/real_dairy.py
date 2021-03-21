# Настав час коли ми вдосконалимо завдання diary до нового рівня.
# В занятті №5 представлений базовий опис, вам потрібно додати можливість
# додавати нові завдання, переглядати та видаляти завдання. Файл з програмою
# назвіть real_diary.py. Примітка. Використання словників в реалізації завдання обов’язкове.

def main():
    week_days = {"1": "monday",
                 "2": "tuesday",
                 "3": "wednesday",
                 "4": "thursday",
                 "5": "friday",
                 "6": "saturday",
                 "7": "sunday"
                 }

    daily_routine = {"monday": ["wash and put away dishes", "wipe down mirrors"],
                     "tuesday": ["sort clothes to keep out", "change air filter"],
                     "wednesday": ["wash windows", "wash out trash can"],
                     "thursday": ["polish wood floors", "clean out dryer vents"],
                     "friday": ["wash rugs", "wash out garbage can"],
                     "saturday": ["go to the cinema"],
                     "sunday": ["at 8 pm meeting with friends"]
                     }

    def see_tasks():
        user_day = input("Enter the day of the week to view tasks:\n").strip().lower()
        week_day = week_days.get(user_day)
        if not week_day:
            if user_day not in daily_routine:
                print("There is no such day of the week!!!\n")
            else:
                if not daily_routine[user_day]:
                    print('No daily task')
                else:
                    print(*daily_routine.get(user_day), sep="\n")
        else:
            if not daily_routine[week_day]:
                print('No daily task')
            else:
                print(*daily_routine.get(week_day), sep="\n")

    def remove_tasks():
        user_day = input("Enter the day of the week to remove tasks:\n").strip().lower()
        week_day = week_days.get(user_day)
        if not week_day:
            if daily_routine.get(user_day):
                daily_routine[user_day] = []
                print(f'We removed tasks from {user_day.capitalize()}')
            else:
                print("There is no such day of the week!!!")
        else:
            daily_routine[week_day] = []
            print(f'We removed tasks from {week_days[user_day].capitalize()} ')

    def add_tasks():
        task = input('Enter what do you want to add:\n')
        task = task.strip().lower()
        user_day = input("Enter the day of the week:\n").strip().lower()
        week_day = week_days.get(user_day)
        if not week_day:
            if daily_routine.get(user_day):
                daily_routine[user_day].append(task)
                print(f'We added {task} to {user_day.capitalize()}')
            else:
                print("There is no such day of the week!!!")
        else:
            daily_routine[week_day].append(task)
            print(f'We added {task} to {week_days[user_day].capitalize()} ')

    def real_dairy():
        while True:
            choose = input(
                    "Choose an action with a diary:\n"
                    "1 - see tasks by day\n"
                    "2 - remove tasks by day\n"
                    "3 - add tasks by day\n"
                    "e - Exit: \n"
                            ).lower()
            if choose == 'e':
                break
            if choose.isdigit():
                choose = int(choose)
                if 1 > choose or choose > 3:
                    print('Please input digit from 1 to 3')
            else:
                print('Please input digit')
                continue

            if choose == 1:
                see_tasks()

            elif choose == 2:
                remove_tasks()

            elif choose == 3:
                add_tasks()

    return real_dairy()


main()
