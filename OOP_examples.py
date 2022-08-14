Последовательность фибоначчи
# def fibonacci(number):
#     result = []
#     cur_val = 0
#     next_val = 1
#
#     for _ in range(number):
#         result.append(cur_val)
#         cur_val, next_val = next_val, cur_val + next_val
#     return result
#
# print(fibonacci(8))
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
Очень важно! Даже если у класса нет атрибута, то объекту класса его все равно можно добавить через точку:
user1.age = 25 Но так делать не рекомендуется, так как это нарушает инкапсуляцию (но можно, если очень надо)))))

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
Методы бывают: классовые, статитчески и обычныe
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
#     pass                         # Просто заводим род.класс и пасуем (для своих ошибок)
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
#         with open('karma.log', 'a', encoding='utf-8') as file: # Для выбора ошибки, оборачиваем их все в []
#             rand_exc = random.choice(
#                 [KillError(), DrunkError(), CarCrashError(),
#                  GluttonyError(), DepressionError()]
#             )                                               # Для райза пишем каждую ошибку со скобками
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
#     except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError): # А вот в except можно просто писать имена ошибок(без скобкок)
#         print(f'День: {count}, совершен проступок, минус в карму!')
#         karma -= random.randint(1, 7)

Задача 3. Свой словарь Реализуйте класс MyDict, который будет вести себя точно так же, как и обычный словарь, за исключением того,
что метод get по умолчанию будет возвращать не None, а число 0
# class MyDict(dict): # В скобках указываем класс, который будет родителем
#     """
#     Создаем свой класс дневника. Родитель: Dict
#     Наследуем методы родителельского класса
#     """
#     def get(self, key, default_value=0):
#         """
#         Переопределяем родительский метод,
#         меняем возвращаемое по умолчанию значение
#
#         :param key: Type = Any
#         :param default_value: 0
#         :return: Value, default_value
#         :rtype: Value = Any, default_value (int)
#         """
#         if key in self:
#             return self[key]
#         else:
#             return default_value
#
# new_dict = MyDict()
# new_dict['A'] = 12
# new_dict[18] = 5
# new_dict['IDK'] = 0.35
#
# print(new_dict)
# print(new_dict.get('A'))
# print(new_dict.get('B'))

Задача 5. А-а-автомобиль! Реализуйте класс автомобиля, а также класс, который будет описывать автобус. У автобуса, кроме
того, что имеется у автомобиля, должны быть поля, содержащие число пассажиров и количество полученных денег, изначально
равное нулю. Также должны быть методы «войти» и «выйти», изменяющие число пассажиров. Наконец, метод move должен быть
переопределён, чтобы увеличивать количество денег в соответствии с количеством пассажиров и пройденным расстоянием
# import math
# import random
#
#
# class Car:
#     """
#     Базовый класс Car(автомобиль) описывающий движение оного.
#
#     Args:
#     x (int): передаётся координата 'х'
#     y (int): передаётся координата 'y'
#
#     Attributes:
#     x (int): координата 'x' точки нахождения Car
#     y (int): координата 'y' точки нахождения Car
#
#     """
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, dist, angle):
#         """
#         Метод для вычисления точки конечного следования Car(автомобиля)
#
#         :param dist: передаётся дистанция на которую движется Car
#         :rtype: int
#
#         :param angle: передаётся угол направления движения Car
#         :rtype: int
#
#         """
#         self.x = self.x + int(dist * math.cos(angle))
#         self.y = self.y + int(dist * math.sin(angle))
#         print('Едем прямо', self.x, self.y, 'дальность пути: ', dist)
#
#     def turn(self, dist, angle):
#         """
#         Метод для вычисления точки следования Car(автомобиля) при смене движения
#         (
#         изменение dist - расстоянии и angle - угла направления движения
#         )
#
#         :param dist: передаётся дистанция на которую движется Car
#         :rtype: int
#
#         :param angle: передаётся угол направления движения Car
#         :rtype: int
#
#         """
#         self.x = self.x + int(dist * math.cos(angle))
#         self.y = self.y + int(dist * math.sin(angle))
#         print('Поворот не туда', self.x, self.y, 'дальность пути: ', dist)
#
#
# class Bus(Car):
#     """
#     Класс Bus(автобус). Родитель: Car(автомобиль)
#
#     __peoples: количество пассажиров
#     __many: количество заработанных денег
#     __places: количество мест в Bus(автобус)
#
#     Args:
#     x (int): передаётся координата 'х'
#     y (int): передаётся координата 'y'
#     cost (int): передаётся величина тарифа расчёта стоимости билета
#
#     Attributes:
#     cost (int): тариф для расчёта стоимости поездки
#
#     """
#     __peoples = 0
#     __many = 0
#     __places = 24
#
#     def __init__(self, x, y, cost):
#         super().__init__(x, y)
#         self.cost = cost
#
#     def more_passengers(self, entered, dist):
#         """
#         Метод запускающий __peoples(пассажир) и собирающий many(деньги) с них.
#
#         :param entered: количество вошедших пассажиров
#         :rtype: int
#
#         :param dist: дистанция движения калькуляции вместе с cost
#         :rtype: int
#
#         """
#         if Bus.__peoples >= Bus.__places:
#             print('Мест нет')
#         else:
#             Bus.__peoples += entered
#             Bus.__many += (self.cost * dist) * entered
#             print(f'Зашло {entered}, оплата {Bus.__many}')
#
#     def less_passengers(self, people_came_out):
#         """
#         Метод для выхода пассажиров.
#
#         :param people_came_out: количество вышедших пассажиров.
#         :rtype: int
#
#         """
#         if Bus.__peoples - people_came_out < 0:
#             print('Не может выйти больше чем есть пассажиров.')
#         else:
#             Bus.__peoples -= people_came_out
#             print(f'Вышло {people_came_out}')
#
#     def get_many(self):
#         """
#         Геттер для показа суммы many(заработанных средств) в конце поездки.
#         :return:__many
#
#         """
#         return self.__many
#
#
# direction = 30
# distance = 100
#
# car = Car(1, 2)
# bus = Bus(2, 4, 3)
#
# route = 0
# while route != 5:
#     route += 1
#     if random.randint(1, 2) == 2:
#         bus.move(distance, direction)
#         bus.more_passengers(random.randint(1, 5), distance)
#         bus.less_passengers(random.randint(1, 5))
#     else:
#         bus.turn(random.randint(1, distance), random.randint(1, direction))
#         bus.more_passengers(random.randint(1, 5), distance)
#         bus.less_passengers(random.randint(1, 5))
#
#         print(f'Заработано {bus.get_many()}')

Задача 4. Компания Реализуйте иерархию классов, описывающих служащих в компании. На самом верху иерархии — класс Person,
который описывает человека именем, фамилией и возрастом. Все атрибуты этого класса являются приватными. Далее идёт класс
Employee и производные от него классы Manager, Agent и Worker
# class Person:
#     """
#     Базовый класс описывающий служащего
#
#     Args:
#         name(str): Передается имя служащего
#         surname(str): Передается фамилия служащего
#         age(int): Передается возраст служащего
#     """
#     def __init__(self, name, surname, age):
#         self.__name = name
#         self.__surname = surname
#         self.set_age(age)
#
#     def __str__(self):
#         return f'Имя: {self.get_name()}\nФамилия: {self.__surname}\nВозраст: {self.get_age()}'
#
#     def set_age(self, age):
#         """
#         Сеттер для установки возраста
#         :param age: int
#         :return: age
#         """
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception('Недопустимый возраст')
#
#     def get_age(self):
#         """
#         Геттер для получения возраста
#         :return: age
#         :rtype: int
#         """
#         return self.__age
#
#     def get_name(self):
#         """
#         Геттер для получения имени
#         :return: name
#         :rtype: str
#         """
#         return self.__name
#
#     def get_surname(self):
#         """
#         Геттер для получения фамилии
#         :return: surname
#         :rtype: str
#         """
#         return self.__surname
#
#
# class Employee(Person):
#     """
#     Класс: Служащий Родитель: Person
#     Args:
#         name(str): Передается имя служащего
#         surname(str): Передается фамилия служащего
#         age(int): Передается возраст служащего
#     """
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname, age)
#
#     def salary_type(self):
#         """
#         Базовый метод для определения заработной платы служащего.
#         :return: None
#         """
#         pass
#
#
# class Manager(Employee):
#     """
#     Класс: Менеджер  Родитель: Employee
#     Args:
#         name(str): Передается имя служащего
#         surname(str): Передается фамилия служащего
#         age(int): Передается возраст служащего
#     """
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname, age)
#
#     def salary_type(self):
#         """
#         Переопределенный метод для расчета ЗП менеджера.
#         :return: salary
#         :rtype: int
#         """
#         salary = 13000
#         return salary
#
#
# class Agent(Employee):
#     """
#     Класс: Агент  Родитель: Employee
#     Args:
#         name(str): Передается имя служащего
#         surname(str): Передается фамилия служащего
#         age(int): Передается возраст служащего
#         volume_of_sales(int): Передается объем продаж
#     """
#     def __init__(self, name, surname, age, volume_of_sales):
#         super().__init__(name, surname, age)
#         self.volume_of_sales = volume_of_sales
#
#     def salary_type(self):
#         """
#         Переопределенный метод для расчета ЗП агента.
#         :return: salary
#         :rtype: float
#         """
#         salary = 5000 + (self.volume_of_sales * (5 / 100))
#         return salary
#
#
# class Worker(Employee):
#     """
#     Класс: Работник  Родитель: Employee
#     Args:
#         name(str): Передается имя служащего
#         surname(str): Передается фамилия служащего
#         age(int): Передается возраст служащего
#         hours_worked(int): Передается кол-во отработанных часов.
#     """
#     def __init__(self, name, surname, age, hours_worked):
#         super().__init__(name, surname, age)
#         self.hours_worked = hours_worked
#
#     def salary_type(self):
#         """
#         Переопределенный метод для расчета ЗП работника.
#         :return: salary
#         :rtype: float
#         """
#         salary = self.hours_worked * 100
#         return salary
#
#
# staff_list = []
# print('\nВнесите менеджеров в список:')
# for _ in range(1):
#     name = input('\nИмя: ')
#     surname = input('Фамилия: ')
#     age = int(input('Возраст: '))
#     manager = Manager(name, surname, age)
#     staff_list.append(manager)
#
# print('\nВнесите агентов в список:')
# for _ in range(1):
#     name = input('\nИмя: ')
#     surname = input('Фамилия: ')
#     age = int(input('Возраст: '))
#     volume_of_sales = int(input('Объем продаж: '))
#     agent = Agent(name, surname, age, volume_of_sales)
#     staff_list.append(agent)
#
# print('\nВнесите работников в список:')
# for _ in range(1):
#     name = input('\nИмя: ')
#     surname = input('Фамилия: ')
#     age = int(input('Возраст: '))
#     hours_worked = int(input('Отработано часов: '))
#     worker = Worker(name, surname, age,hours_worked)
#     staff_list.append(worker)
#
# for i_elem in staff_list:
#     print(i_elem)
#     print(f'Заработная плата сотрудника: {i_elem.salary_type()}')
#     print()

Задача 7. Стек Стек — это абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO
(англ. last in — first out, «последним пришёл — первым вышел»). Напишите класс, который реализует стек и его возможности
(достаточно будет добавления и удаления элемента). После этого напишите ещё один класс — «Менеджер задач».
В менеджере задач можно выполнить команду «новая задача», в которую передаётся сама задача (str) и её приоритет (int).
    Сам менеджер работает на основе стека (не наследование!). При выводе менеджера в консоль все задачи должны быть
