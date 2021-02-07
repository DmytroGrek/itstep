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
user_day = (input("Введите день недели: ").lower())
week_day = week_days.get(user_day)
if not week_day:
    print(*daily_routine.get(user_day) or ["Нет такого дня недели"], sep="\n")
else:
    print(*daily_routine.get(week_day), sep="\n")
