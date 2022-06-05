"""
Урок 7 ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";
7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать)
   и сохранить туда содержимое рабочей директории следующим образом:
   сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.
files: victory.py, bill.py, main.py
dirs: modules, packages

Внесены изменения в функцию


"""


"""
БИБЛИОТЕКА ДЛЯ РАБОТЫ С ФАЙЛАМИ

- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;
- посмотреть только папки
вывод только папок которые находятся в рабочей папке;
- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке;
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
- играть в викторину
запуск игры викторина из предыдущего дз;
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз
(задание учебное, после выхода из программы управлением счетом в главной программе
сумму и историю покупок можно не запоминать);
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/...
или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
- выход
выход из программы.
Так же можно добавить любой другой интересный или полезный функционал по своему желанию
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
"""
import os
import shutil
import sys

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

    if correct_file_name(folder_name):
        if not (os.path.isdir(folder_name)):
            os.mkdir(folder_name)
            success = True
        else:
            print('такая папка \'', folder_name, '\' уже существует.')
    else:
        print('Некорректное имя папки: \'', folder_name, '\'')

    return success


def my_list_dir(path_name=''):
    """
    просмотр содержимого папки path_name
    если не передается имя папки, то возвращается содержимое текущей папки
    вывод всех объектов в рабочей папке
    :param path_name: имя папки, необязательный.
    :return: folders_list - список имен папок и файлов в папке
    """

    # если путь не передан, то возвращаем содержимое текущей папки
    if len(path_name) == 0:
        path_name = os.getcwd()
    return os.listdir(path_name)


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

    only_folders_list = list(filter(lambda f: True if os.path.isdir(f) else False, total_f_list))

    return only_folders_list


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

    only_files_list = list(filter(lambda f: True if os.path.isfile(f) else False, total_f_list))

    return only_files_list


def my_save_list_to_file():
    """
    cоздаёт файл listdir.txt (если он есть то пересоздает)
   и сохраняет в него содержимое рабочей директории следующим образом:
   сначала все файлы, потом все папки

    :return: None
    """
    FILE_NAME = 'listdir.txt'
    txt = 'folders: ' + ', '.join(my_list_only_folders()) +'\n'
    txt = txt + 'files: ' + ', '.join(my_list_only_files())

    with open(FILE_NAME, 'w') as f:
        f.write(txt)

    return None


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

    # Если источник копирования - папка,
    # То просто создаем копию - пустую папку
    if os.path.isdir(src_name):
        my_create_folder(dist_name)  # требования к имени жёстче обычных
        print('Создана пустая папка', dist_name)
        print(my_list_dir())
        success = True
    else:
        # источник - файл
        try:
            shutil.copy(src_name, dist_name)
            print('Копирование завершено')
            print(my_list_dir())
            success = True
        except:
            print('Возникла ошибка. Проверьте корректность введенных имен')

    return success


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
    if len(name) == 0 :
        print()
        print(my_list_dir())     # выводим содержимое текущей папки
        name = input('Введите имя файла/папки для удаления: ')

    # Если удаляемый объект - папка,
    # то удаляем папку вместе с содержимым
    if os.path.isdir(name):
        try:
            shutil.rmtree(name)
            print('Выполнено удаление.')
            print(my_list_dir())
            success = True
        except:
            print('Возникла ошибка. Проверьте корректность введенных имен')
    # и если удаляемый объект -файл, то удаляем файл
    elif os.path.isfile(name):
        try:
            os.remove(name)
            print('Выполнено удаление.')
            print(my_list_dir())
            success = True
        except:
            print('Возникла ошибка. Проверьте корректность введенных имен')

    return success



def my_os_info():
    """
    просмотр информации об операционной системе
    вывести информацию об операционной системе (можно использовать пример из 1-го урока);
    :return: info - текстовая строка
    """
    info = f'My OS is {sys.platform} ({os.name})'
    return info


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
        except:
            print('Возникла ошибка. Проверьте корректность введенного пути')

    return success

def good_buy():

    print('*'*15, 'До новых встреч', '*'*15)

    return '*'*47

# good_buy()

