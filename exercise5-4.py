# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', }

with open('exercise5-4.txt', 'r', encoding='utf-8') as number_list:
    number_list = number_list.readlines()
number_list_ru = []
for line in number_list:
    word, number = line.split(' — ')
    number_list_ru.append(ru_dict.setdefault(word) + ' — ' + number)
with open('exercise5-4-0.txt', 'w', encoding='utf-8') as new_str:
    new_str.writelines(number_list_ru)
print('Ваши данные, построчно, успешно записаны в файл')
