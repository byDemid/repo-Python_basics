# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула на {direction}'

    def show_speed(self):
        return f'Скорость : {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if float(self.speed) > 60:
            return f'Скорость превышена на {self.speed - 60} км/ч'
        else:
            return f'Скорость : {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if float(self.speed) > 40:
            return f'Скорость превышена на {self.speed - 40} км/ч'
        else:
            return f'Скорость : {self.speed}'


class PoliceCar(Car):
    pass


town = TownCar(70, 'blue', 'Audi', False)
print(f'{town.go()}, {town.show_speed()}, {town.turn("лево")}, {town.stop()}')
sport = SportCar(170, 'red', 'Mazda', False)
print(f'{sport.go()}, {sport.show_speed()}, {sport.turn("право")}, {sport.stop()}')
work = WorkCar(30, 'red', 'Reno', False)
print(f'{work.go()}, {work.show_speed()}, {work.turn("лево")}, {work.stop()}')
police = PoliceCar(100, 'yellow', 'Kia', True)
print(f'{police.go()}, {police.show_speed()}, {police.turn("лево")}, {police.stop()}')