отсортированы по приоритету: чем меньше число, тем выше задача
# class Stack:
#     def __init__(self):
#         self.__my_st = []
#
#     def __str__(self):
#         return '; '.join(self.__my_st)
#         # return str(self.__my_st)
#
#     def push(self, elem):
#         self.__my_st.append(elem)
#
#     def pop(self):
#         if len(self.__my_st) == 0:
#             return None
#         return self.__my_st.pop() # Метод pop удаляет последний элемент списка, если не добавлять аргументы
#
#
# class TaskManager:
#
#     def __init__(self):
#         self.task = dict()
#
#     def __str__(self):
#         display = []
#         if self.task:
#             for i_priority in sorted(self.task.keys()):
#                 display.append('{prior} {task}\n'.format(
#                     prior=str(i_priority),
#                     task=self.task[i_priority]
#                 )
#             )
#         return ''.join(display)
#
#     def new_task(self, task, priority):
#         if priority not in self.task:
#             self.task[priority] = Stack()
#         self.task[priority].push(task)
#         # else:
#         #     print(f'Задача {task}, с приоритетом {priority} уже есть в списке задач!')
#
#     def remove_duplicate(self, priority):
#         temp_set = set(self.task)
#         for item in temp_set:
#             if item in temp_set:
#                 return item
#         return None
#
#
#     def remove_task(self, priority):
#         """
#         Метод удаляет задачу из указанного приоритета в Stack
#
#         :param priority: Передаем приоритет задачи, которую требуется удалить
#         :return: Stack with removed task
#         """
#         return self.task[priority].pop()
#
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("почитать книгу", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
# print(manager)
# manager.remove_task(1)
# print(manager)
# manager.remove_task(2)
# print(manager)
========================================================================================================================

Итератор - это объект который, позволяет перебирать элемнеты коллекции (например списка) с помощью цикла
Итераторы нужны для реализации сложных механизмов обхода элементов коллекций (списков, словаре и т.д.).
Важно!!! Итераторы, в отличии от генераторолв работаю с уже готовыми объектами, загруженными в память
items = [10, 20, 30] # Итерируемый объект
iterator = items.__iter__() # Итератор для списка items. Именно с ним и работает цикл (не с самим списком)
print(iterator)

for elem in iterator: # Если вызвать цикл второй раз с тем же итератором, то ничего не выведется, так как итератор
    print(elem)         # уже опустошился!!!!!

iterator = iter(items) # Альтернативный способ получить итератор
print(iterator.__next__()) # Метод, который используется в цикле, для получения следующего элемента коллекции (списка)
print(next(iterator)) # Альтернативный способ получить следующий элемент итератора

Задача 1. Свой for (ну почти) Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая
эмулирует работу цикла for с помощью цикла while и проходит во всем элементам итерируемого объекта. Не забудьте про
исключение «конца итерации»
# def self_for(elem):
#     my_iterator = iter(elem)
#     while my_iterator:
#         try:
#             print(next(my_iterator))
#         except StopIteration:
#             break
#
# items = [10, 20, 30]
# self_for(items)

Пишем свой итератор. В программу передается только лимит итерации. На каждом шагу итератор выдает рандомное число
# import random
#
# class RandomNumbers:
#
#     def __init__(self, limit): # Тут указываем максимальную границу итерации
#         self.__limit = limit
#         self.__counter = 0 # Этот счетчик нужен, что бы отсчитывать шаги итерации
#
#     def __iter__(self): # Метод нужен, что бы с ним мог работать цикл (брать итератор)
#         return self # Возвращает он сам себя (в сложных итераторах здесь могут быть доп. вычисления)
#
#     def __next__(self): # метод нужен, что бы возвращать следующие элементы для будущего цикла
#         if self.__counter < self.__limit: # Если счетчик меньше лимита итерации, с каждым шагом увеличиваем его на 1
#             self.__counter += 1
#             return random.randint(0, 10) # Тупо возвращаем рандомное число с каждым шагом итерации
#         else:
#             raise StopIteration # Если значение счетчика больше лимита итерации возвращаем ошибку,
#         # Она нужна, что бы цикл ее обоработал самостоятельно и остановился
#
#
# my_iter = RandomNumbers(limit=3)
# print(next(my_iter))
#
# for elem in my_iter:
#     print(elem)

Последовательность фибоначчи с помощью итератора ("lazy evaluation" - ленивые вычисления)
# class Fibonacci:
#
#     def __init__(self, number):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         self.number = number
#
#     def __iter__(self): # В итераторе обнуляем значения, что бы он не опустошался при следующем цикле
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         return self # Не забываем вернуть итератор
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.number: # Если шаг итерации выходит за диапазон, возвращаме ошибку, что бы цикл ее
#                 raise StopIteration # обработал и остановился
#             self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val # тут реализуем фибоначчи
#         return self.cur_val # Возвращаем следующее число фибоначчи
#
# fib_iterator = Fibonacci(10)
# for i_value in fib_iterator:
#     print(i_value)
# print(8 in fib_iterator) # Так можно проверить, есть ли число в последовательности фибоначчи. Это и есть "ленивые вычисления"
# # (lazy evaluation) Как только цикл обнарожит число, он остановится, что бы не вычислять последовательность целиком)

Задача 1. Бесконечный итератор (типа цикла вайл). Итератор-счётчик, который не принимает никаких атрибутов и имеет только один статический
атрибут — счётчик. Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
# class CountIterator:
#
#     def __iter__(self):
#         self.counter = 1
#         return self
#
#     def __next__(self):
#         i = self.counter
#         self.counter += 1
#         return i
#
# my_iter = CountIterator()
# for i_elem in my_iter:
#     print(i_elem)

Задача 2. Случайная сумма Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
(первый элемент — просто случайное вещественное число от 0 до 1) при каждом новом вызове итератора в цикле значения
считались заново
# import random
# class MyIter:
#
#     def __init__(self, number):
#         self.counter = 0
#         self.cur_val = random.random()
#         self.number = number
#
#     def __iter__(self): # В итераторе обнуляем значения, что бы он не опустошался при следующем цикле
#         self.counter = 0
#         self.cur_val = random.random()
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.number:
#                 raise StopIteration
#             self.cur_val = self.cur_val + random.random()
#         return self.cur_val
#
# seq = int(input('Кол-во элементов: '))
# new_iter = MyIter(seq)
#
# print('Элементы итератора:')
# for elem in new_iter:
#     print(round(elem, 2))
#
# seq = int(input('\nНовое кол-во элементов: '))
# new_iter = MyIter(seq)
#
# print('Элементы итератора:')
# for elem in new_iter:
#     print(round(elem, 2))

Задача 3. Простые числа Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые
числа от 1 до N.
Важно! Здесь применяется метод "Решето Эратосфена"
# class Primes:
#     def __init__(self, limit):
#         self.num = 2
#         self.limit = limit
#
#     def __isprime(self, n):
#         if n % 2 == 0: # Сначала пропускаем все числа кратные 2
#             return n == 2 # Возвращаем только первое значение n равное двойке, потому что она простое число (остальные пропускаем)
#         d = 3 # Тройка является следующим простым числом
#         while d * d <= n and n % d != 0: # Дальше пропускаем все числа до n, которые кратны (делятся) на 3 и не равны 0 при делении на n
#             d += 2 # d умножаем на d, т.к. следующее число, кратное ему, в вдове больше d
            # К d прибавляем 2, что бы получить следующее нечетное число (3 + 2 = 5), 5 тоже простое число
#         return d * d > n # Возвращаем все значения d, до указанного лимита (n)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.num < self.limit:
#             check = self.num
#             self.num += 1
#             if self.__isprime(check):
#                 return check
#         else:
#             raise StopIteration
#
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')

==========================================================================================================================
Генераторы - это итераторы, реализованный в виде функции. По ним можно итерироваться только один раз!!!
В отличии итераторов, нужны для "ленивой генерации". Они не умеют возвращать сразу все элементы коллекции,
возвращают каждый элемент по готовности (в ходе вычисления). Потому их использую для работы с большими объемами данных "на лету"
Внутри используют оператор yield - он замораживает состояние функции вместе со значениями внутри нее
Методы __iter__ и __next__ внутри используются автомавтически
Отличия: Итераторы используются для готовых структур данных, а генераторы для генерации данных "на лету"
# def fibonacci(number):
#     cur_val = 0
#     next_val = 1
#
#     for _ in range(number):
#         yield cur_val # Замораживает функцию и воспроизводит вычисление (в отличии от return, который функцию завершает)
#         cur_val, next_val = next_val, cur_val + next_val
#         if cur_val > 10 ** 6:
#             return # Вместо raise StopIteration можно использовать return. Он так же прервет выполнение функции
#
# def square(nums):
#     for num in nums:
#         yield num ** 2
#
# feb_seq = fibonacci(10000000000)
# for elem in feb_seq:
#     print(elem, end=' ')
# print('\n')
#
# # Генератор от генератора
# print(sum(square(fibonacci(number=5000)))) # Считаем сумму квадратов чисел fibonacci
#
# # Генераторные выражения
# print()
# cubes_gen = (num ** 3 for num in range(10))
# for nums in cubes_gen:
#     print(nums, end=' ')

Задача 1. Бесконечный генератор По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой
счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
# def is_prime(num):
#     if num == 2: return True
#     if num % 2 == 0: return False
#     for _ in range(3, num // 2, 2): # Все то же "Решето Эратосфена". Чистим двойки, начиная с тройки с шагом 2 перебираем числа
#         if num % _ == 0:
#             return False
#     return True
#
# def primes():
#     num = 2
#     while True:
#         if is_prime(num):
#             yield num
#         num += 1
#
# my_gen = primes()
# for elem in my_gen:
#     print(elem)

Задача 2. Очень большой файл В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите
программу, которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор
# import random
# def write():
#     with open('numbers.txt', 'w', encoding='utf-8') as file:
#         for _ in range(1000):
#             for _ in range(40):
#                 file.write(str(random.randint(0, 10)) + ' ')
#             file.write('\n')
#     return file
#
# def read():
#     with open('numbers.txt', 'r', encoding='utf-8') as file:
#         for i in file.read():
#             if i.isdigit():
#                 yield int(i)
#         return
#
# def file_summ(nums):
#     summa = 0
#     for num in nums:
#         summa += num
#     return summa
#
# new_file = write()
# print(file_summ(read()))

Аннотация типов нужна для читаемости кода и для проверки кода автоматизированныи инструментами
from collections.abc import Iterable
# class Person:
#     __count = 0
#
#     def __init__(self, name: str, age: int): # Что бы питон предупреждал, что тип данных не соответсвует
#         self.__name = name
#         self.set_age(age)
#         Person.__count += 1
#
#     def __str__(self) -> str: # стрелочкой (->) указываем что возвращает функция. Если ничего, пишем None
#         return 'Имя {}\tВозраст {}'.format(self.__name, self.__age)
#
# def fibonacci(number: int) -> Iterable[int]: # Типы можно импортировать из коллекций
#     result = []
#     cur_val = 0
#     next_val = 1
#
#     for _ in range(number):
#         result.append(cur_val)
#         cur_val, next_val = next_val, cur_val + next_val
#     return result

Задача 1. Квадраты чисел Пользователь вводит число N. Напишите программу, которая генерирует последовательность из
квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами:
класс-итератор, функция-генератор и генераторное выражение
# from collections.abc import Iterable
# class Squares:
#     def __init__(self, limit: int):
#         self.__limit = limit
#         self.__num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self) -> Iterable[int]:
#         while self.__num <= self.__limit:
#             i = self.__num ** 2
#             self.__num += 1
#             return i
#         else:
#             raise StopIteration
#
# def my_gen(limit: int) -> Iterable[int]:
#     for i_elem in range(1, limit + 1):
#         i = i_elem ** 2
#         yield i
#
# n = int(input('Введите число: '))
#
# # Способ 1: Генераторное выражение
# g_expression = (num ** 2 for num in range(1, n + 1))
# for elem in g_expression:
#     print(elem, end=' ')
#
# # Способ 2: класс-итератор
# print()
# my_iter = Squares(n)
# for elem in my_iter:
#     print(elem, end=' ')
#
# # Способ 3: функция-генератор
# print()
# new_gen = my_gen(n)
# for elem in new_gen:
#     print(elem, end=' ')

Задача 4. Последовательность Хофштадтера Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором)
Сама последовательность выглядит так:Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))
В итератор (или генератор) передаётся список из двух чисел. Например, QHofstadter([1, 1]) генерирует точную
последовательность Хофштадтера. Если передать значения [1, 2], то последовательность должна немедленно завершиться
# from collections.abc import Iterable
# def QHofstadter(s_list: list) -> Iterable[int]:
#     a = s_list[:]
#     while True:
#         if s_list == [1, 2]:
#             break
#         else:
#             try:
#                 q_num = a[-a[-1]] + a[-a[-2]]
#                 a.append(q_num)
#                 yield q_num
#             except IndexError:
#                 return
#
# limit = 1 # Т.к. псоледовательность бесконечна, ограничил ее на 25 итерациях
# for x in QHofstadter([1, 1]):
#     if limit < 25:
#         print(x, end=' ')
#         limit += 1
#     else:
#         break

