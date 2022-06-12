import os
import shutil
import sys
import datetime

"""
Урок 8

0. В проекте ""Консольный файловый менеджер"" перейти на новую ветку для добавления нового функционала;
1. Где это возможно переписать код с использованием генераторов и тернарных операторов;
2. Там где возможны исключительные ситуации добавить обработку исключений;
3. *Где это возможно применить декораторы.
Иногда может быть так, что применить новые возможности негде, особенно декораторы - это нормально.


Внесены изменения:
    строка 36 -  функция-декоратор
    строка 59 -  тернарный оператор
    строка 104 - переписана функция my_create_folder() - обработка исключений
    строка 163 - тернарный оператор
    строка 167 - переписана функция my_list_dir() - обработка исключений
    строка 192 - генератор списков
    строка 271 - переписана функция my_copy() - обработка исключений
    строка 305 - переписана функция my_delete() - обработка исключений

"""


"""

БИБЛИОТЕКА ДЛЯ РАБОТЫ С ФАЙЛАМИ

"""



def log_decarator(file_function):
    """
    применяется для всех функций, работающих с файлами в директории,
    сохраняет [добавляет] в файл dir_history.log выполненные команды и их результат
    """

    # inner - итоговая функция с новым поведение

    def inner(*args, **kwargs):
        # Запоминаем время операции
        txt = str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

        # Запоминаем название операции
        txt = txt + ':  ' + file_function.__name__ + '\n'

        # Запоминаем новое состояние директории
        txt = txt +  ', '.join(os.listdir()) + '\n'

        # пишем лог в файл:
        FILE_NAME = 'dir_history.log'
        # если файл уже есть, то добавляем в него, иначе пишем в новый файл
        #   ========   тернарный оператор   ========
        file_attr = 'a' if os.path.exists(FILE_NAME) else 'w'
        with open(FILE_NAME, file_attr) as file_to_write:
            file_to_write.write(txt)

        result = file_function(*args, **kwargs)
        # поведение после вызова
        pass

        return result

    # возвращается функция inner с новым поведением
    return inner


def correct_file_name(name):
    """
    Функция более строгая, чем обычно принято
    Функция проверяет, может ли строка 'name' быть именем файла или папки
        в имени можно использовать маленькие латинские буквы, цифры, '_', '.' без пробелов
        Имя должно начинаться с буквы
        имя не заканчивается символом '.'
        общая длина имени - не более 16 символов

    :name: строка с проверяемым именем
    :return: name_is_correct - boolean - допустима ли переданная строка в качестве имени файла
    """

    # длина более 0 и не более 16 символов
    MAX_NAME_LEN = 16
    name_is_correct: bool = len(name) > 0 and len(name) <= MAX_NAME_LEN

    # первый символ - маленькая буква
    correct_1_symbols = 'abcdefghijklmnopqrstuvwxyz'
    name_is_correct = name_is_correct and (name[0] in correct_1_symbols)

    # последний символ - не точка
    name_is_correct = name_is_correct and (name[-1] != '.')

    # все символы - допустимые
    correct_symbols = correct_1_symbols + '._123456789'
    name_is_correct = name_is_correct and (all(item in correct_symbols for item in name))

    return name_is_correct


@log_decarator
def my_create_folder(folder_name=''):
    """
    создать папку
    если не передается имя папки, то пользователь вводит название папки,
    создаем папку в рабочей директории;
    :folder_name:  имя папки, необязательный.
    Если задан, то папка создается с переданным именем,
    если не задан, то осуществляется запрос ввода с клавиатуры
    :return: success - получилось ли создать папку
    """

    success = False

    # если имя не передано в функцию, запрашиваем ввод пользователя
    if len(folder_name) == 0:
        print('Текущая папка:', os.getcwd())
        folder_name = input('Введите имя новой папки: ')

    # папка создается, если имя корректно и если папки c таким именем еще нет
    #
    # if correct_file_name(folder_name):
    #     if not (os.path.isdir(folder_name)):
    #         os.mkdir(folder_name)
    #         success = True
    #     else:
    #         print('такая папка \'', folder_name, '\' уже существует.')
    # else:
    #     print('Некорректное имя папки: \'', folder_name, '\'')

    try:
        os.mkdir(folder_name)
        success = True
    except FileExistsError:
        print('Ошибка. Объект с таким именем уже существует')
        print('Папка не создана')
    except FileNotFoundError:
        print('Ошибка пути к папке')
        print('Папка не создана')
    except Exception as exc:
        print(' Неизвестная ошибка', exc)
        print('Папка не создана')

    return success


@log_decarator
def my_list_dir(path_name=''):
    """
    просмотр содержимого папки path_name
    если не передается имя папки, то возвращается содержимое текущей папки
    вывод всех объектов в рабочей папке
    :param path_name: имя папки, необязательный.
    :return: folders_list - список имен папок и файлов в папке
    """

    # если путь не передан, то возвращаем содержимое текущей папки
    # if len(path_name) == 0:
    #     path_name = os.getcwd()
    #   ========   тернарный оператор   ========
    path_name = os.getcwd() if len(path_name) == 0 else path_name

    lstdr = None

    try:
        lstdr = os.listdir(path_name)
    except Exception as exc:
        print('Ошибка', exc, 'Не удалось получить содержимое папки', path_name)

    return lstdr


@log_decarator
def my_list_only_folders(path_name=''):
    """
    посмотреть только папки
   если не передается имя папки, то возвращается содержимое текущей папки
    :param path_name: имя папки, необязательный.
    :return: only_folders_list - список имен папок
    """

    # если путь не передан, то смотрим содержимое текущей папки
    if len(path_name) == 0:
        path_name = os.getcwd()

    total_f_list = os.listdir(path_name)

    # only_folders_list = list(filter(lambda f: True if os.path.isdir(f) else False, total_f_list))
    #   =======   генератор списков   =======
    only_folders_list = [f for f in total_f_list if os.path.isdir(f)]

    return only_folders_list


