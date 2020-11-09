""" 1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""


START_NUM = 2
END_NUM = 99
START_RANGE = 2
END_RANGE = 9

for i in range(START_RANGE, END_RANGE, +1):
    number = 0
    for k in range(START_NUM,END_NUM, +1):
        if k % i == 0:
            number += 1
    print(f'числу {i} кратно {number} ')
