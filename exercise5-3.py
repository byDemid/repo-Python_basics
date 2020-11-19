# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

sum_wage = 0
with open('exercise5-3.txt', 'r', encoding='utf-8') as some_str:
    some_str = some_str.readlines()
    print('Сотрудники, которые получают оклад менее 20 000')
    for line in some_str:
        surname, money = line.split(' ')
        sum_wage += float(money)
        if float(money) < 20000:
            print(surname)
    print(f'Средняя величина дохода всех сотрудников: {round((sum_wage / len(some_str)), 2)} руб.')
