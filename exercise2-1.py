# 1.Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# Не понял нужно было добавить самому через команду append
# или сразу вписать в список разные типы

# some_list = ['name', 28, 18.5, ['first', 1], True]

some_list = []
some_list.append('name')
some_list.append(28)
some_list.append(18.5)
some_list.append(['first', 1])
some_list.append(True)

print(some_list)

for indx, letter in enumerate(some_list):
    print(f'Индекс {indx}: {letter} = {type(letter)}')
