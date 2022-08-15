# ------- 1,2 -------------
# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo)->None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all()->list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
# add, get_all = notebook()
#
# add('get up')
# add('eat')
# add('work')
# add('eat')
# add('sleep')
#
# print(get_all())


# ------- 3 -------------
# def expanded_form(num: int) -> str:
#     st = str(num)
#     zeros = len(st) - 1
#     return ' + '.join(v + '0' * (zeros - i) for i,v in enumerate(st) if v != '0') + f' = {st}'
#
#
# print(expanded_form(111))

# ------- 4 -------------
# создать декоратор который будет считать сколько
# раз была запущена функция и будет выводит это значение после каждого запуска функции

# def decor(func):
#     count = 1
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         print(f'count = {count}')
#         func(*args,*kwargs)
#         print('-'*20)
#         count+=1
#     return inner
#
# @decor
# def func1():
#     print('func1')
#
# @decor
# def func2():
#     print('func2')
#
# func2()
# func1()
# func2()
#
# func2()
#
# func1()
# func2()
# func1()


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

# x = 33294
#
# unpair = 0
# pair = 0
# for i in str(x):
#     if int(i) % 2 == 0:
#         pair += 1
#     else:
#         unpair +=1
# print(f'pair: {pair}, unpair: {unpair}')

