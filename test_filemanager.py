"""
Тестирования функций консольного файлового менеджера
Написать тесты для каждой "чистой" функции
"""

import os

from console_lib import correct_file_name, my_copy

def test_correct_file_name():
    """
    тестирование функциии, correct_file_name(), 'строго' проверяющей имя файла на корректность:
        только маленькие латинские буквы, цифры, '_', '.' без пробелов
        Имя должно начинаться с буквы, не заканчивается символом '.'
        общая длина - не более 16 символов
    """

    test_names = ['america', 'readme.txt', 'Queen', '1asdf', 'qwertyuiopasdfghj', 'index.dat']
    lst_expected = [True, True, False, False, False, True]
    for i in range(len(test_names)):
        assert correct_file_name(test_names[i]) == lst_expected[i], str(''+ test_names[i])

# test_correct_file_name()

"""
Дополнительно* 
попробовать написать тесты для ""грязных"" функций, 
например копирования файла/папки, ...
"""


def test_my_copy():
    """
        тестирование функциии, my_copy() на примере файлов
        """
    # создаем файл qwerty_test.txt
    my_file = open('qwerty_test.txt', 'w+')
    my_file.write('Это файл для тестирования функций работы с файлами')
    my_file.close()

    assert my_copy('qwerty_test.txt', 'ytrewq_test.txt'), 'ошибка копирования файлов'

    # удалить временные файлы
    os.remove('qwerty_test.txt')
    os.remove('ytrewq_test.txt')

# test_my_copy()