Задача 3. Пути файлов Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной
директории (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов

# from collections.abc import Iterable
# import os
#
# def gen_find_dir(folder: str, path: str) -> Iterable[str]:
#     print('Текущая директория', path)
#     try:
#         for i_elem in os.listdir(path):
#             current_path = os.path.join(path, i_elem)
#             if os.path.isdir(current_path) and i_elem != folder:
#                 yield from gen_find_dir(folder, current_path)
#             elif os.path.isfile(os.path.join(path, i_elem)):
#                 yield os.path.join(path, i_elem)
#             else:
#                 print(f'Директория {folder} найдена')
#                 break
#
#     except PermissionError:
#         print('Отказано в доступе, продолжаем поиск...')
#
# rootdir = os.path.abspath(os.path.join(os.path.sep))
# user_folder = input('Введите имя каталога: ')
# result = gen_find_dir(folder=user_folder, path=rootdir)
#
# for i_path in result:
#     print(i_path)
И еще вариант с os.walk
# with open('output.txt','w') as fout:
#     for root, subFolders, files in os.walk(rootdir):
#         if 'data.txt' in files:
#             with open(os.path.join(root, 'data.txt'), 'r') as fin:
#                 for lines in fin:
#                     dosomething()

Задача 5. Количество строк Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет
общее количество строк кода, игнорируя пустые строки и строчки комментариев
# import os
# from collections.abc import Iterable
#
# def file_path_find(path: str) -> Iterable[str]:
#     """Функция рекурсивно проходит по дереву каталога, генерирует пути к файлам"""
#     for i_elem in os.listdir(path):
#         new_path = os.path.join(path, i_elem)
#         if os.path.isdir(new_path) and not new_path.endswith('.git') and not new_path.endswith('.idea'):
#             yield from file_path_find(new_path)
#         else:
#             if new_path.endswith('.py'):
#                 yield read_and_count(new_path)
#
# def read_and_count(new_file: str) -> int:
#     """Функция для чтения файлов и подсчета количества строк кода"""
#     count = 0
#     with open(new_file, 'r', encoding='utf-8') as file:
#         for line in file.read().split('\n'):
#             if (not line.strip() == '') and (not line.strip().startswith("#")) and (not line.strip().startswith('"')):
#                 count += 1
#     return count
#
# file_path = r"C:\Users\notf8\PycharmProjects\Python_Basic\Python_Basic"
# print('Общее число строк кода:', sum(file_path_find(file_path)))

Задача 6. Односвязный список Связный список — это структура данных, которая состоит из элементов, называющихся узлами.
В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка
В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону
конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно
# from typing import Optional, Any
#
# class Node:
#     """
#     Класс: Узел. Описывает элементы списка.
#
#     """
#     def __init__(self,
#                  value: Optional[Any] = None, # Элемент списка может быть чем угодно
#                  next: Optional['Node'] = None) -> None: # Next от Node означет след элемент себя же
#         self.value = value
#         self.next = next
#
#     def __str__(self) -> str:
#         """
#         Метод возвращает элементы списка в строковом формате.
#         :return: Node
#         :rtype: str
#         """
#         return f'{self.value}'
#
#
# class Linkedlist:
#     def __init__(self) -> None:
#         """
#         Класс Список. Описывает односвязный список.
#         """
#         self.head: Optional[Node] = None # head может быть либо узлом либо None
#         self.length = 0 # Счетчик длины для проверки индексов списка
#
#     def __str__(self) -> str:
#         """
#         Метод возвращает односвязный список в виде строки.
#         :return: Linkedlist
#         :rtype: str
#         """
#         if self.head is not None:
#             current = self.head
#             values = [str(current.value)] # Создаем обычный список значений
#             while current.next is not None: # Идем циклом по значениям и возвращаем строку
#                 current = current.next # помещаем в текущий элемент ссылку на следующий
#                 values.append(str(current.value)) # Добавляем в обычный список следующее значение
#             return '[{values}]'.format(values=' '.join(values))
#         return 'Linkedlist []' # 'Linkedlist' не печатаемая часть, выведется только список
#
#     def __iter__(self):
#         """
#         Метод: Итератор
#         :return: self
#         """
#         return self
#
#     def __next__(self):
#         """
#         Метод возвращает следующий элемент списка.
#         :return: Node
#         """
#         if self.head is None:
#             raise StopIteration
#         current, self.head = self.head, self.head.next
#         return current
#
#     def append(self, elem: Any) -> None:
#         """
#         Метод добавляет элементы в список
#         :param elem: Any
#         :return: None
#         """
#         new_node = Node(elem) #Создаем узел
#         if self.head is None: # Если изначально список пустой, то head будет указывать на этот же узел
#             self.head = new_node # И значит head'ом будет новый нод
#             return
#
#         last = self.head # А если в списке уже есть элементы, в переменную помещаем его первый элемент
#         while last.next: # Идем (только с головы и только в конец списка) циклом по элементам
#             last = last.next # Если next не равен None, то у него есть сосед, его и берем
#         last.next = new_node # Если элемент последний, выходим из цикла и делаем ему соседа
#         self.length += 1 # Увеличиваем длину списка после добавления элемента
#
#     def remove(self, index) -> None:
#         """
#         Метод удаляет элементы из списка
#         :param index: int
#         :return: None
#         """
#         cur_node = self.head # Берем переменную, что бы случайно не поменять голову
#         cur_index = 0 # Это переменная для текущего индекса
#         if self.length == 0 or self.length <= index: # Проверяем, не выходит ли индекс за пределы списка
#             raise IndexError # Если выходит, выводим ошибку индекса
#
#         if cur_node is not None: # Проверяем, не пустой ли текущий указатель
#             if index == 0: # Так же проверим, не удаляем ли мы первый элемент
#                 self.head = cur_node.next # Просто заменяем ссылку в голове, на ссылку из следующего элемента
#                 self.length -= 1 # Уменьшаем длину на 1 после удаления элемента
#                 return # И выходим
#
#         while cur_node is not None: # Если элемент не первый в списке
#             if cur_index == index: # Идем по списку и сравниваем текущий индекс, с переданным
#                 break # Выходим, т.к. если переданный индекс окажется первым элементом, у нас есть условие для него выше
#             prev = cur_node # Берем предыдущий элемент в переменную
#             cur_node = cur_node.next # Текущий становится следующим
#             cur_index += 1 # И увеличиваем текущий индекс на 1
#
#         prev.next = cur_node.next # Как только нашли нужный узел, заменяем ссылку в предыдущем узле на след. за найденным узлом
#         self.length -= 1 # Уменьшаем длину на 1
#
#     def get(self, index) -> Optional[Node]:
#         """
#         Метод для получения элементов списка по индексу.
#         :param index: int
#         :return: Node (элемент списка)
#         """
#         cur_node = self.head # Берем переменную, что бы связать элемент с индексом
#         cur_index = 0 # Это переменная для текущего индекса
#         if self.length < index: # Проверяем, не выходит ли индекс за пределы списка
#             raise IndexError
#         while cur_node is not None: # Проверяем, не пустой ли текущий указатель
#             if cur_index == index: # Если текущий индекс соответствует переданному
#                 return cur_node # Возвращаем текущий элемент
#             cur_index += 1 # Если нет, то увеличиваем индекс на 1
#             cur_node = cur_node.next # И делаем следующий элемент текущим
#
# my_list = Linkedlist()
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print(my_list)
# print('\nТеперь с итераторм:')
# for i in my_list:
#     print(i)
========================================================================================================================
Функция высшего порядка - может принимать в качестве аргумента другую функцию и/или возвращать результаты ее работы
# import time
# from typing import Callable, Any
#
# def timer(func: Callable, *args, **kwargs) -> Any: # func - вызываемое. Здесь передаем kwargs и  args т.к. какие то функции будут с аргкиентами, а какие то нет
#     """Функция таймер. Выводит время работы функции и возвращает ее результат"""
#     started_at = time.time()
#     result = func(*args, **kwargs) # !!! А вот тут пишем со скобками, что бы аргумент запустился как функция
#     ended_at = time.time()
#     run_time = round((ended_at - started_at), 4)
#     print('Затраченное время функции: {} cекунд(ы).'.format(run_time))
#
#     return result
#
# def squares_sum() -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum(i_num ** 2 for i_num in range(10000))
#
#     return result
#
# def cubes_sum(number: int) -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#     result = 0
#     for _ in range(number + 1):
#         result += sum(i_num ** 3 for i_num in range(10000))
#
#     return result
#
# my_result = timer(squares_sum) # Когда передаем функцию (как аргумент) в другую функцию - пишем ее без скобок "squares_sum"
# print('Результат работы функции:', my_result)
# print()
# my_cubes_sum = timer(cubes_sum, 200) # аргумент для передаваемой функции пишем через запятую
# print('Результат работы функции:', my_cubes_sum)

Задача 1. Функции Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10
Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции
# from typing import Callable
#
# def func_1(x: int) -> int:
#     return x + 10
#
# def func_2(func: Callable, *args) -> int:
#     result = func_1(*args)
#     return result * func_1(*args)
#
# print('Результат:', func_2(func_1, 9))

========================================================================================================================
Декораторы!!!
1) Декоратор - это функция, ожидающая другую функцию в качестве параметра
2) Далее идет вложенная функция (обертка) = wrapped_func(*args, **kwargs). Аргументы для декорируемой функции передаются через функцию обертку (wrapped_func)
3) Потом код обертки (что угодно может быть, любая модификация, которая нам нужна)
4) Идет сама вызываемая (декорируемая) value = Func(*args, **kwargs)
5) Далее снова может идти любой код
6) !!!! В конце обертка возвращает результат работы функции: return value
7) В конце декоратор возвращает функцю-обертку в качестве объекта (т.е. без скобок): return wrapped_func
8) обернуть в декоратор функцию можно через знак @ и название функции декоратора над декорируемой функцией (сверху)
 Далее синтаксис для вызова задекорированных функций обучный: Функция()
Из минусов - сложны для отладки, кучу кода нужно выполнять перед основной функции
Если декораторов несколько, то порядок, в котором они применяются - имеет значение!!
# import time
# from typing import Callable, Any
# import functools # Что бы иметь доступ к метода функций если используется обертка в декораторе
#
# def timer(func: Callable) -> Callable: # func - вызываемое. Здесь передаем kwargs и  args т.к. какие то функции будут с аргкиентами, а какие то нет
#     """
#     Декоратор Выводит время работы декорируемой функции и возвращает ее результат
#     """
#
#     @functools.wraps(func) # С помощью этого декоратора приписываем обертке методы, которые указаны в декорируемой функции
#     def wrapped_func(*args, **kwargs) -> Any: # Аргументы для декорируемой функции передаются ф-ей оберткой (wrapped_func)
#         started_at = time.time()
#         result = func(*args, **kwargs) # !!! Тут пишем именно аргумента не саму декорируемую функцию, пишем со скобками!
#         ended_at = time.time()
#         run_time = round((ended_at - started_at), 4)
#         print('Затраченное время функции: {} cекунд(ы).'.format(run_time))
#
#         return result
#     return wrapped_func # Возвращаем функцию без скобок
#
# def logging(func: Callable) -> Callable: # func - вызываемое. Здесь передаем kwargs и  args т.к. какие то функции будут с аргкиентами, а какие то нет
#     """
#     Декоратор, логирующий работу кода.
#     """
#
#     @functools.wraps(func) # С помощью этого декоратора приписываем обертке методы, которые указаны в декорируемой функции
#     def wrapped_func(*args, **kwargs) -> Any: # Аргументы для декорируемой функции передаются ф-ей оберткой (wrapped_func)
#         print('Вызывается функция {func}\t'
#               'Позиционные аргументы: {args}\t'
#               'Именованные аргументы: {kwargs}'.format(
#                 func=func.__name__, args=args, kwargs=kwargs
#         ))
#         print('Функция успешно завершила работу')
#         result = func(*args, **kwargs) # !!! Тут пишем именно аргумента не саму декорируемую функцию, пишем со скобками!
#         return result
#     return wrapped_func # Возвращаем функцию без скобок
#
# @logging
# @timer
# def squares_sum() -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#     """
#     Функция нахождения суммы квадратов
#     для каждого N от 0 до 10 000
#     где 0 < N < 10 000
#     :return: Сумма квадратов
#     """
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum(i_num ** 2 for i_num in range(10000))
#
#     return result
#
# @timer
# @logging
# def cubes_sum(number: int) -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#     result = 0
#     for _ in range(number + 1):
#         result += sum(i_num ** 3 for i_num in range(10000))
#
#     return result
#
#
# my_result = squares_sum() # При использовании декоратора, функцию используем как обычно, в конце пишем скобки
# print('Результат работы функции:', my_result)
# print()
# my_cubes_sum = cubes_sum(200)
# print('Результат работы функции:', my_cubes_sum)
# print()
# print(squares_sum.__doc__) # Выводит документацию функции
# print(squares_sum.__name__) # Выводит имя функции

Задача 1. Двойной вызов Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию
# from typing import Callable, Any
#
# def do_twice(func: Callable) -> Callable:
#     """
#     Декоратор. Повторяет дважды декорируемую функцию
#     :param func:
#     :return: Callable
#     """
#     def wrapping_func(*args, **kwargs) -> Any:
#         for _ in range(2):
#             result = func(*args, **kwargs)
#         return result
#
#     return wrapping_func
#
# @do_twice
# def greeting(name: str) -> None:
#     print('Привет, {name}!'.format(name=name))
#
# greeting('Tom')

Задача 2. Плагины специальный декоратор, который будет «регистрировать» нужные функции как плагины и заносить их в
соответствующий словарь
# from typing import Callable, Dict
#
# def register(func: Callable) -> Callable: # Декоратор не обязательно оборачивает ф-ию в доп. код и модернезирует ее
#     """Декоратор регистрирует функцию как плагин"""
#     PLAGGINS[func.__name__]=func
#     return func
#
# PLAGGINS: Dict[str, Callable] = dict()
#
# @register
# def say_hallo(name: str) ->str:
#     return 'Hello! {name}!'.format(name=name)
#
# @register
# def say_goodbye(name: str) ->str:
#     return 'Goodbye! {name}!'.format(name=name)
#
# print(PLAGGINS)
# print(say_hallo('Tom'))

