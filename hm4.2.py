"""2). Написать два алгоритма нахождения i-го по счёту простого числа.
 Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
 Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена»."""
# Решето Эратосфена работает немного быстрее.
from timeit import timeit
import cProfile


def eratosthenes(k):
    step = 1000
    start = 0
    res = []
    sieve = [i for i in range(step)]
    sieve[1] = 0
    while True:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                j = i + i
                while j < len(sieve):
                    sieve[j] = 0
                    j += i
        res.clear()
        res = [i for i in sieve if i != 0]
        if len(res) >= k:
            return res[k-1]
        else:
            start += step
            sieve_app = [i for i in range(start, start + step)]
            sieve.extend(sieve_app)


print(timeit('eratosthenes(10)', number=100, globals=globals())) # 0.0542596
print(timeit('eratosthenes(200)', number=100, globals=globals())) # 0.19814719999999997
print(timeit('eratosthenes(400)', number=100, globals=globals())) # 0.34460070000000004
print(timeit('eratosthenes(800)', number=100, globals=globals())) # 1.6049732

cProfile.run('eratosthenes(1000)')
"""         84645 function calls in 0.042 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
        1    0.028    0.028    0.042    0.042 hm4.2.py:13(eratosthenes)
        1    0.000    0.000    0.000    0.000 hm4.2.py:17(<listcomp>)
        8    0.002    0.000    0.002    0.000 hm4.2.py:27(<listcomp>)
        7    0.000    0.000    0.000    0.000 hm4.2.py:32(<listcomp>)
        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
    84610    0.012    0.000    0.012    0.000 {built-in method builtins.len}
        8    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}"""
cProfile.run('eratosthenes(2000)')
"""      417592 function calls in 0.190 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.190    0.190 <string>:1(<module>)
        1    0.127    0.127    0.190    0.190 hm4.2.py:13(eratosthenes)
        1    0.000    0.000    0.000    0.000 hm4.2.py:17(<listcomp>)
       18    0.008    0.000    0.008    0.000 hm4.2.py:27(<listcomp>)
       17    0.001    0.000    0.001    0.000 hm4.2.py:32(<listcomp>)
        1    0.000    0.000    0.190    0.190 {built-in method builtins.exec}
   417517    0.053    0.000    0.053    0.000 {built-in method builtins.len}
       18    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       17    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

"""
cProfile.run('eratosthenes(4000)')
"""          1868360 function calls in 0.805 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.805    0.805 <string>:1(<module>)
        1    0.545    0.545    0.805    0.805 hm4.2.py:13(eratosthenes)
        1    0.000    0.000    0.000    0.000 hm4.2.py:17(<listcomp>)
       38    0.028    0.001    0.028    0.001 hm4.2.py:27(<listcomp>)
       37    0.002    0.000    0.002    0.000 hm4.2.py:32(<listcomp>)
        1    0.000    0.000    0.805    0.805 {built-in method builtins.exec}
  1868205    0.228    0.000    0.228    0.000 {built-in method builtins.len}
       38    0.001    0.000    0.001    0.000 {method 'clear' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       37    0.001    0.000    0.001    0.000 {method 'extend' of 'list' objects}"""
cProfile.run('eratosthenes(8000)')
"""            8841114 function calls in 3.980 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.980    3.980 <string>:1(<module>)
        1    2.724    2.724    3.980    3.980 hm4.2.py:13(eratosthenes)
        1    0.000    0.000    0.000    0.000 hm4.2.py:17(<listcomp>)
       82    0.127    0.002    0.127    0.002 hm4.2.py:27(<listcomp>)
       81    0.005    0.000    0.005    0.000 hm4.2.py:32(<listcomp>)
        1    0.000    0.000    3.980    3.980 {built-in method builtins.exec}
  8840783    1.120    0.000    1.120    0.000 {built-in method builtins.len}
       82    0.002    0.000    0.002    0.000 {method 'clear' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       81    0.002    0.000    0.002    0.000 {method 'extend' of 'list' objects}
"""


def not_sieve(num):
    lst = [2]
    n = 3
    while num > len(lst):
        for i in lst:
            if n % i == 0:
                break
        else:
            lst.append(n)
        n += 1
    return lst[-1]


print(timeit('not_sieve(100)', number=100, globals=globals())) #0.04362129999999986
print(timeit('not_sieve(200)', number=100, globals=globals())) #0.19322579999999956
print(timeit('not_sieve(400)', number=100, globals=globals())) #0.6645039000000006
print(timeit('not_sieve(800)', number=100, globals=globals())) #2.7042731999999994

cProfile.run('not_sieve(1000)')
"""          8921 function calls in 0.042 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
        1    0.041    0.041    0.042    0.042 hm4.2.py:91(not_sieve)
        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
cProfile.run('not_sieve(2000)')
"""        19391 function calls in 0.166 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.166    0.166 <string>:1(<module>)
        1    0.163    0.163    0.166    0.166 hm4.2.py:91(not_sieve)
        1    0.000    0.000    0.166    0.166 {built-in method builtins.exec}
    17388    0.002    0.000    0.002    0.000 {built-in method builtins.len}
     1999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
cProfile.run('not_sieve(4000)')
"""           41815 function calls in 0.812 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.812    0.812 <string>:1(<module>)
        1    0.801    0.801    0.812    0.812 hm4.2.py:91(not_sieve)
        1    0.000    0.000    0.812    0.812 {built-in method builtins.exec}
    37812    0.006    0.000    0.006    0.000 {built-in method builtins.len}
     3999    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
cProfile.run('not_sieve(8000)')
"""             89801 function calls in 2.883 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.883    2.883 <string>:1(<module>)
        1    2.869    2.869    2.883    2.883 hm4.2.py:91(not_sieve)
        1    0.000    0.000    2.883    2.883 {built-in method builtins.exec}
    81798    0.012    0.000    0.012    0.000 {built-in method builtins.len}
     7999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""