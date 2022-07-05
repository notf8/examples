========================================================================================================================
Классы (формальное описание объекта) - Объектно Ориентиролванное Програмирование
Названия классов пишутся с большой буквы (cammoncase или camelcase - не понятно сказано))
Все классы сохраняются в отдельные питоновские файлы(напримаер: class.py) и затем подключаются к основной программе с помощью
import class - Но в таком случае к ним нужно обращаться через точку: 'class.метод'
Что бы так не делать пишут from class import * (так импортируется вообще все из файла, но это плохой тон)
Лучше указывать какой именно класс испортируешь: from class import Potatoes
class User: # Название класса
    user_name = 'Admin' # В теле находятся статические атрибуты класса
    password = 'qwerty'
    is_banned = False
user1 = User() # присваиваем переменной наш класс. user1(переменная) - это инстанс класса (или экземпляр класса User)
user1.user_name = 'Top' # Что бы добраться до атрибутов просто ставим "." после инстанса и в списке видим атрибуты (как с методами)
Важно!!! Когда мы меняем атрибуты user1, мы меняем только его атрибуты, сам класс остается неизменным
User.user_name = 'Noname' # Что бы изменить атрибут класса, нужно обратиться к самому классу (а не к инстансу)
Важно! Если изменить один из атрибутов экземпляра класса (например user1.user_name = 'Tom'), а потом изменить атрибут самого
класса (User.user_name = 'Nonme') - то имя экзмаляра, которго мы поменяли перед изменением самого класса осианеися тем же
user1.user_name = 'Tom'

Задача 1. Машина Напишите класс Toyota, состоящий из четырёх статических атрибутов. Создайте три экземпляра класса и
каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200
# import random
# class Toyota:
#     color = 'red'
#     price = 1000000
#     max_speed = 200
#     cur_speed = 0
#
#     def info(self): # Метод для вывода инфо о машине
#         print(
#             'Car color: {}\nCar price: {}\nMax speed: {}\nCurrent speed: {}\n'.format(
#                 self.color, self.price, self.max_speed, self.cur_speed
#             )
#         )
#
#     def speed_set(self, speed): # Метод для установки текущей скорости
#         self.cur_speed = speed
#
# car_1 = Toyota()
# car_2 = Toyota()
# car_3 = Toyota()
#
# car_1.cur_speed = random.randrange(0, 200) # Установка текущей скорости с помощью рандома
# car_2.cur_speed = random.randrange(0, 200)
# car_3.cur_speed = random.randrange(0, 200)
#
# car_2.speed_set(150)
# car_2.info()

Задача 2. Однотипные объекты  В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть
четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора
отличаются только частотой. У наушников три характеристики: название производителя, чувствительность и наличие микрофона
Отличие только в наличии микрофона. Переписать код используя классы
# class Monitor:
#     name = 'Samsung'
#     m_matrix = 'VA'
#     m_res = 'WQHD'
#     m_freq = 60
#
# monitor_1 = Monitor()
# monitor_2 = Monitor()
# monitor_2.m_freq = 144
# monitor_3 = Monitor()
# monitor_3.m_freq = 70
# monitor_4 = Monitor
#
# class Headphones:
#     Headphones_name = 'Sony'
#     headphones_sensitivity = 108
#     headphones_micro = True
#
# headphones_1 = Headphones()
# headphones_1.headphones_micro = False
# headphones_2 = Headphones()
# headphones_3 = Headphones()
========================================================================================================================
Матоды класов и агрументы .self
self - это ссылка на сам объект (класс) В других языках .self называется this
функции внутри классов - называются методами классов. Функции могут содержать именованные аргументы и возвращать
значения с помощью Return
Методы бывают: классовые, статитчески и обычны
для вызова классового и статического не нужны объекты: some_classmethod() или some_stat_metod()
А вот для вызова обычного метода класса требуется объект: m = some_classmethod(), при попытке вызвать без объекта выскочит ошибка
(missing 1 required positional argument: 'self')

# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self): # Первым аргументом обязательно должен идти self, т.к. этофункция класса. Саму функцию для класса пишем внутри класса
#         print(
#             'Name: {}\nPassword: {}\nBan_status: {}\nFriends: {}'.format( # Внутри функции так же обращаемся к атрибутам через self.
#                 self.user_name, self.password, self.is_banned, self.friends
#             )
#         )
#
#     def add_friends(self, friend): # Опять же первый аргумент обязательно self, второй тот, который будет передаваться в функцию
#         if isinstance(friend, User): # Тут проверка, является ли friend-атрибутом user_name, другого инстанса класса User
#             self.friends.append(friend.user_name) # Тут уже указываем куда именно добавляем атрибут класса
#             # А раз мы обращаемся за атрибутом к классу, то добавление начинается с self и через точку указываем из какого аргумента берем инфу
#         else:
#             self.friends.append(friend) # Если же это не экземпляр класса User, просто добавляем имя в список(метод так же append)
#
# user1 = User()
# user2 = User()
# user2.user_name = 'Alina'
# user1.add_friends('Bob') # Так просто добавляем имя через функцию
# user1.add_friends(user2) # Для того что бы добавить атрибут с именем другого инстанса, нужно дописать функцию
# user1.print_info() # Что бы использовать функцию класса, обращаемся к ней так же через точку (не через = как в коллекциях.

Задача Покупка дома для семьи
# class Family: # Тут просто определили класс семья
#     surname = 'Common Family'
#     money = 100000
#     have_a_house = False
#
#     def info(self): # Это метод для вывода инфо о семье
#         print(
#           'Family name: {}\nFamily found: {}\nHaving a house: {}\n'.format(
#               self.surname, self.money, self.have_a_house
#           )
#         )
#
#     def earn_money(self, amount): # Это метод для увеличения бюджета семьи
#         self.money += amount # Здесь увеличиваем бюджет семьи прибавля доход
#         print('Earned {} money! Current value {}'.format(amount, self.money))
#
#     def buy_house(self, house_price, discount=0): # А вот это метод для покупки дома
#         house_price -= house_price * discount / 100 # здесь формируем стоимость дома со скидкой (по умолчанию она 0)
#         if self.money >= house_price:
#             self.money -= house_price
#             self.have_a_house = True
#             print('House purchased! Current money: {}\n'.format(self.money))
#         else:
#             print('Not enough money!\n')
#
# my_family = Family()
# my_family.info()
#
# print('Try to buy house')
# my_family.buy_house(10 ** 6) # Тут передаем стоимость дома в функцию
#
# if not my_family.have_a_house: # Проверяем флаг have_a_house = True/False
#     my_family.earn_money(800000) # Тут передаем заработанные деньги, для увеличения бюджета семьи
#     print('Try to buy house again')
#     my_family.buy_house(10 ** 6, 10) # Тут снова передаем стоимость дома в функцию, но уже со скидкой 10%
#
# my_family.info()

Конструктор __init__(магический метод) и работа с несколькими классами
__init__ - это конструктор класса. Вызывается автоматически в момент иницивализации объекта
Один оскласс может состаять из объектов другого класса, при этом методы у каждого свои
# class Employee:
#     citizenship = 'Russion' # Здесь атрибуты статические (константы)
#
#     def __init__(self, name, salary): # В конструкторе мы инициализируем объекты и атрибуты для них? Могут быть именованными
#         self.name = name # Атрибуты в конструкторе называются динамическими, в отличии от статических в классе
#         self.salary = salary
#
#     def info(self):
#         print(
#             'Citizenship: {}\nName: {}\nSalary: {}\n'.format(
#                 self.citizenship, self.name, self.salary
#             )
#         )
#
# emp_1 = Employee('Bob', 10000)
# emp_2 = Employee('Ted', 20000)
# emp_1.info()
# emp_2.info()