Задача 1. Как дела? Декоратор при вызове декорируемой функции спрашивает у пользователя «Как дела?», вне зависимости от
ответа отвечает что-то вроде «А у меня не очень!» и только потом запускает саму функцию
# from typing import Callable, Any
# import functools
#
# def how_are_you(func: Callable) -> Callable:
#     """ Декоратор перед запуском декорируемой ф-ии,
#     задает вопрос пользователю ип возвращает результат декорируемой функции. """
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         input('\nКак дела? ')
#         print('А у меня не очень! Ладно, держи свою функцию.')
#         result = func(*args, **kwargs)
#         return result
#     return wrapped_func
#
# @how_are_you
# def test() -> None:
#     """Тестовая функция для проверки декоратора. Выводит простой текст """
#     print('<Тут что-то происходит...>')
#
# print(test.__doc__)
# test()

Задача 2. Замедление кода - декоратор, который перед выполнением декорируемой функции ждёт несколько секунд
# from typing import Callable, Any
# import functools
# import time
#
# def waiting(func: Callable) -> Callable:
#     """ Декоратор перед запуском декорируемой ф-ии, ждет несколько секунд. """
#
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         print('Ждем 3 секунды...')
#         time_at_start = time.time()
#         time.sleep(3)
#         time_at_stop = time.time()
#         print('\nЗапускаем функцию: {func}'.format(func=func.__name__))
#         result = func(*args, **kwargs)
#         print('\nФункция успешно запустилась спустя:',
#               round((time_at_stop - time_at_start), 2), 'секунд(ы)')
#         return result
#     return wrapped_func
#
# @waiting
# def test() -> None:
#     """Тестовая функция для проверки декоратора. Выводит простой текст """
#     print('<Тут что-то происходит...>')
# test()

Задача 3. Логирование Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится
название функции и её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл
function_errors.log записываются названия функции и ошибки
# from typing import Callable, Any, Iterable
# import functools
# from datetime import datetime
#
# def logging(func: Callable) -> Callable:
#     """
#     Декоратор, логирующий работу кода.
#     """
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#             print('Вызывается функция {func}\t'
#                   'Документация функции: {docs}\t'.format(
#                     func=func.__name__, docs=func.__doc__
#             ))
#             try:
#                 result = func(*args, **kwargs)
#                 return result
#             except Exception as error:
#                 error = f'\nДата запуска: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")} - ' \ # !!!Формат даты и времени
#                         f'Запускаемая функция: {func.__name__} - Тип ошибки:{error}'
#                 with open('function_errors.log', 'a', encoding='utf-8') as file:
#                     file.write(error)
#
#     return wrapped_func
#
# @logging
# def sero_division() -> float:
#     """Функция для проверки: производит деление на ноль"""
#     x = 1 / 0
#     return x
#
# @logging
# def norm_func() -> str:
#     """Функция для проверки: функция не содержит ошибок"""
#     x = 'Hello'
#     return x
#
# @logging
# def name_error() -> Iterable:
#     """Функция для проверки: возвращает ошибку имени"""
#     a = b
#     return a
#
# @logging
# def no_arg(x):
#     """Функция для проверки: ошибка - в функцию не передан аргумент"""
#     print(x)
#
# for _ in range(3):
#     sero_division()
#     norm_func()
#     no_arg()
#     name_error()

Задача 4. Дебаг Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя (вместе со всеми
передаваемыми аргументами), а затем — какое значение она возвращает. После этого выводится результат её выполнения
# from typing import Callable, Any
# import functools
#
# def debug(func: Callable) -> Callable:
#     """
#     Декоратор, при каждом вызове декорируемой функции
#     выводит её имя (вместе со всеми передаваемыми аргументами)
#     а также какое значение она возвращает
#     """
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         print('\nВызывается функция {func}\t'
#               'Позиционные аргументы: {args}\t'
#               'Именованные аргументы: {kwargs}'.format(
#                 func=func.__name__, args=args, kwargs=kwargs
#         ))
#         result = func(*args, **kwargs)
#         print("{func} вернула значение {res}".format(
#             func=func.__name__, res=result))
#         print(result)
#         return result
#
#     return wrapped_func
#
# @debug
# def greeting(name, age=None) -> str:
#     """Функция возвращает имя и возраст переданные в аргументах"""
#     if age:
#         return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
#     else:
#         return "Привет, {name}!".format(name=name)
#
# greeting("Том")
# greeting("Миша", age=100)
# greeting(name="Катя", age=16)

Задача 5. Счётчик Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции
# from typing import Callable, Any
# import functools
#
# def counter(func: Callable) -> Callable:
#     """ Декоратор считает, сколько раз звызывалась декорируемая функция"""
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         wrapped_func.count += 1
#         result = func()
#         print('\nФункция {func} запускалась: {count} раз(а):'.format(
#             func=func.__name__, count=wrapped_func.count))
#         return result
#     wrapped_func.count = 0 # Важно! Т.к. wrap это тоже класс, просто через точку добавляем ему атрибут - счетчик.
#     # Если счетчик вынести за wraper то он его не увидит (будет за пределами видимости). Причем добавляем его после завершения
#     # функции а не в начале, как обычно!!
#
#     return wrapped_func
#
# @counter
# def test():
#     print('Hallo!')
# for _ in range(3):
#     test()
========================================================================================================================
MRO - metod resolution order(Порялок наследования методотов). Множественное наследование (алгоритм: C3 superclass linearization)
Сначало смотрится методы наследника, зате его родительские классы слева направо и в конце супер-класс
Если у родительских классовтоже несколько родителей, то смотрятся по одному родителю, стоящему первым в списке по очереди
Class Main
Class A(Main)
Class B(Main)
class M1(A, B)
class M2(A, D)
class M3(C,D, E)
class Z(M1, M2, M3)
Тогда MRO = Z -> M1 -> A -> M2 - B -> M3 -> C -> D -> E -> Main

# from typing import List
#
# class Person:
#     """Базовый класс человек"""
#     def __init__(self, name: str, age: int) -> None:
#         self.__name = name
#         self.__age = age
#
# class Employee(Person):
#     """Работник, дочерний класс от Person """
#     def __init__(self, name: str, age: int) -> None:
#         super().__init__(name, age)
#         self.__salary = 20000
#
#     def get_salary(self) -> int:
#         """Метод для получения размера зарплаты"""
#         return self.__salary
#
# class Parent(Person):
#     """Родитель, дочерний класс от Person """
#     def __init__(self, name: str, age: int) -> None:
#         super().__init__(name, age)
#         self.__kids = ['Tom', 'Bob']
#
#     def get_kids(self) -> List[str]:
#         return self.__kids
#
# class Citizen(Parent, Employee): # Множественное наследование. Через запятую указываем классы, от которых хотим наследовать
#     """Житель является и родителем и работником"""
#     pass
#
# my_citizen = Citizen(name='Anton', age=30)
# print(my_citizen.get_salary())
# print(my_citizen.get_kids())
#
# print(my_citizen.__class__.__mro__) # Так можно посмотреть порядок наследования методов и атрибутов класса

Задача 1. Снова роботы.реализует все необходимые классы роботов. Сущности «Робот» и «Может летать» должны быть вынесены
в отдельные классы. Обычный робот имеет модель и может вывести сообщение «Я — Робот». Объект, который умеет летать,
дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать, летать и приземляться.
# class Robot:
#     """Базовый класс Робот"""
#     def __init__(self, model, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.model = model
#
#     def __str__(self) -> str:
#         res = super().__str__()
#         return res + ' {} model {}'.format(self.__class__.__name__, self.model)
#
#     def operate(self) -> None:
#         print('Я - Робот!')
#
# class CanFly:
#     """Базовый класс полет"""
#     def __init__(self, *args, **kwargs) -> None:
#         self.altitude = 0  # метров
#         self.velocity = 0  # км/ч
#
#     def take_off(self) -> None:
#         """Метод взлет"""
#         self.altitude = 100
#         self.velocity = 300
#
#     def fly(self) -> None:
#         """Метод полет"""
#         self.altitude = 5000
#
#     def land_on(self) -> None:
#         """Метод посадка"""
#         self.altitude = 0
#         self.velocity = 0
#
#     def operate(self) -> None:
#         super().operate()
#         print('летим')
#
#     def __str__(self) -> str:
#         res = super().__str__()
#         return res + ' {} высота {} скорость {}'.format(
#             self.__class__.__name__, self.altitude, self.velocity,
#         )
#
# class ScoutDrone(CanFly, Robot):
#     """Класс робот-разведчик. Дочерний класс от классов робот и полет."""
#     def __init__(self, model) -> None:
#         super().__init__(model=model)
#
#     def operate(self) -> None:
#         super().operate()
#         print('Робот ведет разведку с воздуха')
#
#
# class WarDrone(CanFly, Robot):
#     """Класс боевой робот. Дочерний класс от классов робот и полет"""
#     def __init__(self, model, gun) -> None:
#         super().__init__(model=model)
#         self.gun = gun
#
#     def operate(self) -> None:
#         super().operate()
#         print(f'Робот защищает объект при помощи {self.gun}')
#
# print()
# ScoutDrone('a1').operate()
# print()
# WarDrone('r2-d2', 'intellect').operate()

Абстрактный клас и абстрактные методы (квадрат и прямоугольник)
Если класс создается для наследования его методов дочерними классами и не подразумевает создание его инстансов - такой
класс нужно делать абстрактным (наследовать ABC  из модуля abc)
# from abc import ABC, abstractmethod #Abstract Base Class
#
# class Figure(ABC): # Называется абстрактным так как его экземпляры создавать не требуется. Он нужен для наследования основных методов
#     """
#     Абстрактный базовый класс фигура
#
#     Args and attrs:
#         pos_x (int): координата X
#         pos_y (int): координата Y
#         length (int): длина фигуры
#         width (int): ширина фигуры
#     """
#     def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.width = width
#         self.length = length
#
#     @abstractmethod # А благодаря ABC и abstractmethod мы просто не сможем создать инстанс (объект) этого класса
#     def move(self, pos_x: int, pos_y: int) -> None:
#         """Метод изменяет координаты фигуры на плоскости"""
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#
# class ResizableMixin: # Класс примесь. Нужен для изменения размера фигуры. Имеет общий функционал(полиморфизм) для разных фигур(классов ниже).
#     def resize(self, width: int, length: int) -> None:
#         self.width = width
#         self.length = length
#
# class Rectangle(Figure, ResizableMixin):
#     """ Прямоугольник. Родительский класс: Figure"""
#
#     def move(self, pos_x: int, pos_y: int) -> None:# абстрактный метод обязательно должен быть переопределён в дочернем классе!
#         """Метод изменяет координаты фигуры на плоскости"""
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#
# class Square(Figure, ResizableMixin):
#     """Квадрат. Родительский класс: Figure"""
#     def __init__(self, pos_x: int, pos_y: int, size: int):
#         super().__init__(pos_x, pos_y, size, size) #Переопределяем инит родителя, что бы не вносить размер для квадрата дважды
#
#     def move(self, pos_x: int, pos_y: int) -> None: # абстрактный метод обязательно должен быть переопределён в дочернем классе!
#         """Метод изменяет координаты фигуры на плоскости"""
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#
# rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
# rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
# square = Square(pos_x=50, pos_y=70, size=7)
#
# for figure in [rect_1, rect_2, square]: # Увеличиваем размеры фигур в два раза
#     new_size_x = figure.length * 2
#     new_size_y = figure.width * 2
#     figure.resize(new_size_x, new_size_y)

У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:
Автомобили. Они могут ездить только по земле.
Лодки. Ездят только по воде.
Амфибии. Могут перемещаться и по земле, и по воде.
Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.
Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»
# from abc import ABC, abstractmethod
# class Transport(ABC):
#     """
#     Абстрактный базовый класс транспорт.
#
#     Args and attrs:
#         color (str): цвет транспорта
#         speed (int): скорость транспорт
#     """
#     def __init__(self, color, speed) -> None:
#         self.color = color
#         self.speed = speed
#
#
#     # @abstractmethod
#     # def ride_on_earth(self) -> None:
#     #     pass
#     #
#     # @abstractmethod
#     # def ride_on_water(self) -> None:
#     #     pass
#
#     @abstractmethod
#     def horn(self) -> None:
#         pass
#
#     @abstractmethod
#     def __str__(self) -> str:
#         pass
#
# class MediaMixin:
#     """Класс примесь. Нужен для добавления мультимедиа в дочерние классы"""
#     def playing(self) -> None:
#         print("Зачетно качает музло!")
#
# class Car(Transport):
#     """Класс Машина. Родительский класс Transport"""
#
#     def ride_on_earth(self) -> None:
#         """Метод езда"""
#         print('Машина едет по земле!')
#
#     def horn(self) -> None:
#         """Метод сигнал"""
#         print('И сигналит Бип бип бип!!!')
#
#     def __str__(self) -> str:
#         """Метод возвращает текстовое описание объекта"""
#         return 'У {name} цвет {color} и она еде со скоростью {speed}'.format(
#             name=__class__.__name__, color=self.color, speed=self.speed
#         )
#
# class Boat(Transport):
#     """Класс Лодка. Родительский класс Transport"""
#
#     def ride_on_water(self) -> None:
#         """Метод езда"""
#         print('Лодка едет по воде!')
#
#     def horn(self) -> None:
#         """Метод езда"""
#         print('И сигналит Бип бип бип!!!')
#
#     def __str__(self) -> str:
#         """Метод возвращает текстовое описание объекта"""
#         return 'У {name} цвет {color} и она еде со скоростью {speed}'.format(
#             name=__class__.__name__, color=self.color, speed=self.speed
#         )
#
# class Amphibian(Car, Boat, MediaMixin):
#
#     def __str__(self) -> str:
#         """Метод возвращает текстовое описание объекта"""
#         return 'У {name} цвет {color} и она еде со скоростью {speed}'.format(
#             name=__class__.__name__, color=self.color, speed=self.speed
#         )
#
# new_car = Car('red', 200)
# new_boat = Boat('blue', 85)
# new_amphibian = Amphibian('green', 75)
# new_car.ride_on_earth()
# new_car.horn()
# new_boat.ride_on_water()
# new_boat.horn()
# new_amphibian.ride_on_water()
# new_amphibian.horn()
# new_amphibian.playing()
# print(new_car)
# print(new_boat)
# print(new_amphibian)
========================================================================================================================
Контекст-менеджер - объект следящий за инициализацией и финализацией кода. То есть определяет действия, которые должны
происходить до и после выполнения какого то блока кода.
Где используется:
Синхронизация доступа к общим ресурсам
Настройка среды выполнения
Упрапвление подключениями к базе данных
Работа с временными файлами
Обертка соединений по протоколу и т.д.
# import time
#
# class Timer: # Класс для контекст менеджера
#     def __init__(self) -> None:
#         print('\nВремя работы кода')
#         self.start = None
#
#     def __enter__(self) -> 'Timer':# Пишем в кавычках, что вернет метод (если это не коллекция)
#         self.start = time.time() # Засечем время начала работы кода
#         return self #Метод должен вернуть полученные данные в переменную 't1' нащего контекст-менеджера
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool: #Автоматом в методе прописываются 3 аргумента, которые позволяют обрабатывать ошибки
#         print(f'{round((time.time() - self.start), 2)} секунд(ы)') #После окончания работы кода ,выведем время работы блока
#         return True # Если хотим пропускать любые ошибки (ели хоти пропустить только ошибку типа, помно дописать if exc_type is TypeError return True)
#                     # Если метод будет возвращать True/False - то в аннотации пишем 'bool'
#
# with Timer() as t1: # Это наш контекст менеджер
#     print('Первая часть')
#     val_1 = 100 * 100 ** 1000000
#     val_1 += 'ABC'
#
# with Timer() as t2:
#     print('Вторая часть')
#     val_2 = 200 * 200 ** 2000000
#
# with Timer() as t3:
#     print('Третья часть')
#     val_3 = 300 * 300 ** 3000000

Задача 1. Работа с файлом класс File — контекстный менеджер для работы с файлами. Он должен принимать на вход имя файла
и режим чтения/записи и открывать сам файл. В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.
Прописано условия - если файл не найден, создастя новый и откроется для записи
# from typing import TextIO
#
# class File:
#     """
#     Класс для контекст-менеджера
#     :param:
#         file name (str): Имя файла
#         mode (str): Режим чтения/записи
#     """
#     def __init__(self, file_name: str, mode: str) -> None:
#         self.file_name = file_name
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self) -> TextIO:
#         """Метод для входа в контекст менеджер. Возвращает открытый файл."""
#         try:
#             self.file = open(self.file_name, self.mode, encoding='utf-8')
#         except FileNotFoundError:
#             print('Ошибка! Указанный файл не найден\nЗапрошенный файл будет создан автоматически')
#             self.file = open(self.file_name, 'w', encoding='utf-8')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         """Метод закрывает файл после выполнения блока кода"""
#         self.file.close()
#         return True
#
# with File('example.txt', 'r') as file:
#     file.write('Всем привет!')

