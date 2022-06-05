"""
Тестирования функций консольного файлового менеджера
Написать тесты для каждой "чистой" функции
"""

import os

from console_lib import correct_file_name, my_copy, my_save_list_to_file


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


def test_my_save_list_to_file():
    """
    тестирование 'грязной' функции my_save_list_to_file()
    убеждаемся, что имени тестового файла в папке нет,
    читаем записанное в файл исходное состояние директории,
    создаем новый тестовый файл,
    вновь читаем из файла состояние директории, убеждаемся,
    что имя тестового файла теперь в тексте есть,
    удаляем тестовый файл

    """
    TEST_FILE_NAME = 'zyx999.tst'
    REPORT_FILE_NAME = 'listdir.txt'

    # если тестовый файл уже есть, надо вначале его удалить.
    if os.path.exists(TEST_FILE_NAME):
        os.remove(TEST_FILE_NAME)

    # читаем исходное состояние директории
    lst_before = os.listdir()
    # проверяем, что тестового файла в директории нет
    txt = 'На начало тестирования не удаен тестовый файл ' + TEST_FILE_NAME
    assert not (TEST_FILE_NAME in lst_before), txt

    my_save_list_to_file()      # формируем отчетный файл 'listdir.txt'
    # имени TEST_FILE_NAME == 'zyx999.tst' там пока не должно быть

    # проверяем, что имени тестового файла в отчетном файле нет
    with open(REPORT_FILE_NAME, 'r') as f:
        txt_in_file = f.read()
        txt = 'в файле' + TEST_FILE_NAME + ' содержится неверный текст'
        assert not (TEST_FILE_NAME in txt_in_file), txt

    # теперь создаем файл TEST_FILE_NAME == 'zyx999.tst',
    # и он должен оказаться в отчетном файле REPORT_FILE_NAME == 'listdir.txt'

    with open(TEST_FILE_NAME, 'w') as f:
        f.write('Это тестовый файл, который должен быть удален после окончания тестирования.')

    my_save_list_to_file()  # формируем отчетный файл 'listdir.txt'
    # тепеть имя TEST_FILE_NAME == 'zyx999.tst' там должно быть
    # проверяем
    with open(REPORT_FILE_NAME, 'r') as f:
        txt_in_file = f.read()
        txt = 'в файле' + TEST_FILE_NAME + ' содержится неверный текст'
        assert TEST_FILE_NAME in txt_in_file, txt

    # удаляем тестовый файл перед выходом из функции
    if os.path.exists(TEST_FILE_NAME):
        os.remove(TEST_FILE_NAME)


# test_my_save_list_to_file()
