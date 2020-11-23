""" Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
 которые не меньше медианы, в другой — не больше медианы.

"""


import random


def search_med(data):

    def search_median(data, i=0, j=None):
        if j is None:
            j = len(data) - 1
        if data[j] < data[i]:
            data[i], data[j] = data[j], data[i]
        if j - i > 1:
            t = (j - i + 1) // 3
            search_median(data, i, j - t)
            search_median(data, i + t, j)
            search_median(data, i, j - t)
        return data

    return search_median(data, 0, len(data) - 1)



m = 2
list_for_sort = [random.randint(-100, 100) for _ in range(2*m + 1)]

print('Массив до сортировки')
print(list_for_sort)
search_med(list_for_sort)
print('Массив после сортировки')
print(list_for_sort)
print(f'Медиана {list_for_sort[len(list_for_sort) // 2]}')