Прописываем контекст менеджер, который выводит тип ошибки, ее значение и ее след
# class Example:
#     """Класс для контекст-менеджера"""
#     def __init__(self):
#         print('Вызов __init__')
#
#     def __enter__(self) -> bool:
#         """Метод для входа в контекст менеджер"""
#         print('Вызов __enter__')
#         return True
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         """
#         Метод для выхода из контекст-менеджера. Возвращает текстовое описание ошибки при ее наличии
#         :return:
#             exc_type (str):  Тип ошибки
#             exc_val (str): Значение ошибки
#             exc_tb (str): След ошибки
#         """
#         print('Вызов __exit__')
#         if exc_type:
#             print(f'Тип ошибки: {exc_type}\nЗначение ошибки: {exc_val}\n"След" ошибки:{exc_tb}') # Тут выводим все три параметра: тип ,значение и след
#         return True  # первый вариант без этой строки, второй с этой строкой
#
# my_obj = Example()
#
# with my_obj as obj:
#     print('Код внутри первого вызова контекст менеджера')
#     with my_obj as obj2:
#         raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

Декораторы setter и property. Setter нужен для установки атрибута а utnnth для получения инфы о нем
# class Person:
#     """
#     Базовый класс описывающий служащего
#
#     Args:
#         name(str): Передается имя служащего
#         age(int): Передается возраст служащего
#     """
#     def __init__(self, name: str, age: int):
#         self._name = name # Одно подчеркивание означает, что атрибут можно использовать в дочернем классе
#         self.age = age # Даже если атрибут без '_' (_age) то в методах нужно указывать с нижнимм подчеркиванием. Иначе попадешь в рекурсию
#
#     def __str__(self) -> str:
#         return f'Имя: {self._name}\nВозраст: {self._age}'
#
#     @property #Декоратор - свойство (для получения инфы о возрасте возраста)
#     def age(self) -> int:
#         """
#         Геттер для получения возраста
#         :return: age
#         :rtype: int
#         """
#         return self._age
#
#     @age.setter# Декоратор-сеттер Для установки возраста. Сначала пишем параметр (age) и через точку дописываем 'setter'
#     def age(self, age: int) -> None: # Важно!!! Сеттер обязательно идет после property (не до!!!)
#         """
#         Сеттер для установки возраста
#         :param age: int
#         :return: age
#         """
#         if age in range(1, 90):
#             self._age = age
#         else:
#             raise Exception('Недопустимый возраст')
#
#     @property
#     def name(self) -> str:
#         """
#         Геттер для получения имени
#         :return: name
#         :rtype: str
#         """
#         return self._name
#
# tom = Person('Tom', 25)
# print(tom)
# print(tom.age)
# tom.age = 36
# print(tom.age)
# print(tom.name)

Задача 1. Транспорт 2 Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс геттерами и
сеттерами для соответствующих атрибутов. Используйте встроенные декораторы. Вот входные данные той задачи:
# from abc import ABC, abstractmethod
# class MusicMixin:
#
#     def play_music(self):
#         print("""
#         I see trees of green
#         Red roses too
#         I see them bloom
#         For me and for you
#         And I think to myself
#         What a wonderful world
#         """)
#
# class Transport(ABC):
#
#     def __init__(self, color, speed):
#         self._color = color
#         self._speed = speed
#
#     @property
#     def color(self):
#         return self._color
#
#     @color.setter
#     def color(self, value):
#         self._color = value
#
#     @property
#     def speed(self):
#         return self._speed
#
#     @speed.setter
#     def speed(self, value):
#         self._speed = value
#
#     @abstractmethod
#     def ride_on_earth(self):
#         pass
#
#     @abstractmethod
#     def ride_on_water(self):
#         pass
#
#     def signal(self):
#         print("Сигнал")
#
# class Car(Transport):
#
#     def ride_on_earth(self):
#         print("Едем по земле")
#
# class Boat(Transport):
#
#     def ride_on_water(self):
#         print("Ходим по воде")
#
#
# class Amphibian(Car, Boat, MusicMixin):
#     pass
#
# amph_transport = Amphibian('blue', 123)
# amph_transport.ride_on_earth()
# amph_transport.ride_on_water()
# amph_transport.play_music()
# print(amph_transport.color)
# amph_transport.color = 'white'
# print(amph_transport.color)

Класс метод (@classmethod) позволяет получать досту ко всему, что есть в классе, изменять любые атрибуты и тд
# class Pet:
#     TOTAL_SOUNDS = 0
#
#     def __init__(self) -> None:
#         self.__legs = 4
#         self.__has_tail = True
#
#     def __str__(self) -> str:
#         tail = 'Да' if self.__has_tail else 'нет'
#         return 'Всего ног: {legs}\nХвост присутствует: {has_tail}'.format(
#             legs=self.__legs,
#             has_tail=tail
#         )
#
# class Cat(Pet):
#     @classmethod # Декоратор позволяет получать доступ ко всему, что есть в классе, вместо атрибута self в скобках пишем cls.
#     def sound(cls) -> None:
#         cls.TOTAL_SOUNDS += 1 #Через cls и точку обращаемся у нужному элементу класса
#         print(cls.TOTAL_SOUNDS)
#         print('Мяу!')
#
# class Dog(Pet):
#     @classmethod
#     def sound(cls):
#         cls.TOTAL_SOUNDS += 1  # Через cls и точку обращаемся у нужному элементу класса
#         print(cls.TOTAL_SOUNDS)
#         print('Гав!')
#
# my_cat = Cat()
# my_cat.sound()
# my_cat.sound()

Задача 2. Математический модуль класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и:
вычисление длины окружности,вычисление площади окружности,вычисление объёма куба,вычисление площади поверхности сферы
# class MyMath:
#     """
#     Класс - аналогия модуля math
#     :return: Any
#     :rtype: float
#     """
#
#     @classmethod
#     def circle_sq(cls, radius) -> float:
#         """Метод возвращает площадь окружности"""
#         s = 3.141592653589793 * (radius ** 2)
#         return s
#
#     @classmethod
#     def circle_len(cls, radius) -> float:
#         """Метод возвращает длину окружности"""
#         p = 2 * 3.141592653589793 * radius
#         return p
#
#     @classmethod
#     def cube_volume(cls, side) -> float:
#         """Метод возвращает объем куба"""
#         v = side ** 3
#         return v
#
#     @classmethod
#     def sphere_sq(cls, radius) -> float:
#         """Метод возвращает площадь поверхности сферы"""
#         s = 4 * 3.141592653589793 * (radius ** 2)
#         return s
#
#     @classmethod
#     def sphere_volume(cls, radius) -> float:
#         """Метод возвращает объем сферы"""
#         v = 4 * 3.141592653589793 / 3 * (radius ** 3)
#         return v
#
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# res_3 = MyMath.cube_volume(side=15)
# res_4 = MyMath.sphere_sq(radius=5)
# res_5 = MyMath.sphere_volume(radius=6)
# print('Длина окружности:', res_1)
# print('Площадь окружности:', res_2)
# print('Объем куба:', res_3)
# print('Площадь поверхности сферы:', res_4)
# print('Объем сферы:', res_5)

