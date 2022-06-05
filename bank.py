"""
Задание к уроку 7:

ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

    - создается файл 'account_history.json' для хранения истории операций и остатков по счету;
    остаток на счете хранится в последнем элементе списка, последней строки этого файла
    - для получения остатка из файла написана функция get_account()
    - написана функция initialisation() - для создания файла с начальным остатком == 0
    и историей операций
    - написана функция operation_to_file(str_lst) для добавления в файл новых операций
    - переписаны функции для refill() и buy() для структурного хранения
    информации о движении по счету
    - изменена функция get_report() - отчет выводится в новом формате
    - добавлена библиотека для работы со временем

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.

"""



"""
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

import os

import json

import datetime

def input_positiv():
    """
    функция для корректного ввода положительного целого числа
    получает ввод строки с клавиатуры
    оставлеят только цифровые символы
    просит подтверждение пользователя
    :return: int_plus - введенное положительное целое число.
    """
    repeat_loop = True
    while repeat_loop:
        txt = input('Введите положительное целое число: ').strip()
        # оставляем от введенного текста только цифры
        txt = list(filter(lambda ch: True if (ch in '0123456789') else False, list(txt)))
        txt = ''.join(txt)  # обратное преобразование в строку
        if len(txt) == 0:
            txt = '0'
        int_plus = int(txt)
        invitation = 'Введенное число: ' + str(int_plus) + '   Верно?  да/нет '
        yes = input(invitation).lower()
        if yes == 'да':
            repeat_loop = False

    return int_plus


def get_account():
    """
    функция для получения остатка из файла account_history.json
    :return:
    """
    FILE_NAME = 'account_history.json'
    with open(FILE_NAME, 'r') as f:
        operations = json.load(f)
        # актуальный остаток на счете лежит в последней строке, последнем элементе списка
        accont_value = int(operations[-1][-1])

    return accont_value


def report_string(str_lst):
    """
    Функция формирует строку стандартного печатного отчета об операциях
    :param str_lst: список по меньшей мере из 4 строк
           str_lst[0] - строка - дата и время операции.
                          Если пустая строка, то присваивается текущее время
           str_lst[1] - строка - содержание операции
           str_lst[2] - сумма операции
           str_lst[3] - остаток после совершения операции
    :return: возвращает унифицированную строку отчета по движению средств с полями стандартной ширины
    """

    # фиксированная ширина полей
    STR_LEN = [20, 50, 16, 16]

    # Формирование подстроки с датой и временем
    if len(str_lst[0]) == 0:     # если время не передано, то берем текущее время
        str_lst[0] = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    else:
        str_lst[0] = str(str_lst[0])

    # дополнение/обрезание строки до фиксированной ширины
    for i in range(4):
        if i == 1:    # по левому краю выравниваем текст
            str_lst[i] = str_lst[i].ljust(STR_LEN[i])[:STR_LEN[i]]
        else:         # по правому краю выравниваем цифры и дату
            str_lst[i] = str_lst[i].rjust(STR_LEN[i])[:STR_LEN[i]]

    # формирование итоговой строки
    line_str1 = '-'*(sum(STR_LEN) + 5) + '\n'
    line_str2 = chr(124)
    for i in range(4):
        line_str2 = line_str2 + str_lst[i] + chr(124)
    listing_str = line_str1 +line_str2

    return listing_str


def operation_to_file(str_lst):
   """
   добавляет в файл новую строку с операцией
   :param str_lst: список по меньшей мере из 4 строк
           str_lst[0] - строка - дата и время операции
           str_lst[1] - строка - содержание операции
           str_lst[2] - сумма операции
           str_lst[3] - остаток после совершения операции
   :return:
   """

   FILE_NAME = 'account_history.json'
   # вначале прочитаем весь список списков операций
   with open(FILE_NAME, 'r') as f:
       operations = json.load(f)

   # добавим последнюю переданную в функцию строку
   operations.append(str_lst[:4])

   # перезапишем обратно в файл весь массив
   with open(FILE_NAME, 'w') as f:
       json.dump(operations, f)

   return None


def initialisation():
     """
     функция создает файл 'account_history.data'
     для хранения истории операций и остатков по счету с нулевым остатком
     затем вписывает в файл первую строку с нулевым остатком по счету.
     :return:
     """

     operation =  [
         datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), # дата
         'Открытие счета', # содержание операции
         '0',           # сумма операции
         '0'            # остаток на счету
     ]
     operation_lst = []
     operation_lst.append(operation)

     FILE_NAME = 'account_history.json'

     # инициализация происходит однократно
     if not os.path.exists(FILE_NAME):
         with open(FILE_NAME, 'w') as f:
             json.dump(operation_lst, f)

     return None


def refill():
    """
    Функция пополняет счет
    Перезаписывает файл с историей, обновляет остаток
    """
    # строка для записи в файл
    str_lst = []

    acc = get_account()

    # запросить сумму для внесения на счет
    print('\nТекущий остаток: ', str(acc))
    print('Внесение денежных средств')
    money_refilled = input_positiv()

    # увеличить остаток на счете
    acc += money_refilled

    # сформировать строку отчета
    txt = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')  # дата и время в нулевой элемент списка
    str_lst.append(txt)
    txt = 'Пополнение счета. Внесено ' + str(money_refilled) + ' пиастров.'        # текст: содержание операции
    str_lst.append(txt)
    str_lst.append(str(money_refilled))                          # внесено
    str_lst.append(str(acc))                                     # новый остаток

    print(report_string(str_lst))
    operation_to_file(str_lst)

    return None



def buy():
    """
    Функция оформляет покупки и записывает их в файл
    """

    # строка для записи в файл
    str_lst = []

    acc = get_account()

    print('\nТекущий остаток: ', acc)
    print('Покупка    Введите сумму покупки')

    repeat_loop = True
    while repeat_loop:
        money_to_pay = input_positiv()
        if money_to_pay > acc:
            print('Недостаточно средств. Выберите что-то дешевле или введите \'0\'')
        elif money_to_pay == 0:
            print('Покупка отменена')
            repeat_loop = False
        else:
            repeat_loop = False

    sku = input('Введите название покупки: ')

    acc -= money_to_pay

    # сформировать строку отчета
    txt = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')  # дата и время в нулевой элемент списка
    str_lst.append(txt)
    txt = 'Покупка ' + sku + ' на сумму ' + str(money_to_pay)  + ' пиастров.'  # текст: содержание операции
    str_lst.append(txt)
    str_lst.append(str(money_to_pay * (-1)))  # внесено
    str_lst.append(str(acc))  # новый остаток

    print(report_string(str_lst))
    operation_to_file(str_lst)

    txt = 'Покупка ' + sku + ' на сумму ' + str(money_to_pay) + '. Текущий остаток: ' + str(acc)
    print(txt)

    return None


def get_report():
    """
    Функция печатает отчет о совершенных операциях и состоянии счета.
    """
    print('\nВыписка со счета:')

    FILE_NAME = 'account_history.json'
    # вначале прочитаем весь список списков операций
    with open(FILE_NAME, 'r') as f:
        operations = json.load(f)

    # печать заголовка таблицы
    head = report_string(['Дата и время', 'Содержание операции', 'Сумма операции', 'Остаток на счете'])
    print(head)

    for line in operations:
        print(report_string(line))



def go_out(acc=0, history=[]):
    """
    Функция осуществляет выход
    :param acc: входящий остаток
    :param hist: входящая история
    :return: обновленные  acc, hist
    """
    print('До новых встреч!')
    print('*' * 20)
    return acc, history

def play_bank(account=0, history=[]):
    """
    Модуль "Личный счет"
    Пользователь запускает программу у него на счету 0
    Программа предлагает следующие варианты действий
    1. пополнить счет
    2. покупка
    3. история покупок
    4. выход
    :param account: входящий остаток на счете в банке
    :return None
    """
    # создание файла с историей и остатком на счете = 0  (если его нет)
    initialisation()

    # обрабатываемые выборы пользователя и действия
    valid_choices = {
                    '1': refill,
                    '2': buy,
                    '3': get_report,
                    '4': go_out
                     }

    invitaton = 'Добрый день!\n' \
                'Пожалуйста, выберите действие:\n' \
                '1 - пополнение счета\n'\
                '2 - покупки\n' \
                '3 - история покупок\n' \
                '4 - выход\n'

    # реализация сценария работы пользователя

    print(invitaton)

    repeat_loop = True
    while repeat_loop:
        choice = input('\nВведите номер действия: ')
        if choice in valid_choices.keys():
            f = valid_choices[choice]
            f()
            if choice == '4':
                repeat_loop = False
        else:
            print('Неверный выбор.\nПриходите завтра!')
            repeat_loop = False

    return None