"""
Тестирование функции correct_file_name():
    # test_names = ['america', 'readme.txt', 'Queen', '1asdf', 'qwertyuiopasdfghj', 'index.dat']
    # print('Тестирование функции correct_file_name():')
    # for str in test_names:
    #     print(str, ':', correct_file_name(str))
-------------
Результат работы: 
-------------
Тестирование функции correct_file_name():
america : True
readme.txt : True
Queen : False
1asdf : False
qwertyuiopasdfghj : False
index.dat : True



Тестирование функции my_create_folder()
    # while True:
    #     my_create_folder()

-------------
Результат работы: 
-------------
папки создаются, неверные вводы обрабатываются корректно




Тестирование функции my_list_dir()

    # print(my_list_dir())
-------------
Результат работы: 
-------------
['LICENSE', 'console_lib.py', '.gitignore', 'console_file_manager.py', '.git', '.idea']

    # print(my_list_dir('/Users/nikolayagafonov/Music'))
-------------
Результат работы: 
-------------
['Audio Music Apps', 'Music', '.DS_Store', '.localized', 'Ableton', 'iTunes', 'GarageBand']



Проверка функции my_list_only_folders()
     # print(my_list_only_folders())
-------------
Результат работы: 
-------------
['Test1', 'Test2', '.git', '.idea']


Проверка функции my_list_only_files()
     # print(my_list_only_files())
-------------
Результат работы: 
-------------
['LICENSE', 'console_lib.py', '.gitignore', 'console_file_manager.py']


Проверка функции my_copy() для копирования папок: 
    # my_copy()
-------------
Результат работы: 
--------------
/для существующих имен/

['LICENSE', 'console_lib.py', 'test', 'book.txt', '.gitignore', 'console_file_manager.py', '.git', '.idea']
Введите имя исходного файла/папки: test
Введите имя файла/папки, в который копируем: test1
Создана пустая папка test1
['LICENSE', 'console_lib.py', 'test', 'book.txt', 'test1', '.gitignore', 'console_file_manager.py', '.git', '.idea']

-------------
/для несуществующих имен/
['LICENSE', 'console_lib.py', 'test', 'book.txt', 'test1', '.gitignore', 'console_file_manager.py', '.git', '.idea']
Введите имя исходного файла/папки: Папка
Введите имя файла/папки, в который копируем: тест2
Возникла ошибка. Проверьте корректность введенных имен

-------------
/копирование файла в папку/
['LICENSE', 'console_lib.py', 'test', 'book.txt', 'test1', '.gitignore', 'console_file_manager.py', '.git', '.idea']
Введите имя исходного файла/папки: book.txt
Введите имя файла/папки, в который копируем: test
Копирование завершено
['LICENSE', 'console_lib.py', 'test', 'book.txt', 'test1', '.gitignore', 'console_file_manager.py', '.git', '.idea']
-------------
/копирование файла в файл/
['LICENSE', 'console_lib.py', 'test', 'book.txt', 'test1', '.gitignore', 'console_file_manager.py', '.git', '.idea']
Введите имя исходного файла/папки: book.txt
Введите имя файла/папки, в который копируем: fiction.txt
Копирование завершено
['LICENSE', 'console_lib.py', 'test', 'fiction.txt', 'book.txt', 'test1', '.gitignore', 'console_file_manager.py', '.git', '.idea']




Проверка функции my_delete() для удаления файлов и папок
-------------
Результат работы: 
--------------
/удаление папки c содержимым/
['LICENSE', 'console_lib.py', 'book.txt', 'Test1', 'bank.py', '.gitignore', 'victory.py', 'readme.txt', 'Test2', '.git', 'main.py', '.idea']
Введите имя файла/папки для удаления: Test2
Выполнено удаление.
['LICENSE', 'console_lib.py', 'book.txt', 'Test1', 'bank.py', '.gitignore', 'victory.py', 'readme.txt', '.git', 'main.py', '.idea']
--------------
/удаление файла/
['LICENSE', 'console_lib.py', 'book.txt', 'Test1', 'bank.py', 'rrr.txt', '.gitignore', 'victory.py', 'readme.txt', 'Test2', '.git', 'main.py', '.idea']
Введите имя файла/папки для удаления: rrr.txt
Выполнено удаление.
['LICENSE', 'console_lib.py', 'book.txt', 'Test1', 'bank.py', '.gitignore', 'victory.py', 'readme.txt', 'Test2', '.git', 'main.py', '.idea']





Проверка функции my_os_info()
     # print(my_os_info())
-------------
Результат работы: 
-------------
My OS is darwin (posix)



Проверка функции my_get_username()
     # print(os.path.expanduser('~'))
     # print(my_get_username())
-------------
Результат работы: 
-------------
/Users/nikolayagafonov
nikolayagafonov




Проверка функции my_chdir()
    # my_chdir()
 -------------
Результат работы: 
-------------
 переход по абсолютному адресу:
/Users/nikolayagafonov/Desktop/Python progs/HomeWork_5_1
['LICENSE', 'console_lib.py', 'Test1', '.gitignore', 'console_file_manager.py', 'Test2', '.git', '.idea']
Введите адрес папки для перехода: /Users/nikolayagafonov/Music
/Users/nikolayagafonov/Music

 переход по относительному адресу:
/Users/nikolayagafonov/Desktop/Python progs/HomeWork_5_1
['LICENSE', 'console_lib.py', 'Test1', '.gitignore', 'console_file_manager.py', 'Test2', '.git', '.idea']
Введите адрес папки для перехода: Test2
/Users/nikolayagafonov/Desktop/Python progs/HomeWork_5_1/Test2

переход по ошибочному адресу:
/Users/nikolayagafonov/Desktop/Python progs/HomeWork_5_1
['LICENSE', 'console_lib.py', 'Test1', '.gitignore', 'console_file_manager.py', 'Test2', '.git', '.idea']
Введите адрес папки для перехода: ttt
Возникла ошибка. Проверьте корректность введенного пути
"""
