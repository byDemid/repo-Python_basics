proceeds = int(input('Введите выручку компании в рублях: '))
costs = int(input('Введите издержки компании за тот же период в рублях: '))
profit = proceeds - costs
if proceeds > costs:
    profitability = profit / proceeds * 100
    print(f'Ваша компания приносит прибыль {profit} руб., рентабельность выручки составляет {round(profitability,2)}%')
elif proceeds < costs:
    print(f'Ваша компания терпит убытки: {profit} руб.')
else:
    print(f'Ваша компания работает по нулям')
if profit > 0:
    employees = int(input('Сколько сотрудников работает в вашей фирме? '))
    profit_per_employee = profit / employees
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {round(profit_per_employee,2)} руб.')
