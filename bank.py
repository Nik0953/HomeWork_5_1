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


def refill(acc, history):
    """
    Функция пополняет счет
    :param acc: входящий остаток
    :param hist: входящая история
    :return: обновленные  acc, hist
    """
    print('\nТекущий остаток: ', str(acc))
    print('Внесение денежных средств')
    money_refilled = input_positiv()
    acc += money_refilled
    txt = 'Внесено ' + str(money_refilled) + '. Текущий остаток: ' + str(acc)
    print(txt)
    history.append(txt)
    return acc, history


def buy(acc, history):
    """
    Функция оформляет покупки
    :param acc: входящий остаток
    :param hist: входящая история
    :return: обновленные  acc, hist
    """
    print('\nТекущий остаток: ', str(acc))
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
    txt = 'Покупка ' + sku + ' на сумму ' + str(money_to_pay) + '. Текущий остаток: ' + str(acc)
    print(txt)
    history.append(txt)
    return acc, history


def get_report(acc, history):
    """
    Функция выдает отчет о совершенных операциях и состоянии счета.
    :param acc: входящий остаток
    :param hist: входящая история
    :return: обновленные  acc, hist
    """
    print('\nВыписка со счета:')
    for h in history:
        print(h)
    return acc, history


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
    :return account: 
    """
    # история операций
    history.append('*' * 8)
    history.append('')
    history.append('Начальный остаток = ' + str(account))

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
            account, history = f(account, history)
            if choice == '4':
                repeat_loop = False
        else:
            print('Неверный выбор.\nПриходите завтра!')
            repeat_loop = False

    return account
