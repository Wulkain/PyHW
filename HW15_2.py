"""Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров."""

import argparse
import logging

from HW15_2_subclasses import Bird, Fish, Mammal

FILE = 'hw15_2.log'

logging.basicConfig(filename=FILE, filemode='a', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def pars():
    parser = argparse.ArgumentParser(prog='Задача №2.2 ДЗ 15',
                                     epilog='Пример: Bird, Ласточка, 15',
                                     description=f'Данный модуль служит для создания класса-фабрики. Класс принимает '
                                                 f'три параметра: - тип животного из списка [Bird, Fish, Mammal] '
                                                 f'- название животного '
                                                 f'- уникальные параметры (размах крыла (см) для Bird, глубоководность '
                                                 f'(м) для Fish, скорость передвижения (км/ч) для Mammal). '
                                                 f'Модуль осуществляет запись информации о содержимом каталога '
                                                 f'в файл {FILE}')

    parser.add_argument('-t', '--type', default='Bird', help='тип животного')
    parser.add_argument('-n', '--name', default='Ласточка', help='Название животного')
    parser.add_argument('-u', '--unique', default='20', help='Уникальный параметр для животного')
    args = parser.parse_args()
    return AnimalFabric(args.type, args.name, args.unique).creating_animal()


class AnimalFabric:
    def __init__(self, animal_type: str, name: str, uniq):
        self.animal_type = animal_type
        self.name = name
        self.unique_param = uniq

    def unique(self):
        pass

    def creating_animal(self):
        if self.animal_type not in ('Bird', 'Fish', 'Mammal'):
            logger.error('Параметр --type может быть только (Bird, Fish, Mammal)')
            return

        try:
            int(self.unique_param)
        except ValueError:
            try:
                float(self.unique_param)
            except ValueError:
                logger.error('Параметр --unique может быть только числом')
                return

        logger.info(f'type={self.animal_type}, name={self.name}, unique={self.unique_param}')
        if self.animal_type == 'Bird':
            return Bird(self.name, self.unique_param)
        elif self.animal_type == 'Fish':
            return Fish(self.name, self.unique_param)
        elif self.animal_type == 'Mammal':
            return Mammal(self.name, self.unique_param)


if __name__ == '__main__':
    pars()