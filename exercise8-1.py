"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишеки (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class LottoCard:
    def __init__(self, name):
        self.name = name
        self.generate = [i for i in range(1, 91)]
        self.card = [[],
                     [],
                     []]
        for i in self.card:
            count = 1
            while count <= 5:
                # заполнение рандомными значениями:
                i.append(self.generate.pop(random.randint(0, len(self.generate) - 1)))
                count += 1
            i.sort()
            while count <= 9:
                # заполнение рандомно пробелами:
                i.insert(random.randint(0, len(i) - 1), '  ')
                count += 1

    def __str__(self):
        text_card = f'{self.name}: \n' + '\n'.join(
            ['  '.join([self.number_correct(i) for i in a]) for a in self.card]) + '\n'
        return text_card

    @staticmethod
    def number_correct(n):
        # Добавляет пробел перед одиночным символом
        return (' ' + str(n)) if (len(str(n)) < 2) else str(n)


class InputUser:
    # Проверка ввода
    def __init__(self, user_input=None):
        if not user_input:
            while True:
                self.user_input = input('Зачеркнуть цифру? (y/n)\n')
                if self.user_input == 'n' or self.user_input == 'y':
                    break
                else:
                    print('Возможны только значения y или n\n')


class LottoGame:
    def __init__(self, name1, name2):
        self.player1 = name1
        self.player2 = name2
        self.generate = [i for i in range(1, 91)]

    @staticmethod
    def Check(card, lottery_keg):
        # Проверка билета
        result = False
        for string in card:
            for i in range(len(string)):
                if string[i] == lottery_keg:
                    string[i] = '--'
                    result = True
        return result

    @staticmethod
    def amount_numbers(card):
        # Колличество оставшихся номеров в карточке
        count = 0
        for string in card:
            for i in string:
                if str(i).isdigit():
                    count += 1
        return count

    def start(self):
        count = 1
        while count < 91:
            lottery_keg = self.generate.pop(random.randint(0, len(self.generate) - 1))
            print(f'Выпал боченок № {lottery_keg} (осталось - {len(self.generate)})')
            count += 1
            print(self.player1)
            print(self.player2)
            user_answer = InputUser()  # пользовательский ввод
            if self.Check(human_player.card, lottery_keg):
                if user_answer.user_input != 'y':
                    print('Вы проиграли, номер есть в карточке')
                    break
            else:
                if user_answer.user_input != 'n':
                    print('Вы проиграли, такого номера нет в карточке')
                    break
            self.Check(computer_player.card, lottery_keg)
            # Условие победы:
            if self.amount_numbers(human_player.card) == 0:
                print('Победил - ', self.player1)
                break
            elif self.amount_numbers(computer_player.card) == 0:
                print('Победил - ', self.player2)
                break


human_player = LottoCard('Игрок')
computer_player = LottoCard('Компьютер')

game = LottoGame(human_player, computer_player)
game.start()
