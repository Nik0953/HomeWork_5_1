"""
2. В модуле написать тесты для встроенных функций
filter, map, sorted, а также для функций
из библиотеки math: pi, sqrt, pow, hypot.
"""

import math


def test_filter():
    """
    функция для проверки функции filter()
    """

    # проверка фильтра для списка из числовых значений
    # должны остаться только положительные значения
    lst_initial = [1, 2, -20, 3, -1]
    lst_filtered = list(filter(lambda x: True if x > 0 else False, lst_initial))
    lst_expected = [1, 2, 3]
    assert lst_filtered == lst_expected

    # проверка фильтра для строки
    # в списке должны остаться только цифры
    lst_initial = '1.А2БВ345qwerty'
    lst_filtered = list(filter(lambda x: True if x in '0123456789' else False, lst_initial))
    lst_expected = ['1', '2', '3', '4', '5']
    assert lst_filtered == lst_expected


def test_map():
    """
    функция для проверки функции map()
    """

    # проверка map() для списка из числовых значений
    # элементы должны замениться на свои квадраты
    lst_initial = [1, 2, -20, 3, -1]
    lst_mapped = list(map(lambda x: x ** 2, lst_initial))
    lst_expected = [1, 4, 400, 9, 1]
    assert lst_mapped == lst_expected


def test_sorted():
    """
    функция для проверки функции sorted()
    """

    # проверка сортировки списка из числовых значений
    lst_initial = [1, 2, -20, 3, -1]
    lst_sorted = sorted(lst_initial)
    lst_expected = [-20, -1, 1, 2, 3]
    assert lst_sorted == lst_expected

    # проверка ключа reverse
    lst_initial = [1, 2, -20, 3, -1]
    lst_sorted = sorted(lst_initial, reverse=True)
    lst_expected = [3, 2, 1, -1, -20]
    assert lst_sorted == lst_expected

    # проверка параметра 'key'
    # сортировка слов по длине
    lst_initial = ['may', 'october', 'december', 'april']
    lst_sorted = sorted(lst_initial, key=len)
    lst_expected = ['may', 'april', 'october', 'december']
    assert lst_sorted == lst_expected


def test_pi():
    """
    функция для проверки функции pi пакета math
    """

    const_pi = math.pi
    pi_approx = 3.14159
    delta = const_pi - pi_approx
    assert delta < 1e-5


def test_sqrt():
    """
    функция для проверки функции sqrt() пакета math
    """

    assert math.sqrt(121) == 11.0
    assert math.sqrt(6.25) == 2.5


def test_pow():
    """
    функция для проверки функции sqrt() пакета math
    """

    assert math.pow(3, 3) == 27.0
    assert math.pow(0, 13) == 0


def test_hypot():
    """
    функция для проверки функции hypot() пакета math
    """

    assert math.hypot(3, 4) == 5.0
    assert math.hypot(5, 12) == 13


# test_filter()
# test_map()
# test_sorted()
# test_pi()
# test_sqrt()
# test_pow()
# test_hypot()