Задача Happy Farm грядка/картошка. Есть катрошкеа со следующими хар-ми:
1. Номер картошки в грядке (индекс)
2. Стадия зрелости (стадии: Отсутствует, Росток, Зеленая, Зрелая)
Картошка может:
1. Расти (переходить на следующую стадию созревания)
2. Передавать информацию о своей зрелости
Есть грядка с картошкой, котрая:
1. Содержит список картошки, которая на ней растет
И может:
1. Взращивать кеартошку
2. Передавать информацию о зрелости всей картошки
Садовник:
Передавать информацию о себе
Грядка с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
И он может:
Ухаживать за грядкой.
Собирать с неё урожай (количество картошки ― пустой список).
# class Potato:
#     states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'} #Прописываем в статитку уровни зрелости в словаре
#
#     def __init__(self, index): # Будем передавать индекс картошки
#         self.index = index
#         self.state = 0 # Это индекс зрелости, изначально будет равен нулю
#
#     def grow(self): # Прописываем метод(действие) для роста
#         if self.state < 3: # Проверка нужна, что бы картошка не переросла
#             self.state += 1
#         self.print_state() # И вызываем метод вывода индекса зрелости
#
#     def is_ripe(self): # Метод проверки каждой картошки на зрелость
#         if self.state == 3:
#             return True # т.е. если созрела, возвращаем True
#         return False # Иначе возвращаем False
#
#     def print_state(self): #Выводим индекс зрелости, обращаемся к словарю через класс
#         print('Картошка {} сейчас {}'.format(
#             self.index, Potato.states[self.state] # Обращаемся к словарю states в классе Potato по ключу из метода grow
#         ))
#
#
# class PotatoGarden:
#
#     def __init__(self, count): # Формируем список картошки на грядке
#         self.potatoes = [Potato(index) for index in range(1, count + 1)] # Список будет генерироваться с использованием
#         # экземпляров другого класса
#
#     def grow_all(self): # Прописываем метод, который взращивает всю картошку на грядке
#         print('Картошка прорастает!')
#         for i_Potato in self.potatoes: # Проходимся по списку картошки и вызываем для каждой метод grow
#             i_Potato.grow()
#
#     def are_all_ripe(self): # Метод для проверки зрелости всей картошки
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]): # Здесь мы проверяем каждую картошку на зрелость
#             print('Картошка еще не созрела\n')  # т.е. создаем список из значений True/False и с помощью функции all проверяем сразу все значения
#         else:
#             print('Вся картошка созрела, можно собирать!')
#
#
# class Gardener:
#     def __init__(self, name, collected_potatoes):
#         self.name, self.collected_potatoes = name, collected_potatoes
#
#     def gardener_info(self):
#         print('Имя садовника: {}\nСколько собрал картошки: {}\n'.format(self.name, self.collected_potatoes))
#
#     def tend(self, my_garden):
#         if all([i_potato.is_ripe() for i_potato in my_garden.potatoes]): # Проверяем, не созрела ли картошка
#             question = int(input('Собрать картошку? \n1 - да, 2 - нет\n'))
#             if question == 1:
#                 potato_count = 0
#                 for i_potato in my_garden.potatoes: # Собираем картошку в цикле
#                     worker.collected_potatoes += 1
#                     potato_count += 1
#                     i_potato.state = 0 # Обнуляем статус каждой (так как собрали ее)
#                 print('{} собрал {} картофелин!'.format(worker.name, potato_count))
#                 worker.gardener_info()
#             else:
#                 print('Картошка пропадает! Может все таки соберем?')
#         else:
#             question = int(input('Отправить {}а ухаживать за картошкой? \n 1 - да, 2 - нет\n'.format(worker.name)))
#             if question == 1: # Если статус картошки не созревшый, с каждым циклом отправляем ухаживать за грядкой
#                 my_garden.grow_all()
#                 my_garden.are_all_ripe()
#
# my_garden = PotatoGarden(5)
# worker = Gardener('Михалыч', 0)
# print('\nКартошку посадили, теперь за ней нужно ухаживать!\n')
# while True:
#     try:
#         Gardener.tend(worker, my_garden)
#     except KeyboardInterrupt:
#         print('Программа завершена')

Задача 1. Машина 3 Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса
(то есть передаваться в init). Реализуйте такое изменение класса Два метода: Отображение информации об объекте класса
и Метод, который позволяет устанавливать текущую скорость машины
# class Toyota:
#
#     def __init__(self): # Последний аргумент передаем с помощью рандом
#         self.color = 'Red'
#         self.price = 1000000
#         self.max_speed = 200
#         self.cur_speed = self.speed_set() # Тут методом устанавливаем рандомную скорость
#
#     def info(self): # Метод для вывода инфо о машине
#         print(
#             'Car color: {}\nCar price: {}\nMax speed: {}\nCurrent speed: {}\n'.format(
#                 self.color, self.price, self.max_speed, self.cur_speed
#             )
#         )
#
#     def speed_set(self): # Метод для установки текущей скорости
#         self.cur_speed = random.randrange(0, 200)
#         return self.cur_speed
#
# car_1 = Toyota()
# car_2 = Toyota()
# car_3 = Toyota()
#
# car_3.info()

Задача 2. Координаты точки  Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут
передаваться пользовательские значения координат, по умолчанию x = 0, y = 0. Реализуйте класс, который будет представлять
эту точку, и напишите метод, который предоставляет информацию о ней. Также внутри класса пропишите счётчик, который будет
отвечать за количество созданных точек
# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         Point.count += 1 # Если нужно передать счетчик в сам класc, то обращаемся к нему через точку (а не через self к параметру)
#         self.x = x
#         self.y = y
#         self.point_info()
#
#     def point_info(self):
#         print(
#             '\nТочка номер: {}\nКоординаты по "X": {}\nКоординаты по "Y": {}'.format(
#                 self.count, self.x, self.y
#             )
#         )
#
# while True:
#     try:
#         action = input('\nХотите ввести координаты? ').lower()
#         if action == 'yes' or action == 'да':
#             x = int(input('\nВведите координаты точки Х: '))
#             y = int(input('Введите координаты точки Y: '))
#             point = Point(x, y)
#         else:
#             point = Point()
#     except KeyboardInterrupt:
#         print('\nПрограмма завершена!')

Задача 1. Драка Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют
друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от
одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу
# import random
# class Warrior:
#     def __init__(self, name, health=100):
#         self.name = name  # Не забыть про этот параметр, иначе на экран проблемно выводить имя объекта (нужны будут переменные)
#         self.health = health
#
#     def hit(self, target): # Нужно передавать только жертву, так как всего 2 участника, атакующим автоматически становится второй!!!
#         if target.health > 0:
#             target.health -= 20
#             self.info(target) # Опять же передаем только жертву, так как она меняется, для инфы про атакующего идем в self.name
#         if target.health == 0:
#             print(self.name, 'Победил')
#
#     def info(self, target):
#         print(
#             'Проводит атаку {}. У противника осталось {} очков здоровья'.format(
#                self.name, target.health # Здесь обращаемся к параметру здоровья таргета, а атакующий будет автоматом второй юнит
#             )
#         )
#
# warrior1 = Warrior('warrior1') # Обязательно нужно передать строковое значение имени, что бы не делать потом млн переменных
# warrior2 = Warrior('warrior2')
#
# while True:
#     who_hit = random.randint(1, 10) # Такой рандом нужен, что бы была больше вариативность(иначе может выбирать одну и ту же цифру)
#     if who_hit > 5:
#         warrior1.hit(warrior2) # Здесь передаем того, кто будет жертвой
#     else:
#         warrior2.hit(warrior1)
#     if warrior1.health <= 0 or warrior2.health <= 0: # Не забыть прирвать цикл ,что бы не идти ниже 0
#         break