Задача 3. Моделирование Для моделирования 3D фигур используются соответствующие 2D-фигуры, а именно квадрат и треугольник.
Вся поверхность 3D-фигуры может храниться в виде списка. Например, для куба это будет [Square, Square, Square, Square, Square, Square]
Квадрат инициализируется длинами сторон, а треугольник — основанием и высотой. Каждая из 2D-фигур умеет находить свои
периметр и площадь, а 3D-фигуры, в свою очередь, могут находить площадь своей поверхности. спользуя входные данные о
фигурах и знания математики, реализуйте соответствующие классы и методы. Для базовых классов также реализуйте геттеры и сеттеры
# from abc import ABC, abstractmethod
#
# class Figure(ABC):
#     """Абстрактный базовый клас фигура"""
#
#     def __init__(self, _length, _base, _height) -> None:
#         self.length = _length
#         self.height = _height
#         self.base = _base
#
#     @abstractmethod
#     def __str__(self) -> str: # Если нужно, что бы методы работали сразу при печати, просто добавляем их в метод __str__
#         """
#         Абстрактный метод возвращает описание фигуры.
#         :return: str
#         """
#         return f'\nФигура: "{Figure.__name__}"\nПериметр: {self.perimetr()}\nПлощадь: {self.square()}'
#
#     @abstractmethod
#     def perimetr(self) -> None:
#         """Абстрактный метод нахождения периметра"""
#         pass
#
#     @abstractmethod
#     def square(self) -> None:
#         """Абстрактный метод нахождения площади"""
#         pass
#
#     @property
#     def length(self) -> int:
#         """Геттер. Возвращает значение атрибута 'длина'."""
#         return self._length
#
#     @length.setter
#     def length(self, value: int) -> None:
#         """Сеттер: Устанавливает значения атрибута 'длина'."""
#         self._length = value
#
#     @property
#     def base(self) -> int:
#         """Геттер. Возвращает значения параметра основание (base)"""
#         return self._base
#
#     @base.setter
#     def base(self, value: int) -> None:
#         """Сеттер: Устанавливает значения атрибута 'основание'."""
#         self._base = value
#
#     @property
#     def height(self) -> int:
#         """Геттер. Возвращает значения параметра 'высота'"""
#         return self._height
#
#     @height.setter
#     def height(self, value: int):
#         """Сеттер: Устанавливает значения атрибута 'высота'."""
#         self._height = value
#
# class Square(Figure):
#     """Клас: Квадрат. Родительский класс: Figure."""
#     def __init__(self, _length: int) -> None: #При переопределении инита = Важно! Не забыть удалить ненужные параметры
#         super().__init__(_length, None, None)
#
#     def __str__(self) -> str: # Если нужно, что бы методы работали сразу при печати, просто добавляем их в метод __str__
#         """
#         Переопределенный метод, возвращает информацию о фигуре.
#         :return: str
#         """
#         info = super().__str__().replace('Figure', 'Квадрат')
#         return info
#
#     def perimetr(self) -> int:
#         """
#         Переопределенный метод нахождения периметра.
#         :rtype: int
#         """
#         result = self._length * 4 # Что бы питон увидел атрибут, сначала нужно написать без "_"(self.length), потом добавляешь "_" в уже подсвеченный атрибут вручную и все работает
#         return result
#
#     def square(self) -> int:
#         """
#         Переопределенный метод нахождения площади.
#         :rtype: int
#         """
#         result = self._length ** 2
#         return result
#
# class Triangle(Figure):
#     """Клас: Треугольник. Родительский класс: Figure."""
#     def __init__(self, _base: int, _height: int):
#         super().__init__(None, _base, _height)
#
#     def __str__(self) -> str:
#         """
#         Переопределенный метод, возвращает информацию о фигуре.
#         :return: str
#         """
#         info = super().__str__().replace('Figure', 'Треугольник')
#         return info
#
#     def perimetr(self) -> int:
#         """
#         Переопределенный метод нахождения периметра.
#         :rtype: int
#         """
#         result = (2 * self._height) + self._base
#         return result
#
#     def square(self) -> float:
#         """
#         Переопределенный метод нахождения площади.
#         :rtype: int
#         """
#         result = (self._base * self._height) / 2
#         return result
#
# class Cube(Square):
#     """Клас: Куб. Родительский класс: Square."""
#
#     def __str__(self) -> str:
#         """
#         Переопределенный метод, возвращает информацию о фигуре.
#         :return: str
#         """
#         info = f'\nФигура: "{"Куб"}"\nПлощадь поверхности: {self.surface_area()}'
#         return info
#
#     def surface_area(self) -> int:
#         """
#         Метод нахождения площади поверхности.
#         :rtype: int
#         """
#         result = 6 * self._length ** 2
#         return result
#
# class Pyramid(Triangle):
#     """Клас: Пирамида. Родительский класс: Triangle."""
#
#     def __str__(self) -> str:
#         """
#         Переопределенный метод, возвращает информацию о фигуре.
#         :return: str
#         """
#         info = f'\nФигура: "{"Пирамида"}"\nПлощадь поверхности: {self.surface_area()}'
#         return info
#
#     def surface_area(self) -> int:
#         """
#         Метод нахождения площади поверхности.
#         :rtype: int
#         """
#         result = (4 * self._base) + (self._height ** 2)
#         return result
#
# square = Square(_length=84)
# triangle = Triangle(_base=6, _height=12)
# cube = Cube(_length=15)
# pyramid = Pyramid(_base=68, _height=152)
#
# for figure in [square, triangle, cube, pyramid]:
#     print(figure)

Задача 4. Дата класс Date, который должен:проверять числа даты на корректность;конвертировать строку даты в объект класса
Date, состоящий из соответствующих числовых значений дня, месяца и года.Оба метода должны получать на вход строку вида
dd-mm-yyyy При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации
# class Date:
#     """Базовый класс: Дата"""
#     def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self) -> str:
#         """Метод возвращает дату в формате строки"""
#         return 'День: {}\tМесяц: {}\tГод: {}'.format(
#             self.day, self.month, self.year
#         )
#
#     @classmethod # Если сэлф не используем, то можно сразу делать его классметодом
#     def is_date_valid(cls, data: str) -> bool:
#         """Метод проверяет корректность даты"""
#         day, month, year = map(int, data.split('-'))
#         return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999
#
#     @classmethod
#     def from_string(cls, data: str) -> 'Date':
#         """Метод возвращает дату в виде объекта класса, преобразованный из строки"""
#         # dmy_list = data.split('-')
#         # day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
#         day, month, year = map(int, data.split('-')) # Можно заменить верхние закомментированные строки на одну такую
#         date_obj = cls(day, month, year)
#         return date_obj
#
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
========================================================================================================================

Контекст менеджер, только теперь загружаемый из contextlib
# from contextlib import contextmanager # Можно загрузить контекст менеджер для "маленького кода"
# from collections.abc import Iterator
# # Контекст-менеджер автоматически добавит в декорируемую функцию методы enter и exit
#
# @contextmanager
# def next_num(num: int) -> Iterator[int]: # Оборачиваем в контекст-менеджер именно генератор (yield) НЕ функцию!!!!
#     print('Входим в функцию')
#     try:
#         yield num + 1 # Код до yield - работает как метод enter, а код после yield работает, как метод exit
#     except ZeroDivisionError as exc:
#         print('Обнаружена ошибка:', exc)
#     finally:
#         print('Здесь код выполнится в любом случае')
#     print('выходим из функции')
#
# with next_num(-1) as next:
#     print('Следующее число = {}'.format(next))
#     print(10 / next)

Таймер, но теперь укороченная версия (не класс). Генератор обернутый в импортирпованный контекст менеджер
# import time
# from contextlib import contextmanager
# from collections.abc import Iterator
#
# @contextmanager
# def timer() -> Iterator:
#     start = time.time()
#     try:
#         yield # Тк ничего присваивать не нужно просто отражаем старт, то бишь себя
#     except Exception as exc:
#         print(exc)
#     finally:
#         print(f'{round((time.time() - start), 2)} секунд(ы)')
#
# with timer() as t1: # Это наш контекст менеджер
#     print('Первая часть')
#     val_1 = 100 * 100 ** 1000000
#     val_1 += 'ABC'
#
# with timer() as t2:
#     print('Вторая часть')
#     val_2 = 200 * 200 ** 1000000
#
# with timer() as t3:
#     print('Третья часть')
#     val_3 = 300 * 300 ** 1000000

Задача 2. Директории
Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет текущую рабочую директорию на
новую. Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок (например, если такого пути не
существует). Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию
# from contextlib import contextmanager
# from collections.abc import Iterator
# import os
#
# @contextmanager
# def in_dir(path: str) -> Iterator:
#     print('<тут все папки из вашего диска C>')
#     cur_path = os.getcwd() # вернет строку, представляющую текущий рабочий каталог (get_Current_Work_Directory)
#     os.chdir(path) # Эта функция меняет текущий рабочий каталог (CHangeDirectory)
#     try:
#         yield
#     except Exception as exc:
#         print('\nОбнаружена ошибка:', exc)
#     finally:
#         os.chdir(cur_path)
#
# with in_dir('C:\\'):
#     print(os.listdir())

Декоратор с аргументами! Для того ,что бы передать аргумент декоратору, сам декоратор нужно обернуть в еще одну функцию
и уже туда передавать аргумент
Важно!!! Ссылка на декорируемую функцию передается напрямую в декоратор, только если декорато был вызван без аргументов
Если же мы хотим использовать декоратор как с аргументами так и без (аргументами по-умолчанию), в таком случае ссылка на
функцию должна быть не обязательным аргументом (делается это добавлением одного нижнего подчеркивания "_" к функии-аргументу)
# import time
# from typing import Callable, Optional, Any
# import functools # Что бы иметь доступ к методу функций если используется обертка в декораторе
#
# def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 0) -> Callable: # Если передали функцию как необязательную,
#     # то и остальные аргументы должны быть именованными (через "="), и передаваться по ключу, для этого в синтаксисе указываем звездочку
#     def timer_decorator(func: Callable) -> Callable: # func - вызываемое. Здесь передаем kwargs и  args т.к. какие то функции будут с аргументами, а какие то нет
#         """
#         Декоратор Выводит время работы декорируемой функции и возвращает ее результат
#         """
#
#         @functools.wraps(func) # С помощью этого декоратора приписываем обертке методы, которые указаны в декорируемой функции
#         def wrapped_func(*args, **kwargs) -> Any: # Аргументы для декорируемой функции передаются ф-ей оберткой (wrapped_func)
#             started_at = time.time()
#             result = func(*args, **kwargs) # !!! Тут пишем именно аргумента не саму декорируемую функцию, пишем со скобками!
#             ended_at = time.time()
#             run_time = round((ended_at - started_at), precision) # в округление передаем переменную, с которой хотим отражать результат
#             print('Затраченное время функции: {} cекунд(ы).'.format(run_time))
#
#             return result
#         return wrapped_func # Возвращаем функцию без скобок (просто обертку, как декоратор)
#     if _func is None: # Если у декоратора не было аргументов, то возвращать нужно обычный декоратор от функции
#         return timer_decorator
#     return timer_decorator(_func)
#
# @timer_with_precision
# def squares_sum() -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#     """
#     Функция нахождения суммы квадратов
#     для каждого N от 0 до 10 000
#     где 0 < N < 10 000
#     :return: Сумма квадратов
#     """
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum(i_num ** 2 for i_num in range(10000))
#     return result
#
# @timer_with_precision(precision=4)
# def cubes_sum(number: int) -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#     """
#         Функция нахождения суммы кубов
#         для каждого N от 0 до 10 000
#         где 0 < N < 10 000
#         :return: Сумма кубов
#         """
#     result = 0
#     for _ in range(number + 1):
#         result += sum(i_num ** 3 for i_num in range(10000))
#
#     return result
#
# my_result = squares_sum() # При использовании декоратора, функцию используем как обычно, в конце пишем скобки
# print('Результат работы функции:', my_result)
# print()
# my_cubes_sum = cubes_sum(200)
# print('Результат работы функции:', my_cubes_sum)
# print()
# print(squares_sum.__doc__) # Выводит документацию функции
# print(squares_sum.__name__) # Выводит имя функции

Задача 1. Повторение кода декоратор do_twice, который повторяет вызов декорируемой функции два раза В этот раз реализуйте
декоратор repeat, который повторяет задекорированную функцию уже n раз (декоратор с аргументами)
# from typing import Callable, Any, Optional
#
# def repeat(_func: Optional[Callable] = None, *, repeat: int = 2) -> Callable: # Делаем функцию не обязательным аргументом
#     def do_twice(func: Callable) -> Callable:
#         """
#         Декоратор. Повторяет дважды декорируемую функцию
#         :param func:
#         :return: Callable
#         """
#         def wrapping_func(*args, **kwargs) -> Any:
#             for _ in range(repeat):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapping_func
#
#     if _func is None: #Если без аргумента, возврашщаем просто обертку
#         return do_twice
#     return do_twice(_func) #Если аргумент был передан, то возвращаем декоратор от функции
#
# @repeat(repeat=4)                         # По умолчанию повторит дважды, или в зависимости от аргумента
# def greeting(name: str) -> None:
#     print('Привет, {name}!'.format(name=name))
#
# greeting('Tom')

Задача 2. Замедление кода 2 Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве
аргумента. По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
как с аргументами, так и без них
# from typing import Callable, Any, Optional
# import functools
# import time
#
# def waiting_args(_func: Optional[Callable] = None, *, wait=3) -> Callable: # Делаем функцию не обязательным аргументом и оборачиваем ее обертку))
#     def waiting(func: Callable) -> Callable:
#         """ Декоратор перед запуском декорируемой ф-ии, ждет несколько секунд. """
#
#         @functools.wraps(func)
#         def wrapped_func(*args, **kwargs) -> Any:
#             print(f'Ждем {wait} секунд(ы)...')
#             time_at_start = time.time()
#             time.sleep(wait)
#             time_at_stop = time.time()
#             print('\nЗапускаем функцию: {func}'.format(func=func.__name__))
#             result = func(*args, **kwargs)
#             print('\nФункция успешно запустилась спустя:',
#                   round((time_at_stop - time_at_start), 2), 'секунд(ы)')
#             return result
#         return wrapped_func #Если без аргумента, возврашщаем просто обертку
#     if _func is None:
#         return waiting
#     return waiting(_func) #Если аргумент был передан, то возвращаем декоратор от функции
#
# @waiting_args(wait=1)
# def test() -> None:
#     """Тестовая функция для проверки декоратора. Выводит простой текст """
#     print('<Тут что-то происходит...>')
# test()
========================================================================================================================
- Декоратор можно использовать для декорации класса: def decorat_time(cls) - в таком случаее вместо self используется cls
- Обычный декоратор класса никак не влияет на его содержимое, он работает с инстансами класса
- если нужно модифицировать поведение самого класса - используется декоратор с аргументом (можно кстати оставлять пустые скобки)
- dir(cls) - получает все методы класса, включая "магические"
- getattr(cls, method_name) - с помощью имени метода, его можно взять в качестве обхекта
- setattr(cls, method_name, decorated_method) - после декорирования метода, необходимо заменить старый на новый

