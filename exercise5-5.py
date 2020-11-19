# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

res = 0
with open('exercise5-5.txt', 'w+', encoding='utf-8') as some_str:
    some_str.write(input('Введите числа через пробел: '))
    some_str.seek(0)
    numbers = some_str.read().split()
    for i in range(len(numbers)):
        res += float(numbers[i])
    print(res)
