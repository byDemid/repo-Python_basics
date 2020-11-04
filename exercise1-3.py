# Знаю что так нельзя называть переменную. Но в данной задачке так понятней решение
n = str(input('Введите число: '))
nn = n + n
nnn = nn + n
sum_n = int(n) + int(nn) + int(nnn)
print(f'{n}+{nn}+{nnn}={sum_n}')