Задача 2. Студенты Что нужно сделать
Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать свои или запросить их у пользователя) и
отсортируйте его по возрастанию среднего балла. Выведите результат на экран
# from operator import attrgetter
#
# class Student:
#
#     def __init__(self, name_surname, g_number, academic_performance):
#         self.name_surname = name_surname
#         self.g_number = g_number
#         self.academic_performance = academic_performance
#         self.score = self.average_score()
#
#     def average_score(self):
#         return sum(self.academic_performance) / len(academic_performance)
#
#     def print_info(self):
#         print('\nФамилия, Имя: {}\nНомер группы: {}\nОценки: {}\nСредний балл: {}'.format(
#             self.name_surname, self.g_number, self.academic_performance, self.score
#             )
#         )
#
#
# students = []
# for _ in range(10):
#     name_surname = input('\nВведите Имя и Фамилию через пробел: ').split()
#     g_number = int(input('Введите номер группы: '))
#     academic_performance = [int(input('Введите оценку: ')) for score in range(5)]
#     student = Student(name_surname, g_number, academic_performance)
#     students.append(student)
#
# # sorted_list = sorted(students, key=lambda student: student.average_score(), reverse=True) # Лямбду еще не проходили, но вроде понятно как работает)))
# sorted_list = sorted(students, key=attrgetter('score'), reverse=True) # Тут атрибутгеттером забираем ключ, т.к. это объект класса
#
# print('\nОтсортированный список студентов: ')
# for i in sorted_list:
#     i.print_info() # для печати така же используем функцию печати из класса, т.к. в списке лежат экземпляры класса,
#     # по другому просто не распечатать

Задача 3. Круг На координатной плоскости рисуются круги, у каждого круга следующие параметры: координаты X и Y центра
круга и значение R ― радиус круга. По умолчанию центр находится в (0, 0), а радиус равен 1 Реализуйте класс «Круг»,
который инициализируется по этим параметрам. Круг также может:
Находить и возвращать свою площадь, Находить и возвращать свой периметр, Увеличиваться в K раз, Определять, пересекается
ли он с другой окружностью.
# import math
#
# class Circle:
#     pi = math.pi
#
#     def __init__(self, x=0, y=0, r=1):
#         self.x = x
#         self.y = y
#         self.r = r
#
#     def get_area(self):
#         return self.r * self.r * self.pi
#
#     def get_perimeter(self):
#         return 2 * self.r * self.pi
#
#     def scale(self, k):
#         return self.get_area() * 2
#
#     def is_intersect(self, other):
#         return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2
#
# circle1 = Circle()
# circle2 = Circle()
# print(f'Площадь круга: {circle1.get_area()}')
# print(f'Периметр круга: {circle1.get_perimeter()}')
# print(f'Круг увеличенный в 2 раза: {circle1.scale(2)}')
# print(f'Возможное пересечение: {circle1.is_intersect(circle2)}')

Задача 4. Отцы, матери и дети Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
Имя.Возраст.Список детей. И он может:Сообщить информацию о себе. Успокоить ребёнка. Покормить ребёнка. У ребёнка есть:
Имя.Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).Состояние спокойствия.Состояние голода
# import random
# class Parent:
#     children_list = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('\nИмя: {}\nВозраст: {}:'.format(
#             self.name, self.age
#         )
#               )
#
#     def add_children(self):
#         c_quantity = int(input('Сколько будет детей? '))
#         check_age = Parent.__getattribute__(parent_list[0], 'age') #Здесь забираем возраст родителей в переменную для сверки
#         for i_quantity in range(c_quantity):
#             c_name = input(f'Введите имя {i_quantity + 1}-го ребенка: ')
#             c_age = int(input(f'Введите возраст {i_quantity + 1}-го ребенка: '))
#             if c_age < (check_age - 16):
#                 child = Child(c_name, c_age)
#                 Parent.children_list.append(child)
#             else:
#                 print('Ошибка: Возраст должен быть меньше возраста родителя хотя бы на 16 лет')
#                 c_age = int(input(f'Введите возраст {i_quantity + 1}-го ребенка: '))
#                 child = Child(c_name, c_age) #Делаем экземпляром класса
#                 Parent.children_list.append(child) # Здесь после сбора инфы циклом, добавляем в список родителей
#
#
# class Child:
#     state = ['hunger', 'calmness', 'nervous']
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.state = random.choice(self.state) # Тут рандомом выбираем состояние ребенка
#
#     def info(self):
#         print('Имя: {}, возраст: {}'.format(self.name, self.age)) # Это нужно для вывода инфы о детях т.к. это экземпляры
#
#     def s_state(self): # Тут тупо возвращаем состояние ребенка
#         return self.state
#
# parent_list = []
# parent_list.append(Parent('Bob', 48))
# parent_list.append(Parent('Jane', 48))
#
#
# Parent.add_children(Parent)
#
# print('\nРодители:')
# for i_parent in parent_list:
#     i_parent.info() # Через метод выводим инфу о родителях
#
# while True:
#     print('\nЧто хотите сделать?\n1 = Получить информацию о детях'
#           '\n2 = Проверить состояние детей\n3 = Завершить программу')
#     answer = int(input('\nВведите 1 2 ил 3 для выбора действия: '))
#     if answer == 1:
#         n = 1 # Это нужно что бы тупо нумеровать детей, т.к. i_child это не счетчик а экземпляр класса из списка, его как номер не поюзаешь
#         for i_child in Parent.children_list: # Здесь идем за объектами из списка
#             print(f'\n{n}-й ребенок')
#             n += 1
#             Child.info(i_child) # Выводим инфу по каждому ребенку
#     elif answer == 2:
#         for i_child in Parent.children_list:
#             name = Child.__getattribute__(i_child, 'name') #Тут забираем имя ребенка, иначе его из объекта не достать
#             if Child.s_state(i_child) == 'nervous': # Тут проверяем состояние ребенка
#                 print(f'\nРебенок {name} нервничает, нужно срочно его успокоить')
#             elif Child.s_state(i_child) == 'hunger':
#                 print(f'\nРебенок {name} голоден, нужно срочно покормить')
#             else:
#                 print(f'\nРодители могут отдыхать, ребенок {name} спокоен')
#     elif answer == 3:
#         print('Программа завершена!')
#         break
#     else:
#         print('Ошибка ввода! Введите 1, 2 или 3')

Задача 6. Магия У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые:
«Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава». Каждый элемент необходимо организовать как отдельный класс.
Если результат не определён, то возвращается None. Примечание: сложение объектов можно реализовывать через магический
метод __add__, вот пример использования: class Example_1:
    def __add__(self, other):
        return Example_2()
class Example_2:
    answer = 'сложили два класса и вывели'
a = Example_1()
b = Example_2()
c = a + b
print(c.answer)
# class Fire:
#     def __str__(self):
#         return 'Огонь'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Lightning()
#         elif isinstance(other, Water):
#             return Steam()
#         elif isinstance(other, Earth):
#             return Lava()
#         elif isinstance(other, Ice):
#             return Water()
#         elif isinstance(other, Snow):
#             return Water()
#         else:
#             return Undetermined()
#
#
# class Air:
#     def __str__(self):
#         return 'Воздух'
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         elif isinstance(other, Cold):
#             return Snow()
#         else:
#             return Undetermined()
#
#
# class Water:
#     def __str__(self):
#         return 'Вода'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Steam()
#         elif isinstance(other, Earth):
#             return Dirt()
#         elif isinstance(other, Cold):
#             return Ice()
#         elif isinstance(other, Ice):
#             return Water()
#         else:
#             return Undetermined()
#
#
# class Earth:
#     def __str__(self):
#         return 'Земля'
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Dirt()
#         elif isinstance(other, Fire):
#             return Lava()
#         elif isinstance(other, Air):
#             return Dust()
#         else:
#             return Undetermined()
#
#
# class Storm:
#     def __str__(self):
#         return 'Шторм'
#
#
# class Steam:
#     def __str__(self):
#         return 'Пар'
#
#
# class Ice:
#     def __str__(self):
#         return 'Лёд'
#
#
# class Dirt:
#     def __str__(self):
#         return 'Грязь'
#
#
# class Lightning:
#     def __str__(self):
#         return 'Молния'
#
#
# class Dust:
#     def __str__(self):
#         return 'Пыль'
#
#
# class Lava:
#     def __str__(self):
#         return 'Лава'
#
#
# class Snow:
#     def __str__(self):
#         return 'Снег'
#
#
# class Cold:
#     def __str__(self):
#         return 'Холод'
#
#
# class Undetermined:
#     def __str__(self):
#         return 'None'
#
#
# first = Air()
# second = Ice()
#
# result = first + second
#
# print(f"Смешиваем '{first}' и '{second}' и получаем '{result}'")

