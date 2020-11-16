"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
 для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
 и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import defaultdict

firm_dict = defaultdict(list)
average_profit = 0
profit_firm = []
low_profit_firm = []


firms_count = int(input('Введите кол-во компаний:\n'))
firms_names = [input(f'Введите наименование компании {i + 1}: \n') for i in range(firms_count)]
#print(firms_count)
#print(firms_names)

for el in firms_names:
    for i in range(4):
        firm_dict[el].append(int(input(f'Введите прибыль компании {el} за квартал {i + 1}: \n')))
    tmp = sum(firm_dict[el]) / 4
    firm_dict[el].append(tmp)
    average_profit += tmp
average_profit /= firms_count

for key, value in firm_dict.items():
    print(f'Средняя прибыль компании {key} : {value[4]}')
    if value[4] < average_profit:
        low_profit_firm.append(key)
    elif value[4] > average_profit:
        profit_firm.append(key)

print(f' Компания у которой прибыль выше средней: {profit_firm}')
print(f' Компания у которой прибыль меньше средней: {low_profit_firm}')