# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    return sum(args) - min(args)


a, b, c = map(int, input('Введите три числа через пробел: ').split())

print(my_func(a, b, c))
