#1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1bYgYC0YFqDtxRysbW0ZIoT7w2wDNxruX/view?usp=sharing


n = int(input('Введите трехзначное число: \n'))

a = n // 100
b = (n // 10) % 10
c = n % 10
sum = a + b + c
prod = a * b * c

print (f'Ваше число - {n}')
print (f'Сумма Вашего числа: {sum}')
print (f'Произведение Вашего числа: {prod}')