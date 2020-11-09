"""6.В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать."""

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

el_min, el_max = 0, 0

for i in range(1, len(array)):
    if array[el_min] > array[i]:
        el_min = i
    elif array[el_max] < array[i]:
        el_max = i

if el_min > el_max:
   el_min, el_max = el_max, el_min

print(f' откуда будем считать {array[el_min]} по {array[el_max]}')

num_sum = 0
for i in range(el_min + 1, el_max):
    num_sum += array[i]
print(f'Сумма числе между мин и макс - {num_sum}')