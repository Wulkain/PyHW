"""Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров."""

import argparse
import datetime
import logging

FILE = 'hw15_1.log'
MIN_DATE = 1
MAX_YEAR = 9999
MAX_MONTH = 12
MAX_DAY = 31

logging.basicConfig(filename=FILE, filemode='a', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def pars():
    parser = argparse.ArgumentParser(prog='Задача №2.1 ДЗ 15',
                                     epilog='Примеры: 03.07.2023 -> True, 29.02.2020 -> True, 29.02.2021 -> False',
                                     description=f'Данный модуль получает на вход дату в формате DD.MM.YYYY, '
                                                 f'возвращает истину, если дата может существовать '
                                                 f'или ложь, если такая дата невозможна. Модуль осуществляет запись '
                                                 f'информации о содержимом каталога в файл {FILE}')

    parser.add_argument('-d', '--date',
                        default=f'{datetime.datetime.now().day}'
                                f'.{datetime.datetime.now().month}'
                                f'.{datetime.datetime.now().year}',
                        help='Дата в формате DD.MM.YYYY')
    arg = parser.parse_args()
    return is_real_date(arg.date)


def is_real_date(date: str) -> bool | None:
    try:
        day, month, year = map(int, date.split('.'))
    except ValueError:
        logger.error(f'{date} - неверный формат!')
        return

    if (not(MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <= day <= MAX_DAY)) \
            or (month in (4, 6, 9, 11) and day > 30) \
            or (month == 2 and _is_leap_year(year) and day > 29) \
            or (month == 2 and not _is_leap_year(year) and day > 28):
        inf = f'Дата {date} невозможна!'
        is_real = False
    else:
        inf = f'Дата {date} существует'
        is_real = True
    logger.info(f'{inf}, {is_real}')
    return is_real


def _is_leap_year(year: int) -> bool:
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


if __name__ == '__main__':
    pars()