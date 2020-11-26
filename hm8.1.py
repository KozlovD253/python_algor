import hashlib
"""1) Определение количества различных подстрок с использованием хеш-функции. 
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9"""

def count_subs(user_str=None):
    if user_str is None:
        user_str = str(input('Введите строку для посчета: \n'))

    set_count_subs = set()

    for _start in range(len(user_str)):
        for _end in range (_start + 1, len(user_str) + 1):
            set_count_subs.add(hashlib.md5(bytes(user_str[_start:_end].encode('utf-8'))).hexdigest())

    print(f' Введена строка - {user_str}\n Кол-во подстрок - {len(set_count_subs) - 1}')

count_subs('papa')

count_subs('sova')

count_subs()