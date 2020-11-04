integer = int(input('Введите целое положительное число: '))
remains = integer % 10

while integer > 0:
    if integer % 10 > remains:
        remains = integer % 10
    integer = integer // 10

print(f'{remains}')
