"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы."""

from random import randint


random_mass = [randint(-100, 99) for _ in range(10)]


def buble_sort(rnd_lst):
    n = 1
    while n < len(rnd_lst):
        for i in range(len(rnd_lst) - 1):
            if rnd_lst[i] < rnd_lst[i + 1]:
                rnd_lst[i], rnd_lst[i + 1] = rnd_lst[i + 1], rnd_lst[i]
        n += 1


print(random_mass)
print('*' * 50)
buble_sort(random_mass)
print(random_mass)

