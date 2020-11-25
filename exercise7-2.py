# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        print(f'Суммарный расход затраченной ткани равна: '
              f'{round((self.param / 6.5 + 0.5) + (other.param * 2 + 0.3), 2)}')

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __str__(self):
        return f'Для пошива пальто нужно: {self.consumption} ткани'

    @property
    def consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __str__(self):
        return f'Для пошива костюма нужно: {self.consumption} ткани'

    @property
    def consumption(self):
        return round(self.param * 2 + 0.3, 2)


coat = Coat(2)
costume = Costume(4)
print(coat)
print(costume)
coat + costume