Прожить 365 дней с котом)))
# from random import randint
#
#
# class Man:
#     # класс людей
#     def __init__(self, name, fullness=50, house=None):
#         self.name = name
#         self.fullness = fullness  # сытость-показывает запас здоровья
#         self.house = house  # дом (экземпляр класса)
#
#     def __str__(self):
#         return f"{self.name}, сытость: {self.fullness}"  # будет использоваться для print(inst)
#         # где inst, является экземпляром класса
#
#     def eat(self):
#         # прием пищи (еда) для востановления сытости
#         if self.house.food >= 10:
#             print(f'{self.name} поел')
#             self.fullness += 10
#             self.house.food -= 10
#         else:
#             print(f'{self.name} нет еды')
#
#     def work(self):
#         # выполнение работы (при наличии постоянной работы)
#         print(f'{self.name} сходил на работу')
#         self.house.money += 150
#         self.fullness -= 10
#
#     def watch_tv(self):
#         # просмотр телевизора
#         print(f'{self.name} смотрел телевизор')
#         self.house.money -= 10
#         self.fullness -= 10
#
#     def clean(self):
#         # уборка в доме
#         print(f'{self.name} убрал грязь в доме')
#         self.house.mud = 0
#         self.fullness -= 1
#
#     def shopping(self):
#         # поход в магазин за продуктами
#         if self.house.money >= 50:
#             print(f'{self.name} сходил в магазин за едой')
#             self.house.money -= 50
#             self.house.food += 50
#         else:
#             print(f'{self.name} деньги кончились!')
#
#     def go_to_the_house(self, house):
#         # заселение в дом
#         self.house = house
#         self.fullness -= 10
#         print(f'{self.name} въехал в дом номер {self.house.number}')
#
#
# class House:  # дом хранит информацию о наличие ресурсов
#     def __init__(self, number, food=0, money=0, mud=0):
#         self.number = number
#         self.food = food
#         self.money = money
#         self.mud = mud
#
#     def __str__(self):
#         return f'В доме номер "{self.number}" еды: {self.food}, денег: {self.money}, грязь: {self.mud}'
#
#
# class Cat:  # класс котов
#     def __init__(self, name, cat_fullness=50, house=None):
#         self.name = name
#         self.cat_fullness = cat_fullness  # сытость (здоровье кота)
#         self.house = house  # дом домашнего кота
#
#     def __str__(self):
#         return f"{self.name}, сытость: {self.cat_fullness}"
#
#     def scratch_walls(self):
#         print(f'{self.name} поцарапал стены')
#         self.house.mud += 50
#         self.cat_fullness -= 20
#
#     def sleep(self):
#         print(f'{self.name} поспал')
#         self.cat_fullness -= 10
#
#     def eat(self):
#         if self.house.cat_food >= 10:
#             print(f'{self.name} поел')
#             self.cat_fullness += 20
#             self.house.cat_food -= 10
#         else:
#             self.cat_fullness -= 10
#             print(f'{self.name} нет еды')
#
#
# class Man_with_cat(Man):  # класс людей имеющих котов
#
#     def __str__(self):
#         return f"{self.name}, сытость: {self.fullness}"
#
#     def cat_shopping(self):
#         if self.house.money >= 50:
#             print(f'{self.name} сходил в магазин за едой для котов')
#             self.house.money -= 50
#             self.house.cat_food += 100
#         else:
#             print(f'{self.name} деньги кончились!')
#
#     def take_cat_in_the_house(self, cat):
#         cat.house = self.house
#         print(f'{self.name} взял в дом номер {self.house.number} кота {cat.name}')
#
#
# class House_with_cat(House):
#     def __init__(self, number, food, money, mud, cat_food=30):
#         House.__init__(self, number, food, money, mud)
#         self.cat_food = cat_food
#
#     def __str__(self):
#         return f'В доме номер "{self.number}" еды: {self.food}, еды для кота: {self.cat_food}, денег: {self.money}, грязь: {self.mud}'
#
#
# def citizen_daily_act():
#     # распорядок дня вынесен за пределы класса Man, так как распорядок индивидуален для каждого человека.
#     if citizen.fullness <= 0:
#         print(f'{citizen.name} умер...')
#         return
#     action = randint(1, 3)
#     while citizen.house.food >= 10 and citizen.fullness < 50:
#         citizen.eat()
#     citizen.work()
#     if citizen.house.food < 10:
#         citizen.shopping()
#     action = randint(1, 2)
#     if action == 1:
#         citizen.clean()
#     else:
#         citizen.watch_tv()
#
#
# def citizen_daily_act_with_cat():
#     # распорядок дня при наличие кота
#     if citizen.fullness <= 0:
#         print(f'{citizen.name} умер...')
#         return
#     while citizen.house.food >= 10 and citizen.fullness < 50:
#         citizen.eat()
#     citizen.work()
#     if citizen.house.food < 10:
#         citizen.shopping()
#     if citizen.house.cat_food <= 20:
#         citizen.cat_shopping()
#     action = randint(1, 2)
#     if action == 1:
#         citizen.clean()
#     else:
#         citizen.watch_tv()
#
#
# def cat_daily_act():  # события у кота в течение дня
#     if cat.cat_fullness <= 0:
#         print(f'{self.name} сдох...')
#         return
#     # action = randint(1, 2)
#     while cat.house.cat_food >= 10 and cat.cat_fullness < 50:
#         cat.eat()
#     action = randint(1, 2)
#     if action == 1:
#         cat.sleep()
#     elif action == 2:
#         cat.scratch_walls()
#
#
# if __name__ == '__main__':
#
#     citizen = Man(name='Петя')  # человек Петя
#     my_home = House(771)  # Пете дали дом
#     citizen.go_to_the_house(my_home)  # Петя заселился в дом
#     setattr(citizen, 'act', citizen_daily_act)  # установлен атрибут act (без кота)
#
#     for day in range(1, 4):
#         print(f'================ день {day} ==================')
#         citizen.act()
#         print('--- в конце дня ---')
#         print(citizen)
#         print(my_home)
#
#     # Петя решил стать кошатником. Сохраняем текущие данные.
#     # Создаем экземпляр класса кошатников и заносим текущие данные в новый экземпляр
#     name, fullness, house = citizen.name, citizen.fullness, citizen.house  # текущая информация
#     # о Пете
#     citizen = Man_with_cat(name, fullness, house)  # теперь Петя относится к тем, кто держит кота
#     setattr(citizen, 'act', citizen_daily_act_with_cat)  # установлен атрибут act (с котом)
#
#     # Сохраняем текущие данные экземпляра класса House.
#     # Создаем экземпляр класса House_with_cat и заносим текущие данные в новый экземпляр
#     number, food, money, mud = my_home.number, my_home.food, my_home.money, my_home.mud
#     my_home = House_with_cat(number, food, money, mud)
#     citizen.house = my_home  # оборудуем дом Пети для проживания кота,
#     # (значением citizen.house становится экземпляр класса House_with_cat)
#
#     cat = Cat(name="Пушок")  # Петя нашел кота и назвал его Пушок
#
#     citizen.take_cat_in_the_house(cat)
#     setattr(cat, 'act', cat_daily_act)
#
#     for day in range(1, 366):
#         print(f'================ день {day} ==================')
#         citizen.act()
#         cat.act()
#         print('--- в конце дня ---')
#         print(citizen)
#         print(cat)
#         print(my_home)

