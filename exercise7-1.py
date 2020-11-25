# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        new_list = []
        for i, element in enumerate(self.matrix):
            list_sum = []
            for j, el in enumerate(element):
                m = 0
                while m == 0:
                    list_sum.append(other[i][j] + el)
                    m = 1
            new_list.append(list_sum)
        self.matrix = new_list


def CreatArray(x, y):
    return [[random.randint(0, 99) for i in range(x)] for j in range(y)]


x, y = map(int, input('Введите количество строк и столбцов в матрице через пробел: ').split())

some_list = (CreatArray(x, y))
some_list_2 = (CreatArray(x, y))
matrix = Matrix(some_list)
print(f' {"-" * 20} Matrix 1 {"-" * 20}')
print(matrix)
print(f' {"-" * 20} Matrix 2 {"-" * 20}')
print('\n'.join('\t'.join(map(str, row)) for row in some_list_2))
print(f' {"-" * 20} sum of matrices {"-" * 20}')
matrix + some_list_2
print(matrix)
