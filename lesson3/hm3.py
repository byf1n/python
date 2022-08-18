# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#   def __init__(self,x,y):
#     self.x = x
#     self.y = y
#     self.array = x * y
#
#   def __add__(self, other):
#     return self.array + other.array
#   def __sub__(self, other):
#     return self.array - other.array
#   def __eq__(self, other):
#     return self.array == other.array
#   def __ne__(self, other):
#     return self.array != other.array
#   def __gt__(self, other):
#     return self.array > other.array
#
#   def __lt__(self, other):
#     return self.array < other.array
#
#   def __len__(self):
#     return self.y*2 + self.x*2
#
#
# rectangle1 = Rectangle(2, 3)
# rectangle2 = Rectangle(10, 20)
#
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 > rectangle2)
# print(rectangle1 < rectangle2)
#
# print(len(rectangle1))

###############################################################################

# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prince(Human):
    def __init__(self, name, age, shoes_size):
        super().__init__(name, age)
        self.shoes_size = shoes_size

    def find_size(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.size == self.shoes_size:
                print(cinderella)
                break


class Cinderella(Human):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return str(self.__dict__)
        # return str(self.__dict__) -- не дуже зрозумів як тут dict працює


cinderellas = [
    Cinderella('boib', 15, 41),
    Cinderella('oleg', 23, 42),
    Cinderella('tania', 27, 43),
    Cinderella('dmitriu', 17, 44)
]

prince = Prince('Bobo', 27, 43)
prince.find_size(cinderellas)
###############################################################################


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)

class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)

# 3) Створити клас Main в якому буде:
class Main:
    printable_list = []

    @classmethod
    def add(cls,new_item):
        if isinstance(new_item, (Book,Magazine)):
            cls.printable_list.append(new_item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
#   класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:
#
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
#
# для
# перевірки
# ксассів
# використовуємо
# метод
# isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