Задача 7. Совместное проживание
Что нужно сделать
Чтобы понять, стоит ли ему жить с кем-то или всё же лучше остаться в гордом одиночестве, Артём решил провести довольно
необычное исследование. Для этого он реализовал модель человека и модель дома. Человек может:
Есть (+ сытость, − еда). Работать (− сытость, + деньги). Играть (− сытость). Ходить в магазин за едой (+ еда, − деньги).
У человека есть имя, степень сытости (изначально 50) и дом. В доме есть холодильник с едой (изначально 50 еды) и тумбочка
с деньгами (изначально 0 денег). Если сытость человека становится меньше нуля, то человек умирает.
Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6.
2. Если сытость < 20, то поесть.
3. Иначе, если еды в доме < 10, то сходить в магазин.
4. Иначе, если денег в доме < 50, то работать.
5. Иначе, если кубик равен 1, то работать.
6. Иначе, если кубик равен 2, то поесть.
7. Иначе играть
# from random import randint
#
# class Man:
#     # класс людей
#     def __init__(self, name, fullness=50):
#         self.name = name
#         self.fullness = fullness
#
#     def __str__(self):
#         return f"{self.name}, сытость: {self.fullness}"  # будет использоваться для printa
#
#     def eat(self):
#         # прием пищи (еда) для восcтановления fullnes
#         print(f'{self.name} поел')
#         self.fullness += 1
#         my_home.food -= 1
#
#
#     def work(self):
#         # Поход на работу
#         print(f'{self.name} сходил на работу')
#         my_home.money += 1
#         self.fullness -= 1
#
#     def playing(self):
#         # поиграть
#         print(f'{self.name} поиграл')
#         self.fullness -= 20
#
#
#
#     def shopping(self):
#         # поход в магазин за продуктами
#         print(f'{self.name} сходил в магазин за едой')
#         my_home.money -= 1
#         my_home.food += 1
#         if my_home.money <= 0:
#             print(f'{self.name} деньги кончились!')
#
#
# class House:  # инфа о наличии денег и еды
#     def __init__(self, food=50, money=0):
#         self.food = food
#         self.money = money
#
#     def __str__(self):
#         return f'В доме еды: {self.food}, денег: {self.money}'
#
#
# def people_daily_act(man):
#     # Ежедневные действия класса Man отдельной ф-ей, т.к. они индивидуальны для каждого человека.
#     # if man.fullness <= 0:
#     #     print(f'{man.name} умер...')
#     action = randint(1, 6)
#     if man.fullness < 20:
#         if my_home.food > 0:
#             man.eat()
#         else:
#             pass
#     elif my_home.food < 10:
#         if my_home.money > 0:
#             man.shopping()
#         else:
#             pass
#     elif my_home.money < 50:
#         man.work()
#     elif action == 1:
#         man.work()
#     elif action == 2:
#         man.eat()
#     else:
#         man.playing()
#
#
# man_1 = Man('Артём')  # человек Артём
# man_2 = Man('Виртуальный сожитель Артёма))')
# my_home = House()  # Виртуальный дом Артёма
#
#
# for day in range(1, 366):
#     print(f'================ день {day} ==================')
#     people_daily_act(man_1)
#     people_daily_act(man_2)
#     print('-{:-^42}-'.format('В конце дня'))
#     print(man_1)
#     print(man_2)
#     print(my_home)
#     if man_2.fullness <= 0:
#         print(f'{man_2.name} умер...')
#         break
#     if man_1.fullness <= 0:
#         print(f'{man_1.name} умер...')
#         break

Блэк-джэк. Этим все сказано)) Из особенностей, колода формируется сама, какрты не повторяются (реализовано в классах)
# import random
# class Card:
#
#     def __init__(self, rank, lear):
#         self.rank = rank
#         self.lear = lear
#
#     def __str__(self): # Это для печати инфы о каждой карте в словаре
#         return f'Карта: {self.rank} {self.lear}'
#
#
# class Deck:
#     rank_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack of', 'Queen of', 'king of', 'Ace of']
#     lear_list = ['spades', 'hearts', 'clubs', 'Diamonds']
#     dec_dict = {}
#
#     def make_a_deck(self): # Заполняем колоду двумя циклами
#         for i_rank in self.rank_list: # Внешний для всего списка карт
#             for i_lear in self.lear_list: # внутренний для списка мастей
#                 rank = i_rank
#                 lear = i_lear
#                 card = Card(rank, lear)
#                 self.dec_dict[card] = 1 # ну и собираем составной ключ из card, а значение у всех 1 (оно в принципе не потребуется дальше)
#     # # Для проверки работы функции сбора колоды карт
#     # def dict_view(self):
#     #     for i_dict in self.dec_dict.keys():
#     #         print(i_dict)
#
#
# class Player:
#
#     def __init__(self, name):
#         self.name = name
#         self.card_list = []
#
#     def get_gard(self):
#         nex_card = random.choice(list(Deck.dec_dict.keys())) # Тут нужно превратить в список все ключи, иначе получим ошибку диопазона
#         self.card_list.append(str(nex_card).split()) # полученный ключ нужно превратить в строку, что бы можно было сверять его значения с условиями по срезу строки
#         Deck.dec_dict.pop(nex_card) # Удаляем из колоды карту, которую отдали игроку (что бы они не повторялись)
#         print(f'\nУ {self.name} на руках карты:')
#         self.card_list_view()
#         print('Сумма карт:', self.sum_card())
#
#     def card_list_view(self):
#         for i_card in self.card_list:
#             print(*i_card) # выводим список карт без кавычек и значков списка (для этого просто добавляем '*')
#
#     def sum_card(self):
#         summ = 0
#         for i_card in self.card_list:
#             if i_card[1] == 'king' or i_card[1] == 'Queen' or i_card[1] == 'Jack':
#                 summ += 10
#             elif i_card[1] == 'Ace' and summ <= 10:
#                 summ += 11
#             elif i_card[1] == 'Ace' and summ > 10:
#                 summ += 1
#             else:
#                 summ += int(i_card[1]) # тут как раз по срезу превращаем значение в цифру, если это не картинка
#         return summ
#
#     def info(self):
#         print(f'\nУ игрока {self.name} на руках карты:\n')
#         self.card_list_view()
#         print('Сумма карт:', self.sum_card())
#
# new_deck = Deck()
# new_deck.make_a_deck()
# # new_deck.dict_view() # Проверка колоды
#
# print('Сыграем в Блэк-джек...')
# pc_player = Player('PC_player')
# name = input('Как Вас зовут? ')
# player = Player(name)
# print('\nКоличество карт в колоде:', len(Deck.dec_dict))
#
# for _ in range(2):
#     pc_player.get_gard()
#     player.get_gard()
#
# while True:
#     print('\nКоличество карт в колоде:', len(Deck.dec_dict))
#
#     answer = int(input('\n1 = Взять карту, 2 = Открыть карты, 3 = Пропустить ход: '))
#     if answer == 1:
#         player.get_gard()
#         if player.sum_card() > 21:
#             print(f'\nУ Вас перебор!!! Победил игрок {pc_player.name}')
#             break
#         else:
#             pass
#     elif answer == 3:
#         print('\nВы пропускаете ход')
#         pass
#     elif answer == 2:
#         Player.info(pc_player)
#         Player.info(player)
#         if player.sum_card() > pc_player.sum_card():
#             print('\nУра!! Вы побели!')
#             break
#         elif player.sum_card() < pc_player.sum_card():
#             print('\nК сожалению вы проиграли')
#             break
#         else:
#             print('\nНичья')
#             break
#     else:
#         print('Ошибка ввода! Введите 1, 2 или 3', end=' ')
#         answer = int(input())
#
#     if pc_player.sum_card() < 18:
#         print(f'\nИгрок {pc_player.name} берет карту....')
#         pc_player.get_gard()
#         if pc_player.sum_card() > 21:
#             print(f'У игрока {pc_player.name} перебор! Вы победили!!!')
#             break
#     else:
#         print(f'\nИгрок {pc_player.name} пропускает ход')
#         pass

