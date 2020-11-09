"""5. В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве.
 Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения."""

from random import randint

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = -20
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = MIN_ITEM
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i
print(f'Максимальный отрицательный элемент {num} находится в ячейке {index}')