# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('exercise5-1_2.txt', 'r', encoding='utf-8') as some_str:
    line = 0
    for i in some_str:
        line += 1
        word = 0
        flag = 0
        for j in i:
            if j != ' ' and flag == 0:
                word += 1
                flag = 1
            elif j == ' ':
                flag = 0
        print(f'{i} {word} сл.')
    print(f'Количество строк: {line}')