Задача 9. Крестики-нолики Напишите программу, которая реализует игру «Крестики-нолики». Да, это всё условие задачи
# def display_instruction():
#     print(''' \nСыграем в "крестики-нолики". Для того что бы сделать ход, введи номер клетки, '
#           'в которую хочешь поставить символ (Х или 0)''')
#
#
# class Board:
#     board = list(range(1, 10))
#
#     def display_board(self):
#         print('-' * 13)
#         for i_cell in range(3):
#             print('|', self.board[0 + i_cell * 3], # Тут умножаем индекс из цикла на 3 - так он будет соот-ть индексу цифры из списка board
#                   '|', self.board[1 + i_cell * 3], # Ну и т.к. в ряду всего три клетки, прибавляем умноженный индекс к 0, 1, 2
#                   '|', self.board[2 + i_cell * 3], '|')
#             print('-' * 13)
#
#
# class Player:
#
#     def __init__(self, symbol):
#         self.symbol = symbol
#
#     def make_a_move(self):
#         valid = False
#         while not valid: # False до тех пор, пока корректность ввода не подтверждена
#             player_answer = input(f'Куда поставим {self.symbol} ? ')
#             try:
#                 player_answer = int(player_answer) # Тут хитро проверяем, является ли введенная инфа цифрой с помощью try
#             except:
#                 print('Не корректный ввод. Нужно ввести число')
#                 continue
#             if 1 <= player_answer <= 9:
#                 if str(Board.board[player_answer - 1]) not in 'X0': # Тут проверяем, не стоит ли уже в списке board 'Х' или '0'
#                     Board.board[player_answer - 1] = self.symbol # Если нет, то меняем элемент списка board на 'Х' или '0'
#                     valid = True # Подтверждаем корректность замены
#                 else:
#                     print('Эта клетка уже занята')
#             else:
#                 print('Не корректный ввод. Для хода нужно ввести число от 1 до 9')
#
# class Victories:
#
#     def __init__(self):
#         self.win_seq = (
#             (0, 1, 2), (3, 4, 5),
#             (6, 7, 8), (0, 3, 6),
#             (1, 4, 7), (2, 5, 8),
#             (0, 4, 8), (2, 4, 6)
#         )
#
#     def check_win(self):
#         for each in self.win_seq: # Тут сверяем каждую комбинацию из win_seq и если значения каждого индекса в board из комбинации
#             if Board.board[each[0]] == Board.board[each[1]] == Board.board[each[2]]: # например (0, 1, 2) заполнены одним символом (равны друг другу)
#                 return Board.board[each[0]] # то возвращаем символ, которым они заполнены, например Board.board[each[0]] - заполнен "Х"
#         return False # что бы понять, кто выиграл. Если все три элемента не равны друг другу, то возвращаем False
#
# def game():
#     display_instruction()
#     board = Board()
#     result = Victories()
#     counter = 0
#     win = False
#     while not win: # Пока флаг вин не сработал, продолжаем играть
#         board.display_board()
#         if counter % 2 == 0:
#             Player('X').make_a_move()
#         else:
#             Player('0').make_a_move()
#         counter += 1
#         if counter > 4: # Проверять возможность выигрыша начинаем после 4-го хода, раньше бессмысленно
#             tmp = result.check_win()
#             if tmp:
#                 print(tmp, 'Выиграл!')
#                 win = True # переключаем флаг win
#                 break
#         if counter == 9: # Если после 9 ходов не нашелся победитель, прерываем игру (т.к. клетки пустые уже закончились)
#             print('Ничья!')
#     board.display_board()
#
# game()
# input('Нажмите enter для входа')

=========================================================================================================================
Инкапсуляция - объединение данных и методов в единый объект и сокрытие реализации от пользователя.
    Первый принцип - Инкапсуляция (сокрытие данных)
Что бы скрыть параметры класса, нужно вначале параметра добавить два нижних подчеркивания __
В таком случае методы, аргументы и функции будут доступны только внутри класса (и не доступны извне), что бы случайно вне класса
не изменить параметры
Важно! Это соглашение между программерами, и если очень надо, то можно получить доступ к сокрытому аттрибуту, спомощью
нижнего подчеркивания перед классом: Person._Person__count - Но делать так только в крайних случаях!!!
метод так же можно сделать приватным:
# def __do_action(self): # Используется как шестеренка для полноценной работы класса
# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name #(защищаем от изменения извне) Важно! Подчеркивания ставим в параметрах self
#         self.set_age(age) # сэлф с методом, заранее защищаемся от инициализации объекта с некорректным возрастом (метод проверит сразу)
#         Person.__count += 1
#     def __str__(self):
#         return 'Имя {}\tВозраст {}'.format(self.__name, self.__age)
#     def get_count(self): #Что бы получить данные из класса, нужно дописать метод (их называют геттеры):
#         return self.__count
#     def get_age(self):
#         return self.__age
#     def set_age(self, age): # А это метод, что бы установить параметры в классе ,называется сеттер
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception('Недопустимый возраст')
# misha = Person('Misha', 20)
# tom = Person('Tom', 25)
# print(misha.get_count())
# new_age = 80
# misha.set_age(new_age)
# print(misha.get_age())

Задача 1. Координаты точки В одной из практик предыдущего модуля была задача на реализацию класса «Точка». Модернизируйте
класс по следующему условию: объект «Точка» на плоскости имеет координаты x и y; при создании новой точки могут
передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
Предоставление информации о точке (используйте магический метод str). Геттер и сеттер для x. Геттер и сеттер для y
# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         Point.count += 1 # Если нужно передать счетчик в сам класc, то обращаемся к нему через точку (а не через self к параметру)
#         self.set_coordinates_y(y)
#         self.set_coordinates_x(x)
#
#
#     def __str__(self):
#         return '\nТочка номер: {}\nКоординаты по "X": {}\nКоординаты по "Y": {}'.format(
#                 self.count, self.__x, self.__y)
#
#     def set_coordinates_x(self, x):
#         if isinstance(x, int):
#             self.__x = x
#         else:
#             raise Exception('Координаты должны быть числом')
#
#     def set_coordinates_y(self, y):
#         if isinstance(y, int):
#             self.__y = y
#         else:
#             raise Exception('Координаты должны быть числом')
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
# action = input('\nХотите ввести координаты? ').lower()
# if action == 'yes' or action == 'да':
#     point = Point()
#     x = point.set_coordinates_x(int(input('\nВведите координаты точки Х: ')))
#     y = point.set_coordinates_y(int(input('Введите координаты точки Y: ')))
# else:
#     point = Point()
#
# print(point)
# point.set_coordinates_x(6)
# point.set_coordinates_y(4)
# print('X:', point.get_x())
# print('Y:', point.get_y())

