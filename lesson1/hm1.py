# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# digit = []
# st = 'as 23 fdfdg544'
# print(','.join(i for i in st if i.isdigit()))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################

# st = 'as 23 fdfdg544 34'
# print(','.join(''.join(i if i.isdigit() else ' ' for i in st).split()))

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# print([i.upper() for i in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i**2 for i in range(50) if i%2 != 0])

# function
#
# - створити функцію яка виводить ліст

# def func1 (list):
#     for i in list:
#         print(i)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def nums3 (a,b,c):
#     return max(a,b,c)
# print(nums3(10,2,3))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def maxMin (*args):
#     print(max(args))
#     return min(args)

# - створити функцію яка повертає найбільше число з ліста

# def maxlist (list):
#     return max(list)

# - створити функцію яка повертає найменьше число з ліста

# def minlist (list):
#     return min(list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sumlist(list):
#     return sum(list)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avglist (list):
#     return sum(list) // len(list)


# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
def find_min():
    l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(min(l))

#   - видалити усі дублікати
def del_duplicates ():
    l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(list(set(l)))

#   - замінити кожне 4-те значення на 'X'

# def update():
#     l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print(['X' if (i+1) % 4 ==0 else v for i,v in enumerate(l)])

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(num):
    for i in range(num):
        if i == 0 or i == num-1:
            print('*'*num)
        else:
            print('*' + ' ' * (num-2) + '*')
# square(100)
# 3) вывести табличку множення за допомогою цикла while

def table():
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            res = j * i
            print(f'{res:4}', end='')
            j += 1
        i += 1
        print()


table()
# 4) переробити це завдання під меню

while True:
    print('1 - find_min')
    print('2 - del_duplicates')
    print('3 - square')
    print('4 - table')
    print('0 - exit')

    choice = input("????:")

    if choice == '1':
        find_min()
    elif choice == '2':
        del_duplicates()
    elif choice == '3':
        square(5)
    elif choice == '4':
        table()
    elif choice == '0':
        break
