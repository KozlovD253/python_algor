"""Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный;

● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
 Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему. """

# Была выбрана задача из 3 урока под номером 1:
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


from sys import getsizeof

START_NUM = 2
END_NUM = 99
START_RANGE = 2
END_RANGE = 9


def var_1():
    for i in range(START_RANGE, END_RANGE, +1):
        number = 0
        for k in range(START_NUM, END_NUM, +1):
            if k % i == 0:
                number += 1
    return locals()


def var_2():
    result = {}
    dividers_dict = {n: n * 0 for n in range(START_RANGE, END_RANGE + 1)}

    for i in range(START_NUM, END_NUM + 1):
        for key, val in dividers_dict.items():
            if i % key == 0:
                dividers_dict[key] += 1

    for key, val in dividers_dict.items():
        result[key] = val
    return locals()


def var_3():
    result = ''
    end_str = ''
    count = 0
    for i in range(START_RANGE, END_RANGE + 1):
        for k in range(START_NUM, END_NUM + 1):
            if k % i == 0:
                count += 1
        if i == END_RANGE:
            end_str = ''
        result = f'{result}{i}: {count}{end_str}'
        count = 0

    return locals()


def mem_count(x,mem_size=0):

    mem_size += getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                mem_count(key)
                mem_count(value)
        elif not isinstance(x, str):
            for item in x:
                mem_count(item)
    return mem_size


def local_global_mem_counting(local_global_dict):
    total_mem = 0
    for el in local_global_dict.values():
        total_mem += mem_count(el)
    return total_mem



print(local_global_mem_counting(var_1()))
print(local_global_mem_counting(var_2()))
print(local_global_mem_counting(var_3()))

"""
Windows 64 bit
Python 3.9.0 64 bit
Решение 1 - 84 байт памяти
Решение 2 - 804 байт памяти
Решение 3 - 232 байт памяти

Отлично видно что вариант 1 занимает наименьшее кол-во памяти. )))
"""
