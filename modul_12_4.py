import logging
from unittest import TestCase
import unittest


class Runner:
    def __init__(self, name, speed=5):
        try:
            name + 'ddd'
        except TypeError:
            logging.error (f'{name} Ошибка ввода имени', exc_info=True)
        else:
            self.name = name
            logging.info (f'{name} :имя введено верно')
        self.distance = 0
        try:
          1/speed
        except :
            logging.error (f'{name} Ошибка ввода скорости', exc_info=True)
        else:
            if speed <0:
                logging.error (f'{name} ошибка ввода скорости', exc_info=True)
            else:
                self.speed=speed
                logging.info (f'{name} ввод скорости выполнен успешно ')



    def run(self):
        self.distance += self.speed * 2


    def walk(self):
        self.distance += self.speed


    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name


    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class RunnerTest(unittest.TestCase):

    def test_run_1(self):
        a = 1
        for par in tur_1.participants:
            try:
                1 / par.speed
            except:
                a = a * 0
            else:
                if par.speed>0:
                    a = a * 1
                else:
                    a = a * 0
        if a != 0:
            logging.info (f'tur_1 "test_run" пройден успешно')
        elif a == 0:
            logging.info (f'tur_1 "test_run" не пройден')
        self.assertFalse (a == 0)


    def test_walk_1(self):
        a = 1
        for par in tur_1.participants:
            try:
                par.name+'rr'
            except:
                a = a * 0
            else:
                a = a * 1
        if a != 0:
            logging.info (f'tur_1 "test_walk" пройден успешно')
        elif a == 0:
            logging.info (f'tur_1 "test_walk" не пройден')
        self.assertFalse (a == 0)


    def test_run_2(self):
        a = 1
        for par in tur_2.participants:
            try:
                1 / par.speed
            except:
                a = a * 0
            else:
                if par.speed > 0:
                    a = a * 1
                else:
                    a = a * 0
        if a != 0:
            logging.info (f'tur_2 "test_run" пройден успешно')
        elif a == 0:
            logging.info (f'tur_2 "test_run" не пройден')
        self.assertFalse (a == 0)


    def test_walk_2(self):
        a = 1
        for par in tur_2.participants:
            try:
                par.name + 'rr'
            except:
                a = a * 0
            else:
                a = a * 1
        if a != 0:
            logging.info (f'tur_2 "test_walk" пройден успешно')
        elif a == 0:
            logging.info (f'tur_2 "test_walk" не пройден')


    def test_run_3(self):
        a = 1
        for par in tur_3.participants:
            try:
                1 / par.speed
            except:
                a = a * 0
            else:
                if par.speed > 0:
                    a = a * 1
                else:
                    a = a * 0
        if a != 0:
            logging.info (f'tur_3 "test_run" пройден успешно')
        elif a == 0:
            logging.info (f'tur_3 "test_run" не пройден')
        self.assertFalse (a == 0)


    def test_walk_3(self):
        a = 1
        for par in tur_3.participants:
            try:
                par.name + 'rr'
            except:
                a = a * 0
            else:
                a = a * 1
        if a != 0:
            logging.info (f'tur_3 "test_walk" пройден успешно')
        elif a == 0:
            logging.info (f'tur_3 "test_walk" не пройден')


logging.basicConfig (level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                         format='%(asctime)s | %(levelname)s | %(message)s')


if __name__=="__main__":
    logging.basicConfig (level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                         format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main ()


first_1 = Runner('Василий', 5)
second_1 = Runner('Анатолий', 7)
third_1= Runner('Григорий', 3)
tur_1 = Tournament (101, second_1, third_1, first_1)


first_2 = Runner(123, 5)
second_2 = Runner('Толя', '7')
third_2= Runner('Гриша', 11)
tur_2= Tournament (101, second_2, third_2, first_2)


first_3 = Runner('Васюта', 5)
second_3 = Runner('Тоша', 7)
third_3= Runner('Гришуня', -3)
tur_3= Tournament (101, second_3, third_3, first_3)






