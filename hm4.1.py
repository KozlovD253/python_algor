"""в рамках домашнего задания первых трех уроков.
 Примечание. Идеальным решением будет:
 ● выбрать хорошую задачу, которую имеет смысл оценивать,
 ● написать 3 варианта кода (один у вас уже есть),
 ● проанализировать 3 варианта и выбрать оптимальный,
 ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких
 N вы проводили замеры),
 ● написать общий вывод: какой из трёх вариантов лучше и почему."""

"""Я выбрал задание № 3 из 3 урока, а именно:
 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """
#вывод: Вариант 3 (с сортировкой) показал наименьшее затраты по времени в связи с чем является лучшим вариантом.


from random import randint
from timeit import timeit
import cProfile


def arr_rnd(size):
    array = [randint(0, 100) for _ in range(size)]
    return array


def var_1(sz):
    array = arr_rnd(sz)
    el_min, el_max = 0, 0
    for i in range(len(array)):
        if array[el_min] > array[i]:
            el_min = i
        elif array[el_max] < array[i]:
            el_max = i
    array[el_min], array[el_max] = array[el_max], array[el_min]


print(timeit('var_1(50)', number=100, globals=globals()))  # 0.009482900000000002
print(timeit('var_1(100)', number=100, globals=globals()))  # 0.0250514
print(timeit('var_1(200)', number=100, globals=globals()))  # 0.02798940000000001
print(timeit('var_1(400)', number=100, globals=globals()))  # 0.05765809999999999

cProfile.run('var_1(2000)')

"""          10529 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.005    0.005 hm4.1.py:20(arr_rnd)
        1    0.001    0.001    0.005    0.005 hm4.1.py:21(<listcomp>)
        1    0.000    0.000    0.006    0.006 hm4.1.py:25(var_1)
     2000    0.001    0.000    0.002    0.000 random.py:237(_randbelow_with_getrandbits)
     2000    0.002    0.000    0.004    0.000 random.py:290(randrange)
     2000    0.001    0.000    0.004    0.000 random.py:334(randint)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2522    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

cProfile.run('var_1(4000)')

"""          21039 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
        1    0.000    0.000    0.012    0.012 hm4.1.py:20(arr_rnd)
        1    0.002    0.002    0.012    0.012 hm4.1.py:21(<listcomp>)
        1    0.001    0.001    0.013    0.013 hm4.1.py:25(var_1)
     4000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
     4000    0.004    0.000    0.008    0.000 random.py:290(randrange)
     4000    0.002    0.000    0.010    0.000 random.py:334(randint)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     4000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5032    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

cProfile.run('var_1(8000)')

"""         42163 function calls in 0.029 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.029    0.029 <string>:1(<module>)
        1    0.000    0.000    0.027    0.027 hm4.1.py:20(arr_rnd)
        1    0.004    0.004    0.027    0.027 hm4.1.py:21(<listcomp>)
        1    0.002    0.002    0.028    0.028 hm4.1.py:25(var_1)
     8000    0.007    0.000    0.010    0.000 random.py:237(_randbelow_with_getrandbits)
     8000    0.009    0.000    0.018    0.000 random.py:290(randrange)
     8000    0.005    0.000    0.023    0.000 random.py:334(randint)
        1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     8000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10156    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

cProfile.run('var_1(16000)')

"""          84208 function calls in 0.051 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.051    0.051 <string>:1(<module>)
        1    0.000    0.000    0.047    0.047 hm4.1.py:20(arr_rnd)
        1    0.007    0.007    0.047    0.047 hm4.1.py:21(<listcomp>)
        1    0.003    0.003    0.051    0.051 hm4.1.py:25(var_1)
    16000    0.012    0.000    0.017    0.000 random.py:237(_randbelow_with_getrandbits)
    16000    0.015    0.000    0.032    0.000 random.py:290(randrange)
    16000    0.008    0.000    0.040    0.000 random.py:334(randint)
        1    0.000    0.000    0.051    0.051 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    16000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    20201    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}

"""


# Вариант 2 через минимум и максимум


def var_2(sz):
    array = arr_rnd(sz)
    el_min = min(array)
    array.index(min(array))
    el_max = max(array)
    array.index(max(array))
    array[array.index(max(array))], array[array.index(min(array))] = array[array.index(min(array))], array[
        array.index(max(array))]


print(timeit('var_2(50)', number=100, globals=globals()))  # 0.007067099999999993
print(timeit('var_2(100)', number=100, globals=globals()))  # 0.014665099999999986
print(timeit('var_2(200)', number=100, globals=globals()))  # 0.026297099999999962
print(timeit('var_2(400)', number=100, globals=globals()))  # 0.05633460000000001

cProfile.run('var_2(2000)')
"""          10530 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.006    0.006 hm4.1.py:132(var_2)
        1    0.000    0.000    0.006    0.006 hm4.1.py:20(arr_rnd)
        1    0.001    0.001    0.006    0.006 hm4.1.py:21(<listcomp>)
     2000    0.002    0.000    0.002    0.000 random.py:237(_randbelow_with_getrandbits)
     2000    0.002    0.000    0.004    0.000 random.py:290(randrange)
     2000    0.001    0.000    0.005    0.000 random.py:334(randint)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2510    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""
