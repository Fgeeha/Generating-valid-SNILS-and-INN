from random import randint
from typing import Tuple, Optional
import random

# Так называемые контрольные числа
control_nums_ul = (2, 4, 10, 3, 5, 9, 4, 6, 8)
control_nums_fl = (
    (7, 2, 4, 10, 3, 5, 9, 4, 6, 8),
    (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8),
)


def get_random_kno() -> str:
    """
    Случайный Код Налогового Органа
    :return: Случайный Код Налогового Органа.
    """
    return str(randint(10000, 19999))[1:]


def get_controls_inn_fl(inn) -> Tuple[str, str]:
    """
    Получить контрольные числа для ИНН Физического лица
    :param inn: ИНН Физического лица.
    :return: Кортеж, содержащий первое и второе контрольные числа.
    """
    inn = inn[:-2] if len(inn) == 12 else inn
    first_control_num = sum([x * int(y) for(x, y) in zip(control_nums_fl[0], inn)]) % 11
    first_control_num = 0 if first_control_num == 10 else first_control_num
    inn += str(first_control_num)
    second_control_num = sum([x * int(y) for(x, y) in zip(control_nums_fl[1], inn)]) % 11
    second_control_num = 0 if second_control_num == 10 else second_control_num
    return str(first_control_num), str(second_control_num)


def get_random_inn_fl(kno: Optional[str] = None) -> str:
    """
    Получить случайный ИНН Физического Лица.

    :param kno: Случайный Код Налогового Органа.
    :return: ИНН Физического Лица.
    """
    if kno is None:
        kno = get_random_kno()
    inn = kno + str(randint(1000000, 1999999))[1:]
    inn += ''.join(get_controls_inn_fl(inn))
    return inn


def get_snils() -> str:
    """
    Генерирует случайный СНИЛС.

    :return: СНИЛС.
    """
    nums = [
        random.randint(0, 9) if x != 3 and x != 7 and x != 11
        else '-' if x == 3 or x == 7
        else ' '
        for x in range(0, 12)
    ]

    cont = nums[0] * 9 + nums[1] * 8 + nums[2] * 7 + nums[4] * 6 + nums[5] * 5 \
        + nums[6] * 4 + nums[8] * 3 + nums[9] * 2 + nums[10] * 1

    if cont in (100, 101):
        cont = '00'
    elif cont > 101:
        cont = cont % 101
        if cont in (100, 101):
            cont = '00'
        elif cont < 10:
            cont = '0' + str(cont)
    elif cont < 10:
        cont = '0' + str(cont)

    nums.append(str(cont))
    return ''.join([str(x) for x in nums])


if __name__ == '__main__':
    print("Снилс    ИНН")
    print(f'{get_random_inn_fl()}  {get_snils()}')
