""" 5.Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
 Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

a = 1
symb = ''
for i in range(32, 128):
    if a > 9:
        symb = '\n'
        a = 0
    print(f'{i}:{chr(i)} ', end=symb)
    symb = ''
    a += 1