cProfile.run('var_2(4000)')
"""            21129 function calls in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
        1    0.000    0.000    0.011    0.011 hm4.1.py:132(var_2)
        1    0.000    0.000    0.010    0.010 hm4.1.py:20(arr_rnd)
        1    0.001    0.001    0.010    0.010 hm4.1.py:21(<listcomp>)
     4000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
     4000    0.004    0.000    0.007    0.000 random.py:290(randrange)
     4000    0.002    0.000    0.009    0.000 random.py:334(randint)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     4000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5109    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
cProfile.run('var_2(8000)')
"""               42155 function calls in 0.023 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
        1    0.000    0.000    0.023    0.023 hm4.1.py:132(var_2)
        1    0.000    0.000    0.022    0.022 hm4.1.py:20(arr_rnd)
        1    0.003    0.003    0.022    0.022 hm4.1.py:21(<listcomp>)
     8000    0.006    0.000    0.008    0.000 random.py:237(_randbelow_with_getrandbits)
     8000    0.007    0.000    0.015    0.000 random.py:290(randrange)
     8000    0.004    0.000    0.019    0.000 random.py:334(randint)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     8000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10135    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""
cProfile.run('var_2(16000)')
"""         84376 function calls in 0.047 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.047    0.047 <string>:1(<module>)
        1    0.000    0.000    0.047    0.047 hm4.1.py:132(var_2)
        1    0.000    0.000    0.044    0.044 hm4.1.py:20(arr_rnd)
        1    0.006    0.006    0.044    0.044 hm4.1.py:21(<listcomp>)
    16000    0.011    0.000    0.016    0.000 random.py:237(_randbelow_with_getrandbits)
    16000    0.015    0.000    0.030    0.000 random.py:290(randrange)
    16000    0.007    0.000    0.038    0.000 random.py:334(randint)
        1    0.000    0.000    0.047    0.047 {built-in method builtins.exec}
        4    0.001    0.000    0.001    0.000 {built-in method builtins.max}
        4    0.001    0.000    0.001    0.000 {built-in method builtins.min}
    16000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    20356    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""


# Вариант 3  через сортировку


def var_3(sz):
    array = arr_rnd(sz)
    array.sort()
    array[0], array[-1] = array[-1], array[0]


print(timeit('var_3(50)', number=100, globals=globals()))  # 0.00878420000000002
print(timeit('var_3(100)', number=100, globals=globals()))  # 0.013330400000000076
print(timeit('var_3(200)', number=100, globals=globals()))  # 0.028171199999999952
print(timeit('var_3(400)', number=100, globals=globals()))  # 0.05113630000000002

cProfile.run('var_3(2000)')
"""         10556 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.000    0.000    0.005    0.005 hm4.1.py:20(arr_rnd)
        1    0.001    0.001    0.005    0.005 hm4.1.py:21(<listcomp>)
        1    0.000    0.000    0.005    0.005 hm4.1.py:237(var_3)
     2000    0.001    0.000    0.002    0.000 random.py:237(_randbelow_with_getrandbits)
     2000    0.002    0.000    0.003    0.000 random.py:290(randrange)
     2000    0.001    0.000    0.004    0.000 random.py:334(randint)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2549    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
"""
cProfile.run('var_3(4000)')
"""
         21044 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.000    0.000    0.011    0.011 hm4.1.py:20(arr_rnd)
        1    0.002    0.002    0.011    0.011 hm4.1.py:21(<listcomp>)
        1    0.000    0.000    0.012    0.012 hm4.1.py:237(var_3)
     4000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
     4000    0.004    0.000    0.008    0.000 random.py:290(randrange)
     4000    0.002    0.000    0.010    0.000 random.py:334(randint)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
     4000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5037    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}
"""
cProfile.run('var_3(8000)')
"""
         42186 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.032    0.032 <string>:1(<module>)
        1    0.000    0.000    0.031    0.031 hm4.1.py:20(arr_rnd)
        1    0.004    0.004    0.031    0.031 hm4.1.py:21(<listcomp>)
        1    0.000    0.000    0.032    0.032 hm4.1.py:237(var_3)
     8000    0.008    0.000    0.011    0.000 random.py:237(_randbelow_with_getrandbits)
     8000    0.010    0.000    0.022    0.000 random.py:290(randrange)
     8000    0.005    0.000    0.027    0.000 random.py:334(randint)
        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
     8000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10179    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}"""
cProfile.run('var_3(16000)')
"""         84082 function calls in 0.043 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.043    0.043 <string>:1(<module>)
        1    0.000    0.000    0.041    0.041 hm4.1.py:20(arr_rnd)
        1    0.005    0.005    0.041    0.041 hm4.1.py:21(<listcomp>)
        1    0.000    0.000    0.043    0.043 hm4.1.py:237(var_3)
    16000    0.011    0.000    0.015    0.000 random.py:237(_randbelow_with_getrandbits)
    16000    0.014    0.000    0.028    0.000 random.py:290(randrange)
    16000    0.007    0.000    0.035    0.000 random.py:334(randint)
        1    0.000    0.000    0.043    0.043 {built-in method builtins.exec}
    16000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    20075    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.002    0.002    0.002    0.002 {method 'sort' of 'list' objects}

"""
