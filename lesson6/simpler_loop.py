# Напишіть програму simpler_loop.py, яка виведе на екран перші 30 чисел,
# які діляться без остачі на 5.Починаючи з нуля.
first_num = 0
for i in range(300):
    if i % 5 == 0:
        first_num += 1
        print(i)
        if first_num == 30:
            break
