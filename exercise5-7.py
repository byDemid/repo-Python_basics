# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

firm = 0
sum_profit = 0
firm_list = []
firm_dict = {}
average_dict = {}
with open('exercise5-7.txt', 'r', encoding='utf-8') as some_str:
    for line in some_str:
        line = line.split()
        profit = float(line[2]) - float(line[3])
        print(f'Прибыль компании {line[0]} : {profit} руб.')
        if profit > 0:
            firm += 1
            sum_profit += profit
            firm_dict.update({line[0]: profit})
        else:
            firm_dict.update({line[0]: profit})
    average_profit = sum_profit / firm
    average_dict.update({'average_profit': round(average_profit, 2)})
    firm_list.append(firm_dict)
    firm_list.append(average_dict)

    print(f'Средняя прибыль компаний : {round(average_profit, 2)} руб.')
    print(firm_list)

with open('exercise5-7-0.json', 'w', encoding='utf-8') as f_json:
    json.dump(firm_list, f_json, ensure_ascii=False, indent=4)