Декоратор класса. Единственное отличие от декоратора функции в том, что вместо параметра "Func" используется "CLS"
Время создания объекта класса (код фиксирует время инициализации объекта)
Так же внутри есть декоратор для всех методов (с использованием getattr() и setattr())
# import functools
# from datetime import datetime
# import time
# from typing import Callable, Any
#
# def createtime(cls):  # Так как в декоратор передаем объект класса а не функцию, то в скобках cls вместо self
#     # Так как это класс метод, аннотацию в имени функции не пишем
#     """Декоратор класса. Выводит время создания инстанса класса."""
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         instance = cls(*args, **kwargs) # Так создается инстанс класса
#         print('Время создания инстанса класса:', datetime.utcnow()) # Метод utcnow выдает текущую дату и время
#         return instance
#     return wrapper
#
# def timer(func: Callable) -> Callable: # func - вызываемое. Здесь передаем kwargs и  args т.к. какие то функции будут с аргкиентами, а какие то нет
#     """
#     Декоратор Выводит время работы декорируемой функции и возвращает ее результат
#     """
#     @functools.wraps(func) # С помощью этого декоратора приписываем обертке методы, которые указаны в декорируемой функции
#     def wrapped_func(*args, **kwargs) -> Any: # Аргументы для декорируемой функции передаются ф-ей оберткой (wrapped_func)
#         started_at = time.time()
#         result = func(*args, **kwargs) # !!! Тут пишем именно аргумента не саму декорируемую функцию, пишем со скобками!
#         ended_at = time.time()
#         run_time = round((ended_at - started_at), 4)
#         print('Затраченное время функции: {} cекунд(ы).'.format(run_time))
#
#         return result
#     return wrapped_func # Возвращаем функцию без скобок
#
# def for_all_methods(decorator: Callable) -> Callable:
#     """
#     Декоратор класса. Получает другой декоратор и
#     применяет его ко всем методам класса.
#     :param decorator:
#     :return: Callable
#     """
#     @functools.wraps(decorator)
#     def decorate(cls):
#         for i_method_name in dir(cls):
#             if i_method_name.startswith('__') is False:
#                 cur_method = getattr(cls, i_method_name) #Тк идем по названиям а не по самим методам,
#                 # нужно взять их атрибуты по их названиям с помощью getattr(). В скобках просто указываем класс, откуда берем метод и его имя
#                 decorated_method = decorator(cur_method)
#                 setattr(cls, i_method_name, decorated_method) # Тут заменяем старый метод(i_method_name) на новый decorated_method, причем именно старый метод, а не переменну, которой метод присовили
#         return cls  # Ну и возвращаем сам класс в конце
#     return decorate
#
# @createtime
# @for_all_methods(timer) # В скобках указываем, каким декоратором необходимо модифицировать методы класса.
# class Functions:
#     def __init__(self, max_num: int) -> None:
#         self.max_num = max_num
#
#     def squares_sum(self) -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#         """
#         Функция нахождения суммы квадратов
#         для каждого N от 0 до 10 000
#         где 0 < N < 10 000
#         :return: Сумма квадратов
#         """
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum(i_num ** 2 for i_num in range(self.max_num))
#
#         return result
#
#     def cubes_sum(self, number: int) -> int: # Эта функция первого класса (как и все остальные, которые не являются высшими
#         """
#         Функция нахождения суммы квадратов
#         для каждого N от 0 до 10 000
#         где 0 < N < 10 000
#         :return: Сумма кубов
#         """
#         result = 0
#         for _ in range(number + 1):
#             result += sum(i_num ** 3 for i_num in range(self.max_num))
#
#         return result
#
# my_func_1 = Functions(max_num=1000)
# # time.sleep(1)
# # my_func_2 = Functions(max_num=2000)
# # time.sleep(1)
# # my_func_3 = Functions(max_num=3000)
# my_func_1.squares_sum()
# my_func_1.cubes_sum(number=2000)

Задача 2. Декорацию знаешь? Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод
в нём. Логирование реализуйте на своё усмотрение
# from datetime import datetime
#
# def logged(func):
#     """Декоратор логирует запуск кода."""
#     def wrapped(*args, **kwargs):
#         print("Запуск функции произошёл в:", datetime.utcnow())
#         return func(*args, **kwargs)
#
#     return wrapped
#
# def decorator(cls):
#     """Декоратор для всех методов класса"""
#     for i_method in dir(cls):
#         if i_method.startswith('__'): # Игнорируем все встроенные методы
#             continue
#         a = getattr(cls, i_method) # Получаем атрибуты наших методов
#         if hasattr(a, '__call__'): # если метод является вызываемым (функцией в классе)
#             decorated_a = logged(a) # декорируем его. Сразу передаем в декоратор logged
#             setattr(cls, i_method, decorated_a) # Заменяем старый метод на новый
#     return cls
#
# @decorator
# class A:
#     """Тестовый класс для проверки работы декоратора"""
#     def test_sum_1(self) -> int:
#         print('Тут метод test_sum_1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
#     def test_sum_2(self) -> int:
#         print('Тут метод test_sum_1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# A().test_sum_1()

Декоратор как класс. Он используется крайне редко и в спецефических места
# from typing import Callable
# import functools
#
# class CountCalls:
#     def __init__(self, func: Callable) -> None: # В классе декораторе, инит всегда должен хранить ссылку на функцию
#         functools.update_wrapper(self, func) # Это вместо wraper для функции
#         self.func = func
#         self.num_calls = 0
#
#     def __call__(self, *args, **kwargs) -> Callable: # Позволяет любому экземпляру этого класса быть вызваным, как будто он функция
#         # Для пример x() это тоже самое, что x.call
#         self.num_calls += 1
#         print('Вызов номер: {num} Функции: {func}'.format(
#             num=self.num_calls, func=self.func.__name__
#         ))
#         return self.func(*args, **kwargs) # Обязательно возвращаем функци с аргументами
#
# @CountCalls
# def say_hallo():
#     print('Hallo!')
#
# say_hallo()
# say_hallo()
# say_hallo()

Задача 1. Права доступа Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к вызываемой
функции, и если нет, то выдаёт исключение PermissionError
# from typing import Callable
# import functools
# def check_permission(permission: str) -> Callable:
#     """
#     Декоратор для проверки прав доступа.
#     Возвращает результат функции либо ошибку прав доступа.
#     """
#
#     def check(func: Callable) -> Callable:
#         @functools.wraps(func)
#         def wrap(*args, **kwargs):
#             try:
#                 if permission in user_permissions:
#                     return func(*args, **kwargs)
#                 else:
#                     raise PermissionError
#             except PermissionError:
#                 print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func}'.format(
#                     func=func.__name__
#                 ))
#         return wrap
#     return check
#
# user_permissions = ['admin']
#
# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')
#
# @check_permission('user_1')
# def add_comment():
#     print('Добавляем комментарий')
#
# delete_site()
# add_comment()

Задача 2. Функция обратного вызова Это функция, которая вызывается при срабатывании определённого события (переходе на
страницу, получении сообщения или окончании обработки процессором). В неё можно передать функцию, чтобы она выполнилась
после определённого события. Это используется, например, в HTTP-серверах в ответ на URL-запросы
# from typing import Callable
#
# app = {}
# def callback(check_route: str) -> Callable: # Это обертка с аргументом (ключем) для обертки))
#     """Декоратор (функция) обратного вызова,
#     вызывается при срабатывании события"""
#     def wrapped(func: Callable) -> Callable:
#         app[check_route] = func # Присваиваем полученному ключу значение в виде декорируемой функции example
#         # и возвращаем
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return wrapped
#
# @callback('//') # Передаем в качестве аргумента ключ для словаря app
# def example():
#     print('Пример функции, которая возвращает ответ сервера')
#     return 'OK'
#
# route = app.get('//') # Пытаемся получить значение по ключу '//' из словаря app
# if route:
#     response = route() # ТК в словаре значением является декорируемая функция example, берем под нее переменную response, вызываем route уже как функцию
#     print('Ответ:', response) # И исполняем функцию в принте
# else:
#     print('Такого пути нет')

Задача 3. Логирование в формате Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме
магических методов) и в который можно передавать формат вывода даты и времени логирования. Пример кода, передаётся формат
«Месяц День Год - Часы Минуты Секунды»
from typing import Callable, Any
from datetime import datetime
import time

# def logged(cls, func, date_format): # В декоратор передаем и класс и методы, что бы можно было использовать все аргументы прямо в нем
#     """Декоратор логирует запуск кода."""
#
#     def wrapped(*args, **kwargs):
#         format = date_format # Берем переменную для формата даты (переданного как аргумент)
#         for sym in format:
#             if sym.isalpha():
#                 format = format.replace(sym, '%' + sym) # Тут заменяем просто буквы на буквы и исмволы, такой формат нужен для strftime()
#         print('- Запускается {n_class}.{func}. Дата и время запуска: {time}'.format(
#             n_class=cls.__name__, func=func.__name__, time=datetime.now().strftime(format) # Передаем формат даты
#         ))
#         start = time.time()
#         result = func(*args, **kwargs)
#         print('- Завершение {n_class}.{func}, время работы = {end_time}s'.format(
#             n_class=cls.__name__, func=func.__name__, end_time=round((time.time() - start), 3)
#         ))
#         return result
#
#     return wrapped
#
# def log_methods(date_format: str) -> Callable:
#     def decorator(cls):
#         """Декоратор для всех методов класса"""
#         for i_method in dir(cls):
#             if i_method.startswith('__'): # Игнорируем все встроенные методы
#                 continue
#             a = getattr(cls, i_method) # Получаем атрибуты наших методов
#             if hasattr(a, '__call__'): # если метод является вызываемым
#                 decorated_a = logged(cls, a, date_format) # декорируем его. Сразу передаем в декоратор logged
#                 setattr(cls, i_method, decorated_a) # Заменяем старый метод на новый
#         return cls
#     return decorator
#
# @log_methods("b d Y - H:M:S")
# class A:
#     """Базовый класс для тестирования декоратора"""
#     def test_sum_1(self) -> int:
#         print('test sum 1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# @log_methods("b d Y - H:M:S")
# class B(A):
#     """Класс для тестирования кода. Родитель: A"""
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Наследник test sum 1")
#
#     def test_sum_2(self):
#         print("test sum 2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()

Задача 4. Весь мир — декоратор… Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая
должна быть декоратором, и даёт возможность любому декоратору принимать произвольные аргументы
from typing import Callable
import functools
#
# def decorator_with_args_for_any_decorator(decorator_to_enhanced) -> Callable:
#     """Декоратор позволяет другому декоратору принимать произвольные документы"""
#     def decorator_maker(*args, **kwargs) -> Callable:
#         def decorator_wrapper(func: Callable) -> Callable:
#             return decorator_to_enhanced(func, *args, **kwargs) # Возвращаем декоратор, который по сути просто функция, возвращающая другую функцию
#         return decorator_wrapper
#     return decorator_maker
#
#
# @decorator_with_args_for_any_decorator
# def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
#     """Шаблон для декоратора"""
#     @functools.wraps(func)
#     def wrapper(*func_args, **func_kwargs) -> Callable:
#         print('Переданные арги и кварги в декоратор:', dec_args, dec_kwargs)
#         return func(*func_args, **func_kwargs)
#     return wrapper
#
#
# @decorated_decorator(100, 'рублей', 200, 'друзей')
# def decorated_function(text: str, num: int) -> None:
#     print("Привет", text, num)
#
#
# decorated_function("Юзер", 101)

Задача 5. Синглтон Синглтон — это порождающий паттерн проектирования, который гарантирует, что у класса есть только один
экземпляр, и предоставляет к нему глобальную точку доступа. Синглтонами мы уже пользовались, к ним относятся, например,
None, True и False. Именно потому, что None является синглтоном, мы можем использовать оператор is — он возвращает True
только для объектов, представляющих одну и ту же сущность
# import functools
#
# def singleton(cls): # Использем cls т.к. будем декорировать целый класс
#     # Аннотацию не пишем так как это cls
#     """
#     Декоратор класса. Позволяет сделать из класса singleton
#     Класс, который может иметь только один инстанс (объект класа)
#     """
#     @functools.wraps(cls) # Т.к. работаем с классом
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance = None # Это кэш (если в нем есть объект класса отдаем его, если нет, то вычисляем
#     return wrapper_singleton
#
# @singleton
# class Example:
#     pass
#
# my_obj = Example()
# my_another_obj = Example()
#
# print(id(my_obj))
# print(id(my_another_obj))
#
# print(my_obj is my_another_obj)
========================================================================================================================
Пространство имен
- Локальное пространство имен (Local namespace) - Это пространство имен содержит локальные имена внутри функции. Оно создается
при вызове функции и продолжается пока функция не вернется (не завершится)
- Глобальное пространство имен (Global namespace) - включает имена из основного кода и имена из импортированных модулей.
Продолжается до завершения скрипта целиком
- Втроенное пространство имен (build-in namespace) - Содержит встроенные функции и имена исключений (list, tuple, sum...)
Поиск в этой области выполняется в последнюю очередь
Области видимости внутри функцй:
 - locale scope (локальная область) - Является самой внутренней областью,которая содержит список локальных имен внутри функции
 - enclosing scope (область всех закрывающих функций) - поиск имени начинается с ближайшей охватывающей области и
