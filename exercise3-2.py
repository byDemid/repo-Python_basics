# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(**kwargs):
    for v in kwargs.values():
        print(v, end=' ')


name = input('Введите Имя: ')
surname = input('Введите Фамилию: ')
year = int(input('Возраст: '))
city = input('Ваш город: ')
email = input('Ваш email: ')
phone = input('Моб.тел: ')

my_func(name=name, surname=surname, year=year, city=city, email=email, phone=phone)