Задача 2. Человек Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом
(должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов. Реализуйте
сокрытие данных для всех атрибутов (как статических, так и динамических), а для изменения и получения данных объекта
напишите специальные геттеры и сеттеры. При тестировании класса измените приватный атрибут (например, возраст) двумя
способами: сеттером и «крайне не рекомендуемым», который был показан в уроке
# class Human:
#     __count = 0 # __ нужны для защит от изменения случайно (извне класса)
#
#     def __init__(self, name, age):
#         self.set_name(name) #Вместо нижних подчеркиваний ставим функцию (она же сразу проверит введенные данные при инициалихации
#         self.set_age(age)
#         Human.__count += 1
#     def __str__(self):
#         return 'Имя {}\tВозраст {}'.format(self.__name, self.__age)
#     def get_count(self): #Что бы получить данные из класса, нужно дописать метод (их называют геттеры):
#         return self.__count
#     def get_age(self):
#         return self.__age
#     def get_name(self):
#         return self.__name
#     def set_age(self, age): # А это метод, что бы установить параметры в классе ,называется сеттер
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception('Недопустимый возраст')
#     def set_name(self, name):
#         if name.isalpha():
#             self.__name = name
#         else:
#             raise Exception('Имя должно содержать только буквы')
#
#
# misha = Human('Misha', 20) # Если в Имя добавить цифру, получим ошибку, метод проверит на корректность сам
# tom = Human('Tom', 25)
# print(misha.get_count())
# new_age = 80
# misha.set_age(new_age)
# print(misha.get_age())
# misha._Human__name = 'Vasya' # Это запрещенный прием (sucker_punch)
# print(misha.get_name())
========================================================================================================================
Наследование'''''Это подклассы или дочерние классы
Наследование - это механизм, позволяюший создать новый класс на основе уже существующего. Используется там, где можно
выделить общие свойства и поведение разных объектов'''''
# class Pat: # Это родительский класс (базовый или суперкласс)
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'да' if self.has_tail else 'нет'
#         return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail=tail
#         )
#
# class Cat(Pat): # Наследуем атрибуты класса Pat указав его в скобках, что бы не дублировать код
#     def sound(self):
#         print('Мяу!')
#
# class Dog(Pat):
#     def sound(self):
#         print('Гав!')
#
# class Frog(Pat):
#     has_tail = False
#     def sound(self):
#         print('Ква!')
#
# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(frog)
# print(cat)
# print(dog)
# cat.sound()
# dog.sound()
# frog.sound()

Задача 1. Корабли Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый
может сделать два действия: сообщить свою модель и идти по воде
# class Ship:
#     def __init__(self, model):
#         self.__model = model
#
#     def __str__(self):
#         return "\nМодель корабля: {model}".format(
#             model=self.__model
#         )
#
#     def sail(self):
#         return "\nКорабль куда-то поплыл!"
#
#
# class WarShip(Ship):
#     def __init__(self, model, gun): # Инит нужен что бы инициализировать корабль со вторым атрибутом "gun",  (в супер классе он один "model")
#         super().__init__(model) #Тут вызываем инит родительского(супер класса), правой клавишей по выделению и вызвать context menu, seuper class call
#         self.gun = gun # И только потом дополняем новый объект, нужными нам итрибутами
#
#     def attack(self):
#         print('\nКорабль атакует с помощью оружия', self.gun)
#
#
# class CargoShip(Ship):
#     def __init__(self, model):
#         super().__init__(model) # Обязательно вначале вызвать супер инит(род. класса) и только потом дописывать сэлф
#         self.tonnage_load = 0 # Т.к. передавать тонаж мы не планируем (в отличи от оружия), просто инциализируем его в инит
#
#     def load(self):
#         print('\nЗагружаем корабль!')
#         self.tonnage_load += 1
#         print('Текущая загруженность корабля', self.tonnage_load)
#
#     def unload(self):
#         if self.tonnage_load > 0:
#             print('\nРазгружаем корабль!')
#             self.tonnage_load -= 1
#         else:
#             print('\nКорабль уже разгружен!')
#         print('Текущая загруженность корабля', self.tonnage_load)
#
#
# warship = WarShip('zxc2', 'Пушки')
# warship.attack()
# cargoShip = CargoShip('qwe3')
# cargoShip.load()

Задача 2. Роботы Три варианта роботов, есть модель и допы для классов. Одно общее действие
# class Robot:
#     def __init__(self, model):
#         self.model = model
#
#     def operate(self):
#         return self.operate() # Т.к. действие общий метод для всех, просто возвращаем его
#
#     def __str__(self):
#         return "\nМодель робота {model}".format(
#             model=self.model
#         )
#
#
# class RobotCleaner(Robot):
#     def __init__(self, model):
#         super().__init__(model)
#         self.dust_bug = 0
#
#     def operate(self):
#         self.dust_bug += 1
#         print('Пылесосим пол! Заполненность мешка для пыли', self.dust_bug)
#
#
# class WarRobot(Robot):
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def operate(self):
#         print('Защищаяю военный объект с помощью оружия', self.gun)
#
#
# class MarineWarRobot(Robot):
#     def __init__(self, model, depth):
#         super().__init__(model)
#         self.depth = depth
#
#     def operate(self):
#         print('Защищаяю военный объект по водой, на глубине:', self.depth)
#
#
# robotCleaner = RobotCleaner('sad-5')
# print(robotCleaner)
# robotCleaner.operate()
# warRobot = WarRobot('SDF-45', 'Рельсотрон')
# print(warRobot)
# warRobot.operate()
# marineWarRobot = MarineWarRobot('LVC-258', 25)
# print(marineWarRobot)
# marineWarRobot.operate()

Задача 3. Кастомные исключения Исключения в Python также являются классами, и все они берут свои истоки от самого
главного класса — Exception. И для создания своего собственного класса ошибки достаточно написать его дочерний класс.
Например: '''class MyOwnException(Exception)'''
# class MyOwnException(Exception):
#     pass
#
# with open('answer.txt', 'r') as file:
#     for i_line in file:
#         try:
#             if i_line.strip().split()[0] < i_line.strip().split()[1]:
#                 raise MyOwnException()
#         except MyOwnException:
#             print('Это моя ошибка!')
#         finally:
#             result = round(int(i_line.strip().split()[0]) / int(i_line.strip().split()[1]), 2)
#             print(result)

Полиморфизм - принцип предполагающий возможность изменения функционала, унаследованного от базового класса
Плюс разбор документации
# class Human:
#     # Такая документация называется Docstring
#     """
#     Базовый класс описывающий человека
#     __count: общее количество человек
#
#     Args:
#         name (str): Передается имя человека
#         age (int): Передается возраст
#
#     Attributes:
#         max_count (int): Максимальное количество инстансов
#         (__скрытые агрументы как правило не описывают)
#         (есть прям программы для проверки документации - линтеры)
#     """
#     __count = 0 # __ нужны для защит от изменения случайно (извне класса)
#     max_count = 5
#
#     def __init__(self, name, age):
#         self.set_name(name) #Вместо нижних подчеркиваний ставим функцию (она же сразу проверит введенные данные при инициалихации
#         self.set_age(age)
#         self.location = 'Moscow'
#         if self.max_count < self.__count:
#             raise Exception('Слишком много людей')
#         Human.__count += 1
#
#     def __str__(self):
#         return 'Имя {}\tВозраст {}'.format(self.__name, self.__age)
#
#     def get_count(self): #Что бы получить данные из класса, нужно дописать метод (их называют геттеры):
#         return self.__count
#
#     def get_age(self):
#         """
#         Геттер для получения возраста
#         :rtype int
#         :return: age
#         """
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age): # А это метод, что бы установить параметры в классе ,называется сеттер
#         """
#         Сеттер для установки возраста
#         :param age: int
#         :raise Exception: Если возраст не в границах от 1 до 90, то вызывается исключение
#         """
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception('Недопустимый возраст')
#
#     def set_name(self, name):
#         if name.isalpha():
#             self.__name = name
#         else:
#             raise Exception('Имя должно содержать только буквы')
#
#
# class Student(Human):
#     def __init__(self, name, age, university):
#         super().__init__(name, age)
#         self.university = university
#
#     def __str__(self):
#         info = super().__str__() # Переопределяем родительскую __str__ для этого класса, что бы вывести инфу и его и родителя
#         info = '\n'.join(
#             (
#                 info,
#                 'Студент учится в университет {}'.format(self.university)
#             )
#         )
#         return info
#
#
# class Employee(Human):
#     """
#     Класс: Работник. Родитель: Person
#
#     Args:
#         name (str): Передается имя человека
#         age (int): Передается возраст
#
#         Attributes:
#         max_count (int): Максимальное количество инстансов
#
#         job (str): Должность работника
#     """
#     def __init__(self, name, age, company, salary):
#         super().__init__(name, age)
#         self.company = company
#         self.salary = salary
#
#     def __str__(self):
#         info = super().__str__() # Переопределяем родительскую __str__ для этого класса, что бы вывести инфу и его и родителя
#         info = '\n'.join(
#             (
#                 info,
#                 'Компания: {}\tЗарплата {}'.format(self.company, self.salary)
#             )
#         )
#         return info
#
# my_student = Student(name='Tom', age=25, university='MSU') # Передача именованных аргументов - правила хорошего тона
# print(my_student)
# my_employee = Employee(name='Bob', age=25, salary=10000, company='Google') #Более 7 параметров, как правило не передают
# print(my_employee)
# print(Human.__doc__) # Распечатка документации

