"""
Модуль для тестирования функций из банковского модуля 'bank.py'
"""

from bank import get_account, report_string


def test_report_string():
    """
    'чистая'
    функция для тестирования report_string() из bank.py
    """
    str_expected = '-' * 107 + '\n' + '|                 abc|def                                               |             ghi|           12345|'
    assert str_expected == report_string(['abc', 'def', 'ghi', '12345'])


def test_get_account():
    """
    'грязная'
    функция для тестирования get_account() из bank.py
    необходимо из файла 'account_history.json' взять последний текст в двойных кавычках,
    перевести его в int и сравнить его с тем, что возвращает get_account()
    """

    FILE_NAME = 'account_history.json'

    with open(FILE_NAME, 'r') as f:
        txt_in_file = f.read()

    # между последними двумя апострофами находится искомый остаток на счете
    apostr2 = txt_in_file.rfind('\"')
    apostr1 = txt_in_file.rfind('\"', 0,  apostr2)
    acc_from_file = int(txt_in_file[apostr1+1: apostr2])

    # сравниваем полученный остаток с результатом работы функции
    assert acc_from_file == get_account()


# test_report_string()
# test_get_account()
