# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

some_list = input('Введите элементы в список через пробел: ').split()
print(some_list)

for i in range(int(len(some_list))):
    if (i != 0) and (i % 2 != 0):
        some_list[i - 1], some_list[i] = some_list[i], some_list[i - 1]
print(some_list)