@log_decarator
def my_list_only_files(path_name=''):
    """
    посмотреть только  файлы
    если не передается имя папки, то возвращается содержимое текущей папки
    :param path_name: имя папки, необязательный.
    :return: only_files_list - список имен папок
    """

    # если путь не передан, то смотрим содержимое текущей папки
    if len(path_name) == 0:
        path_name = os.getcwd()

    total_f_list = os.listdir(path_name)

    # only_files_list = list(filter(lambda f: True if os.path.isfile(f) else False, total_f_list))
    #   =======   генератор списков   =======
    only_files_list = [f for f in total_f_list if os.path.isfile(f)]

    return only_files_list


@log_decarator
def my_save_list_to_file():
    """
    cоздаёт файл listdir.txt (если он есть то пересоздает)
   и сохраняет в него содержимое рабочей директории следующим образом:
   сначала все файлы, потом все папки

    :return: возвращает текст, который записан в файл
    """
    FILE_NAME = 'listdir.txt'
    txt = 'folders: ' + ', '.join(my_list_only_folders()) + '\n'
    txt = txt + 'files: ' + ', '.join(my_list_only_files())

    with open(FILE_NAME, 'w') as f:
        f.write(txt)

    return txt


@log_decarator
def my_copy(src_name='', dist_name=''):
    """
    копировать (файл/папку)
    если хотя бы одна из переменных - имён не передается, то
    пользователь вводит и название папки/файла - источника,
    и новое название папки/файла, в который копируется.
    В случае, если источником является не файл, а папка,
    то создаем просто пустую папку с именем dist_name
    Копируем;
    :param src_name: файл/папка источник
    :param dist_name: файл/папка, куда копируется
    :return: success - boolean - успех копирования
    """

    success = False

    # Если хотя бы один из файлов не задан, запрашиваем оба файла/папки:
    if len(src_name) == 0 or len(dist_name) == 0:
        print()
        print(my_list_dir())     # выводим содержимое текущей папки
        src_name = input('Введите имя исходного файла/папки: ')
        dist_name = input('Введите имя файла/папки, в который копируем: ')

    # # Если источник копирования - папка,
    # # То просто создаем копию - пустую папку
    # if os.path.isdir(src_name):
    #     my_create_folder(dist_name)  # требования к имени жёстче обычных
    #     print('Создана пустая папка', dist_name)
    #     print(my_list_dir())
    #     success = True
    # else:
    #     # источник - файл
    try:
        shutil.copy(src_name, dist_name)
        print('Копирование завершено')
        print(my_list_dir())
        success = True
    except FileNotFoundError:
        print('Ошибка имени файла. Копирование не выполнено.')
    except Exception as exc:
        print('Неизвестная ошибка', exc, '. Копирование не выполнено.')
    return success


@log_decarator
def my_delete(name=''):
    """
    удалить (файл/папку)
    если переменная не передается, то
    пользователь вводит название папки/файла
    :param name: файл/папка для удаления
    :return: success - boolean - успех удаления
    """

    success = False

    # Если имя файла не задано, запрашиваем
    if len(name) == 0:
        print()
        print(my_list_dir())     # выводим содержимое текущей папки
        name = input('Введите имя файла/папки для удаления: ')

    # выбираем функцию для удаления
    # узнаём, чем является удаляемый объект 'name': файлом или папкой
    # если 'name' - не файл и не папка , будем печатать диагностику

    if os.path.isdir(name):
        f = shutil.rmtree
    elif os.path.isfile(name):
        f = os.remove
    else:
        print(name, 'не является ни папкой, ни файлом. Удаление не выполнено')
        return False

    try:
        f(name)
        print('Выполнено удаление', name)
        print(my_list_dir())
        success = True
    except Exception as exc:
        print('Возникла ошибка', exc)

    return success


@log_decarator
def my_os_info():
    """
    просмотр информации об операционной системе
    вывести информацию об операционной системе (можно использовать пример из 1-го урока);
    :return: info - текстовая строка
    """
    info = f'My OS is {sys.platform} ({os.name})'
    return info


@log_decarator
def my_get_username():
    """
    возвращает строку с именем пользователя
    :return:
    """
    # получаем путь до папки пользователя
    path = os.path.expanduser('~')
    # очищаем имя пользователя от пути
    slash = path.rfind('/')
    info = path[slash+1:]

    return info


@log_decarator
def my_chdir(path=''):
    """
    смена рабочей директории
    пользователь вводит полный /home/user/...
    или относительный user/my/... путь. 
    Меняем рабочую директорию на ту что ввели и работаем уже в ней;
    :return: success - boolean - успех смены рабочей директории
    """

    success = False

    # если в функцию ничего не передано, запрашиваем ввод пользователя
    if len(path) == 0:
        print(os.getcwd())
        print(my_list_dir())
        path = input('Введите адрес папки для перехода: ')

    # если передан полный путь без ошибок,
    #     переходим в запрошенную папку
    if os.path.exists(path):
        os.chdir(path)
        print(os.getcwd())
        success = True
    else:
        # надеемся, что передан локальный путь
        try:
            os.path.join(os.getcwd(), path)
            os.chdir(path)
            print(os.getcwd())
            success = True
        except Exception as exc:
            print('Возникла ошибка', exc, '. Проверьте корректность введенного пути')

    return success


@log_decarator
def good_buy():

    print('*'*15, 'До новых встреч', '*'*15)

    return '*'*47
