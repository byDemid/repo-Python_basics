# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите месяц числом: '))
my_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

if month == 12 or month == 1 or month == 2:
    print(my_list[0], my_dict[1])
elif 3 <= month <= 5:
    print(my_list[1], my_dict[2])
elif 6 <= month <= 8:
    print(my_list[2], my_dict[3])
elif 9 <= month <= 11:
    print(my_list[3], my_dict[4])
else:
    print("Такого месяца не существует")
