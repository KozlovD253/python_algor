""" 2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

# https://drive.google.com/file/d/1bYgYC0YFqDtxRysbW0ZIoT7w2wDNxruX/view?usp=sharing

user_num = int(input('Введите число: \n'))

def even_or_odd(num, even = 0, odd = 0):
    if num < 1:
        return even,odd
    else:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_or_odd(num // 10, even, odd)


even_count, odd_count = even_or_odd(user_num)
print(f'Четных цифр в числе {even_count}, нечетных {odd_count}.')