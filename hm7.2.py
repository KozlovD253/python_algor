"""2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""

import random


def merge_sort(array):

    if len(array) <= 1:
        return array

    left_part = merge_sort(array[:len(array) // 2])
    right_part = merge_sort(array[len(array) // 2:])

    i, j = 0, 0

    while len(left_part) > i and len(right_part) > j:
        if left_part[i] < right_part[j]:
            array[i + j] = left_part[i]
            i += 1
        else:
            array[i + j] = right_part[j]
            j += 1

    while len(left_part) > i:
        array[i + j] = left_part[i]
        i += 1
    while len(right_part) > j:
        array[i + j] = right_part[j]
        j += 1

    return array



sort_list = [random.randint(0, 49) for _ in range(10)]
print(f'не отсортированный список - {sort_list}')
print('*' * 50)
merge_sort(sort_list)
print(f'отсортированный список - {sort_list}')