Задача 1. Юниты Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие
«получить урон» (базовый класс получает 0 урона), солдат - урон = переданному, граждански - урон = переданный х 2
# class Unit:
#
#     def __init__(self, health):
#         self.__health = health
#
#     def take_damage(self, damage=10):
#         self.__health -= damage
#
#     def get_health(self):
#         return self.__health
#
#     def __str__(self):
#         return 'Состояние здоровья юнита: {}'.format(self.__health)
#
#
# class Soldier(Unit):
#     def __init__(self, health):
#         super().__init__(health)
#
#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 '\nКласс: Солдат, получает урон',
#                 info
#             )
#         )
#         return info
#
#     def take_damage(self, damage=any):# Здесь присваиваем damage значение по умолчанию any. Иначе будет не соответствие родителем
#         super(Soldier, self).take_damage(damage) # Если использовали инкапсуляцию, то переопределить атрибут метода можно
#         # так, иначе не получится получить доступ к атрибутам родительского класса
#
#
# class Civilian(Unit):
#
#     def __init__(self, health):
#         super().__init__(health)
#
#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 '\nКласс: Гражданский, получает двойной урон',
#                 info
#             )
#         )
#         return info
#
#     def take_damage(self, damage=any): # Здесь присваиваем damage значение по умолчанию any. Иначе будет не соответствие родителем
#         super(Civilian, self).take_damage(damage * 2) # Если использовали инкапсуляцию, то переопределить атрибут метода можно
#         # так, иначе не получится получить доступ к атрибутам родительского класса
#
# my_s = Soldier(100)
# my_s.take_damage(10)
# print(my_s)
# my_c = Civilian(100)
# my_c.take_damage(10)
# print(my_c)

Задача 2. Полёт Иногда для реализации дочерних классов используется так называемый класс-роль, где также описываются
общие атрибуты и  методы, но в программе инициализируются объекты только дочерних классов, а базовый класс-роль не трогается.
 К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться
# class CanFly:
#     height = 0
#     speed = 0
#
#     def fly_up(self):
#         pass
#
#     def flying(self):
#         pass
#
#     def landing(self):
#         self.height = 0
#         self.speed = 0
#
#     def __str__(self):
#         return "Высота: {}\nСкорость: {}".format(self.height, self.speed)
#
# class Butterfly(CanFly):
#     def __init__(self, ):
#         super().__init__()
#
#     def fly_up(self):
#         self.height = 1
#         print('Бабочка взлетела!')
#
#     def flying(self):
#         self.speed = 0.5
#         print('Бабочка летит!')
#
#
# class Rocket(CanFly):
#     def __init__(self):
#         super().__init__()
#
#     def fly_up(self):
#         self.height = 500
#         self.speed = 1000
#         print('Рокета взлетела!')
#
# my_butter = Butterfly()
# my_butter.fly_up()
# my_butter.flying()
# print(my_butter)
# my_rocket = Rocket()
# my_rocket.fly_up()
# print(my_rocket)
# my_rocket.landing()
# print(my_rocket)

Задача 1. Налоги Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового
класса Property и производных от него классов Apartment, Car и CountryHouse. Каждый дочерний класс должен иметь конструктор
с одним параметром, передающий свой параметр конструктору базового класса
# class Property:
#
#     def __init__(self, worth):
#         self.worth = worth
#
#     def tax_method(self):
#         pass
#
#
# class Apartment(Property):
#
#     def __init__(self, worth):
#         super().__init__(worth)
#
#     def tax_method(self):
#         return self.worth / 1000
#
#
# class Car(Property):
#
#     def __init__(self, worth):
#         super().__init__(worth)
#
#     def tax_method(self):
#         return self.worth / 200
#
#
# class CountryHouse(Property):
#
#     def __init__(self, worth):
#         super().__init__(worth)
#
#     def tax_method(self):
#         return self.worth / 500
#
#
# print('\n={:-^45}='.format('Расчет налогов на имущество'))
# amount_money = int(input('\nВведите количество имеющихся денег: '))
# print('Введите стоимость имущества: ')
#
# my_apartment = Apartment(float(input('\nСтоимость квартиры: ')))
# print(f'Налог на квартиру {my_apartment.tax_method()}')
#
# my_car = Car(float(input('\nСтоимость машины: ')))
# print(f'Налог на машину {my_car.tax_method()}')
#
# my_CH = CountryHouse(float(input('\nСтоимость загородного дома: ')))
# print(f'Налог на загородный дом {my_CH.tax_method()}')
#
# sum_tax = my_apartment.tax_method() + my_car.tax_method() + my_CH.tax_method()
# if sum_tax > amount_money:
#     print(f'\nВсего налога на сумму {sum_tax}, у Вас в наличии: {amount_money}')
#     diff = sum_tax - amount_money
#     print(f'Для уплаты налогов Вам не хватает: {round(diff, 2)}')
# else:
#     print(f'\nВсего налога на сумму {sum_tax}\nУ вас достаточно денег!')

Задача 2. Карма Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы
(это константа), чтобы достичь просветления. Каждый день вызывается специальная функция one_day(), которая возвращает
количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений)
# import random
#
# class MyOwnException(Exception):
#     pass
#
#
# class KillError(MyOwnException):
#     """
#     Класс: "Своя ошибка", родитель: MyOwnException
#     """
#     def __str__(self):
#
#         """
#         Функция возвращает строковое описание элемента
#
#         :return: (text)
#         :rtype (str)
#         """
#
#         return 'Убил комарика - попортил карму!'
#
#
# class DrunkError(MyOwnException):
#     def __str__(self):
#         return 'Перебрал горячительного, недобрал кармы'
#
#
# class CarCrashError(MyOwnException):
#     def __str__(self):
#         return 'Покоцал тачку?  Минусим бюджет и карму'
#
#
# class GluttonyError(MyOwnException):
#     def __str__(self):
#         return 'Переел? В весе плюс, в карме минус'
#
#
# class DepressionError(MyOwnException):
#     def __str__(self):
#         return 'Депрессия заминусила карму'
#
#
# def one_day(count):
#     if random.choices((0, 1), (1 - 1 / 10, 1 / 10))[0]:
#         with open('karma.log', 'a', encoding='utf-8') as file:
#             rand_exc = random.choice(
#                 [KillError(), DrunkError(), CarCrashError(),
#                  GluttonyError(), DepressionError()]
#             )
#             file.write(f'День: {count}, проступок: {rand_exc}\n')
#             raise rand_exc
#     else:
#         return random.randint(1, 7)
#
#
# count = 1
# karma = 0
# while karma < 500:
#     try:
#         karma += one_day(count)
#         print(f'День: {count}, карма: {karma}')
#         count += 1
#     except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError):
#         print(f'День: {count}, совершен проступок, минус в карму!')
#         karma -= random.randint(1, 7)


