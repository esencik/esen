# 1.Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET для удаления дубликатов, возьмите values и проверьте каждый ли элемент доступен для конвертации.
# Создайте список. Проитерируйте values. Если объект в списке можно переконвертировать добавьте True в новый список иначе добавьте False. После, с помощью функции all() скажите можно ли конвертировать values в SET?
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# words = []
#
# for i in values:
#     try:
#         set(i)
#         words.append(True)
#     except TypeError:
#         words.append(False)
#         print(words)
# print(all(words))

#2.Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел.
# num = set()
#
# for i in range(5):
#     try:
#         num1 = int(input("Введите число: "))
#         num.add(num1)
#         if num1 == 0:
#             print("Введите натуральное число")
#         if num1 < 0:
#             print("Число выше чем  0")
#     except ValueError:
#         print("Введите число")
# print("Самое маленькое число это: ", min(num))
#
#3.Представим Вы создали сайт онлайн курсов по Python. Ваша задача спросить у пользователя Python ФУНКЦИЮ и если такая есть исполнить и вернуть пользователю результат иначе сказать что в Python такой функции нет!
# functions = ['all','any','abs','min','eval','reversed','max','slice','round',]
# func = input("Введите функцию : ")
# if func in functions:
#     print('Такая функция есть')
# else:
#     print('Такой функции нету')
#4.Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму займа(не меньше 50 000) и посчитайте сколько нужно будет вернуть если % = 3.47, результат округлите до 2 чисел после точки.
# Формула подсчёта переплаты: Сумма * (% / 100)
# 1

# 1.пишите код где есть TypeError,IndexError,NameError.
# num = input('Введите число: ')
# if num > 5:         # TypeError
#     print('Что то')
#
# list1 = [1, 2, 3, 4]   # IndexError
#
# print(list1[6])
# print(num)            # NameError

# 2.зьмите код #1 и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.
# Code #1:

# #
# try:
#     at = 10
#     in1 = 15
#     wo = 20
#     for e in range(-at, at):
#         print(wo / e)
#     if at > '5':
#         print("at > 5")
# except ZeroDivisionError:
#     print('Делить на ноль нельзя')
#
# 3.ренесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение.
#Code #2:


# lst = []
# for i in range(10):
# lst.apend(i)
#
# a = list(revesed(lst))
# sls_obj = slice('0','8')
# print(а[sls_obj])
#
#
# try:
#     at = 10
#     in1 = 15
#     wo = 20
#     for e in range(-at, at):
#         print(wo / e)
#         if at > 5:
#             print("at > 5")
# except ZeroDivisionError:
#     print('Делить на ноль нельзя')

# 4.ренесите к себе код #3 и исправьте все ошибки, сделайте так чтобы код работал. Если не знаете как исправить ошибку создайте для неё except выражение.
# Code #3:
# a = (0)
# b = (1,)
# numbers = []
# while b > a:
#     numbers += b
#     b += 1
#     print(a, b)

# 1.Дан словарь в котором ключи должны быть только строковыми объектами, но может встретиться Int, как в качестве ключа, но ваша проверка только проверяет на строку и поэтому у вас выходит баг,
# ваша задача обработать исключением ошибку TypeError
#
#    Пример:
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for x in dict_.keys():
# x + 'abc'
# Запустить код
# Обработайте исключение

#dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
#try:
#    for x in dict_.keys():
#        x + 'abc'
#except TypeError:
#   print('У вас ошибка')

