перемещается наружу (если внутри функции вложеная функция и в ней не нашлась переменная, поиск перемещаяется на уровень выше)
# def f1():
#     print('Внутри f1 num =', number)
#
# def f2():
#     number = 50 # локальная переменная
#     print('Внутри f2 num =', number)
#
# def f3():
#     def f4():
#         # global number # Так мы можем поменять(использовать) внутри функции глобальную переменную
#         nonlocal number # Так можно использовать имя из области видимости верхней функции
#         number = 10
#         print('Внутри f3/f4 num =', number)
#     number = 30 # enclosing scope
#     print('Внутри f3 num =', number)
#     f4()
#     print('Внутри f3 num =', number)
#
# number = 100  # Глобальная переменная
# print('Global num =', number)
# f1()
# f2()
# f3()
# print('Global num =', number)

Возможные ошибки в пространстве имен:
# test = 1
#
# def f1():
#     print(test) # выдаст ошибку, если ниже объявить переменную test уже внутри функции (ошибка - используется до объявления)
#     test = 7 # Если не объявлять эту переменную, то питон найдет ее в глобальном пространстве имен (перед функцией) и ошибки не будет
#     print(test)
# f1()
#
#
# def f2(): # Не выдаст ошибку, т.к. test есть и в глобальном и в локальном пространстве
#     test = 2
#     print(test)
#
#     if 'test' not in globals():
#         raise Exception
#     if 'test' not in locals():
#         raise Exception

# def func():
#     var = 1
#
#     def f3():
#         par = 2
#         if 'var' not in locals():
#             raise Exception
#         print('var' in locals())
#
#     f3()  # выбьет ошибку, т.к. 'var' в enclosing scope а не в locals
#
#     def f4():
#         par = 4
#         print(var)
#         if 'var' not in locals():
#             raise Exception
#
#     f4()  # Ошибку не выбьет так как мы просто печатаем var, а не делаем операций присваиванья
#
#     def f5():
#         var = 4
#         par = 4
#         print(var)
#         if 'var' not in globals():
#             raise Exception
#
#     f5()  # выбьет ошибку, т.к. 'var' в enclosing scope а не в globals
# func()

Задача 1. Счётчик 2 В этот раз реализуйте тот же декоратор, но уже с использованием знаний о локальных и глобальных
переменных. Два способа 1) используя глобальную переменную count, 2) используя локальную переменную count внутри декоратора
# from typing import Callable, Any
# import functools
#
# count = 0  # Счетчик с глобальной переменной
# def counter(func: Callable) -> Callable:
#     """ Декоратор считает, сколько раз вызывалась декорируемая функция"""
#     count = 0  # Счетчик с локальной переменной
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         global count  # Счетчик с глобальной переменной
#         # nonlocal count  # Счетчик с локальной переменной
#         count += 1
#         result = func(*args, **kwargs)
#         print('\nФункция {func} запускалась: {count} раз(а):'.format(
#             func=func.__name__, count=count))
#         return result
#     return wrapped_func
#
# @counter
# def test():
#     print('Hallo!')
# for _ in range(3):
#     test()
#
# print(dir('.'))  # перечисляет все функции и методы, находящиеся во встроенном пространстве имён в Python.
# print('*' * 100)
# print()
# print(dir(__builtins__))  # перечисляет все встроенные имена объектов во встроенном пространстве имён в Python.
========================================================================================================================

!!! Лямбда функция !!!
# from typing import List
#
# def string_to_int(elem: str) -> int: # Это дословное описание того, что делает lambda в коде ниже
#     return int(elem[4:]) # Т.е получает элемент списка, срезает его с 4го символа и возвращает в виде числа
#
# users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22', 'user100']
#
# sorted_list1 = sorted(users, key=string_to_int) # В кей передается только функция, никакой другой объект
# print(sorted_list1)
#
# # Но код можно записать гараздо короче, в одну строку
sorted_list = sorted(users, key=lambda elem: int(elem[4:])) #Полсле lambda через пробел пишем связанную переменную (elem)
# после ":" прописываем саму функцию (выше ее суть) которая будет работать с переменной
print(sorted_list)

x = lambda a: a + 10 # Лямбду так же можно присвоить переменной, но это дурной тон в питоне.
print(x(5))
def y(a): return a + 10 # Так лямбда связывается непосредственно с идентификатором
print(y(5))

Задача 1. Минимум и максимум Мы знаем, что для нахождения минимального и максимального значений в наборе данных можно
использовать две встроенные функции: min() и max(). И у них тоже можно использовать именованный аргумент key
# from typing import Dict, List
#
# grades: List[Dict] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
# {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
# {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
# {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
# {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
# {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
# {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
# {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
# {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
# ]
#
# print('\nМаксимальное количество очков:', max(grades, key=lambda values: values['score']))
# print('\nМинимальное количество очков:', min(grades, key=lambda values: values['score']))
# print('\nОтсортированный список:', sorted(grades, key=lambda values: values['score']))

!!! Метод __repr__ в Python выдает текстовое или строковое представление сущности или объекта. Функция __str__ в Python
делает то же самое, но ее поведение всё же немного отличается. Она предназначена для создания удобочитаемой версии,
 полезной для отслеживания или отображения информации об объекте. А метод __repr__ предназначен для предоставления
«официального» текстового образа объекта, который можно использовать для воссоздания этого объекта


Задача 2. Сортировка Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами. Затем
создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию
# class Person:
#     """
#     Базовый класс. Описывает человека.
#     :param:
#         name: Имя (str)
#         age: Возраст (int)
#     """
#     def __init__(self, name: str, age: int) -> None:
#         self._name = name
#         self._age = age
#
#     def __repr__(self) -> str:  # Метод __repr__ выдает текстовое или строковое представление сущности или объекта
#         return '\nИмя: {name},\tВозраст: {age}'.format(
#             name=self.name, age=self.age
#         )
#
#     @property
#     def age(self) -> int:
#         """Метод возвращает возраст"""
#         return self._age
#
#     @age.setter
#     def age(self, age: int) -> None:
#         """Метод для установки возраста"""
#         if age in range(1, 90):
#             self._age = age
#         else:
#             raise Exception('Недопустимый возраст')
#
#     @property
#     def name(self) -> str:
#         """Метод возвращает имя."""
#         return self._name
#
#     @name.setter
#     def name(self, name: str) -> None:
#         """Метод для установки имени."""
#         self._name = name
#
# man_1 = Person('Tom', 35)
# man_2 = Person('Jack', 85)
# man_3 = Person('Alice', 26)
#
# people_list = [man_1, man_2, man_3]
#
# print(people_list)
# people_list.sort(key=lambda value: value.age)  # Сортируем по возрастанию
# print(people_list)
# people_list.sort(key=lambda value: - value.age)  # Сортируем по убыванию
# print(people_list)

Функция Map и Filter! Важно: Если используется несколько итерируемых объектов, то число итераций будет столько, сколько
значений в минимальном итерируемом объекте. Т.е. если складываем два списка, то количество итераций будет равно длине
самого короткого списка
- map удобно использовать для ленивых вычислений (если нам не нужны все данные сразу)
- lambda замедляет map, но он все равно быстрее list comprehensions. Можно ускорить map, если вместо лямбды использовать
заранее прописанную функцию (заплатить за скорость красотой кода)
Синтаксис map(int, -- сначала пишем какую функцию применить --, numbers.split(' ') - после запятой пишем, к чему применить)

from typing import List

my_list: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
other_list: List[int] = [2, 7, 1, 8, 2, 8, 1, 8]

result: List[int] = list(map(lambda x, y: x + y, my_list, other_list))  # Сначала переменнные в лямбде, потом в функции пишем, что с
# ними делать. И далее через запятую, указываем итерированные объекты (то есть наши списки).
print(result)
Функция фильтр
result_even: List[int] = list(filter(lambda x: x % 2 == 0, result)) # Фильтр принимает только один итерируемый объект (только один список)
# Дальше пропускает элементы объекта и через лямбду и возвращает только те, которые True. Т.е. если просим отфильтровать
# только четные ,то и вернет он только четные
# и возвращает итератор (нужно выводить на печать через list), лямбда в этом случае просто возвращает только четные элементы
# filter может принимать первым аргументом None, а вторым например map. Тогда он будет возвращать значения, которые являются истиной


# и лямбда и фильтр и map отлично дружат друг с другом:
result = map(lambda num: num * 3, filter(lambda num: num % 2, my_list)) # Тут умножаем на 3 (с помощью лямбды) только нечетные элемента списка my_list
print(list(result))

Задача список животных. Реализовать два способа изменить регистр первых символвлов
# animals = ['cat', 'dog', 'cow']  # Допустим нужно сделать все элементы с большой буквы. Есть два варианта:
#
# new_animals = list(map(lambda elem: elem.capitalize(), animals)) # Первый вариант с лямбдой
# print(new_animals)
# new_animals_2 = [elem.capitalize() for elem in animals] # Второй с лист компрехеншенс
# print(new_animals_2)

Задача 1. Однострочный код Пользователь вводит неопределённое количество чисел. Напишите код, который запрашивает эти
числа и сортирует их по возрастанию. Реализуйте решение в одну строку
# numbers = input('введите числа через пробел: ')
# print(sorted(list(map(int, numbers.split(' ')))))

Задача 2. Однострочный код 2 Пользователь вводит строку, состоящую из любых символов. Напишите код, который выводит на
экран список этих символов, исключая цифры и буквы в верхнем регистре
# string = input('введите строку из чисел и цифр: ')
# print(list(filter(lambda val: not (val.isupper() or val.isdigit()), string)))

Задача 3. Функция reduce Помимо map и filter, есть ещё одна функция — reduce. Она применяет указанную функцию к элементам
последовательности, сводя её к единственному значению
# from functools import reduce
# from typing import List
#
# def my_add(a: int, b: int) -> int:
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result
#
# numbers: List[int] = [0, 1, 2, 3, 4]
#
# print(reduce(my_add, numbers))
Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:
# def check_was(a, b):
#     if isinstance(a, str):  # обработаем первый элемент отдельно
#         a = int(a.count('was'))
#     result = a + int(b.count('was'))
#     return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка
#
# sentences = [
#     "Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
#     "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic", "or had been"
# ]
#
# print(reduce(check_was, sentences))

Специальная переменная __name__. Если прописать проверку if __name__ == '__main__', то можно запускать отдельные функции и методы из
импортированного файла.pu иначе будет выполняться весь основной код из импортированного модуя (питон так работает). Эта проверка
прописывается как в основно (исполняемом) файле, так и в импортированном
# from functools import reduce
# def check_was(a, b):
#     if isinstance(a, str):  # обработаем первый элемент отдельно
#         a = int(a.count('was'))
#     result = a + int(b.count('was'))
#     return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка
#
# sentences = [
#     "Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
#     "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
#     "or had been"
# ]
# if __name__ == "__main__":
#     print(reduce(check_was, sentences))

Задача 1. Новые списки Напишите код, который создаёт три новых списка. Вот их содержимое:Каждое число из списка floats
возводится в третью степень и округляется до трёх знаков после запятой. Из списка names берутся только те имена, в которых
есть минимум пять букв Из списка numbers берётся произведение всех чисел
# from typing import List
# from functools import reduce
#
# floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
#
# if __name__ == '__main__':
#     print('\n1-ый список:', list(map(lambda x: round(x ** 3, 3), floats)))
#     print('2-ой список:', list(filter(lambda elem: len(elem) >= 5, names)))
#     print('3-ий список:', reduce(lambda prev_el, el: prev_el * el, numbers)) # Тут очень подходит reduce, так как он оставляет
#     # только крайнее число в последовательности, а лямбда как раз его умножает на следующий элемент списка (гениально)

Задача 2. И снова zip Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N элементов. Создайте
кортежи из пар элементов списков и запишите их в список results. Не используйте функцию zip. Решите задачу «в одну строку»
(не считая print(results))
# from typing import List
#
# letters: List[str] = ['a', 'b', 'c', 'd', 'e']
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
#
# if __name__ == '__main__':
#     results = list(map(lambda x, y: (x, y), letters, numbers))
#     print(results)

Простые числа одной строкой (с использованием lambda функций)
# print(*list(filter(lambda x: x % 2 != 0 and all(map(lambda i: x % i != 0, range(3, int(x ** 0.5) + 1, 2))) or x == 2, range(2, 1000))))