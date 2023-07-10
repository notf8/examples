# Фрэймворк - это набор готовых библиотек и готовых модулей, типа панель администратора, набор регистрации пользователей и т.д.
# Django - это готовый фреймворк, с огромным набором библиотек
#
#  - HTTP запрос бывает 2-х видов: Get и Post. В себе они содержат голову (Head) и тело (Body)
#  - Для получения инфы с сервера используется Get запрос
#  - Для обновления инфы на сервере используется Post запрос
#  - Host - Указывет, к какому веб приложению нужно обратится на сервере
#  - User-agent - говорит с какого браузера и устройства обращается клиент
#  - Accept - говорит о том, какой язык может понять клиент
# ========================================================================================================================
#
# Простейшее серверное приложение:
# ## (Запустить сервер из командной строки, находясь в директории с файлом: python simple_http_server.py)
# from http.server import HTTPServer, BaseHTTPRequestHandler
#
# APP_HOST = 'Localhost'  # Указываем на каком хосту будет запускаться наш веб-сервер (в это случае, это хост нашей машины = 127.001)
# APP_PORT = 8000  # Указываем на каком порту сервер будет работать
#
# class SimpleGetHandler(BaseHTTPRequestHandler):  # Класс - элементарный обработчик get запросов
#     def _set_handlers(self):
#         self.send_response(200)  # Указываем, какие заголовки должны быть в нашем запросе
#         self.send_header("Content-type", "text/html; charset=utf-8")
#         self.end_headers()
#
#     def _html(self, message):
#         content = (f"<html>"
#                    f"<body>"
#                    f"<h1>{message}</h1>"  # Здесь передаем наш месадж в html код
#                    f"</body>"
#                    f"/html")
#         return content.encode("utf8")  # Кодируем контент в utf8
#
#     def do_GET(self):
#         self._set_handlers()
#         message = "Привет, мир!"  # Создаем нужный нам месадж
#         self.wfile.write(self._html(message))  # Отправляем наш ответ(ответ сервера) клиенту
#
# def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):  # Инициализируем запуск сервера
#     server_address = (APP_HOST, APP_PORT)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()  # Указываем, что сервер необходимо хранить вечно (пока не упадет в ошибку или мы его не выключим)
#
# if __name__ == "__main__":
#     run_server(handler_class=SimpleGetHandler)
# ========================================================================================================================
#
# Компоненты веб приложений и первый запуск DJANGO: Модель MTV
# СУБД (база данных) => Модель => Пердставление => Шаблон
#  - Модель - специальный слой, необходимый для общения с источником данных
#  - Пердставление - Специальная питоновская функция или класс, вызывается при обращении по спец.url и возвращает http ответ
#     Оно преобразует наши http запросы
#  - Шаблон - Это форма представления данных. С помошью нее, можно преобразовывать данные из представления в HTML код и
#     возвращать их клиенту
# ========================================================================================================================
#
# Пишем приложение на DJANGO (все команды можно писать в терминале питона или через CMD перейдя в дирректорию, где будем создавать приложение)
#  - Установка Django: pip install Django==2.2
 - Установка "ToDo": django-admin startproject todo  # Команда создает каркас и все нужные файлы для работы приложения"
#  - Создаем новое приложение: django-admin startapp tasks
#  - Выполняем миграцию наших данных в базу данных: python manage.py migrate
#  - Создаем пользователя для приложения: python manage.py createsuperuser. Django попросит ввести имя пользователя (сделал admin)
#     потом попросит ввести email - можно оставить пустым
#     после попросит пароль (1234), потом попросит ввести более сложный (можно просто пропустить этот ход)
#  - Запускаем сервер: python manage.py runserver
#     Запустится приложение на локальном сервере и порту 8000. Можно пройти и проверить (http://localhost:8000)
#     Важно! Созданый сайт уже с админкой! ЧТо бы ее открыть нужно добавить http://localhost:8000/admin (логин и пароль указывали ранее)
#  - Останоить сервер: CTRL+C
#  - Все обработчики запросов находятся в файле views.py Если мы захолтим поменять наше отображение, код меняем именно там
# ========================================================================================================================
#
#                                         Создание проектов:
# Шаг 1:
# Виртуальное окружение: Нужно для того, что бы можно было установить разные версии фреймворков в один интерпритато питона
# Для примекра, как это работает:
#  - Создаем папку - mkdir project
#  - Переходим в эту папку - cd project
#  - Создаем в ней виртуальное окружение - python -m venv venv  # В конце (venv) указываем как будет называться наше окружение
#  - Активируем окружение - project\my_venv\Scripts\activate.bat
#  - После работы деактивируем окружение - project\my_venv\Scripts\deactivate.bat
# ========================================================================================================================
#
# Шаг 2:
# Создаем приложение advertisement
# Важно! При выкатке на продакшн, все пакеты должны быть подписаны одной версией и лежать в файле requirements.txt
#  - Просто создаем файл requirements.txt в папке проекта (команда из видио "touch" не работает в винде)
#  - Далее в файл записываем все пакеты, которые нам понадобятся (нарпимер Django==2.2, версия пишется через ==)
#  - Установим все необходимое из файла - pip install -r requirements.txt (перед установкой перейти в папку проекта (cd project))
#  - После можно стартовать проект - django-admin startproject board (в конце "board" - это название проекта)
#  - Смотрим структуру папок проекта - tree board (в терминале)
#  - Переходим в папку с проектом (cd board) и выполняем команду python manage.py help
#  - Если ввести название команды после 'help', можно получить справку по команде - python manage.py help startapp
#
# Важно! Веб-приложение и Django - не одно и тоже. В django содержутся пакеты, обеспечивающие клиент-серверное взаимодействие
# в веб-приложении же хранятся формы, файл, шаблоны и т.д. для работы самого веб-приложения
#
#  - Создаем приложение, в котором будет лежать код для доски объявлений - python  manage.py startapp advertisement
#  - Теперь создаем миграцию базы данных (в gjango пердустановлена SQLlite) - python manage.py migrate
# ========================================================================================================================
#
# Шаг 3:
# Теперь конфигурируем проект:
# Что бы не превращать основной файл URLS в корневом проекте 'Board' в мешанинуну УРЛов из разных проектов, нужно инкапсулировать
# все запросы внутри проекта advertisement, и потому просто импортируем файл urls.py (предвароительно создав его) из проекта avertisememnt
#  - Для этого в файл 'urls.py', который лежит в папке board добавим импорт из проекта advertisement:
#     - В строке импорта (from django.urls) дописываем через запятую include
#     - А в переменную urlpatterns (в список) добавим через запятую: path('', include('advertisement.urls'))
#     - После, в папке advertisement создаем файл urls.py
#     - from django.urls import path
#     - from .import views          ## Тут импортируем вьюхи
#      - urlpatterns = [
#         path("", views.advertisement_list, name='advertisement_list')  #Здесь связываем представления advertisement
#       ]                                                                #с корневым каталогом двойными кавычками
#     #Этот запрос соответсвует пустой строке (обращению к 127.001) и будет обработан этим представлением. Именной аргумент
#     # "name" это идентификатор url и должен быть уникальным (и легко запоминающимся)
#
# Теперь открываем файл views в папке advertisement:
#  - Добавим в файл свою функцию:
#     from django.http import HttpResponse
#     def advertisement_list(request, *args, **kwargs):
#         return HttpResponse('<ul>'
#                             '<li>Мастер на час</li>'
#                             '<li>Выведение из запоя</li>'
#                             '<li>Услуги экскаватора-погрузчика</li>'
#                             '</ul>')
#  - Что бы добавить новую страничку с объявлением. Для этого нужно дописать еще один url в urlpatterns, например ‘advertisement/’
#     по аналогии с предыдущим (то есть, если вы хотите добавить отдельную ссылку для адреса http://127.0.0.1:8000/advertisement/
#     вам нужно добавить в urls.py такую строчку path('advertisement/', views.advertisement_detail, name='advertisement_list')
#     и представление (функцию) advertisement_detail во views.py.
#
# Что бы функция в файле views возвращала пердставление (а не шаблон внутри представления), а html код в отдельном шаблоне:
#     def advertisement_list(request, *args, **kwargs):
#         return render(request, 'advertisement/advertisement_list.html', {}) # функция render возвращает объект http response
#  - После изменения функции нужно создать соответствующий шаблон. Они хранятся в директории 'advertisement => templates => advertisement'
#     Просто создаем нужные папки в дирректории и уже внутри создадим файл advertisement_list.html
#  - Далее в файл settings.py в директории board/board добавляем 'advertisement' в список INSTALLED_APPS
#  - Файл settings.py - Это конфигуратор проекта, в нем лежат все переменные ,которые мы будем использовать в проекте
#  - Теперь нужно добавить теги в шаблон, что бы отобразить список объявлений - Это делаем в ранее созданом файле advertisement_list.html.

========================================================================================================================
                                            Работа в убунту
 - Создаем в ней виртуальное окружение - python -m venv venv  # В конце (venv) указываем как будет называться наше окружение
 - Активируем окружение - project\my_venv\Scripts\activate.bat
 - После работы деактивируем окружение - project\my_venv\Scripts\deactivate.bat
 - Если pip не установлен в системе, его нужно установить: sudo apt install -y python3-pip
 - Устанавливаем django (в пайчарме) - pip install django
 - Создаем проект - python -m django startproject mysite (-m означает что мы обращаемся к модулю django)
    В созданом проекте есть файлы:
    asgi.py - нужен для запуска асинхронного сервера джанго
    settings.py - нужен для настройки и управления всем проектом (тут же настраиваются все сторонние приложения)
    urls.py - ссылки, которые обробатывают приложения в django
    wsgi.py - нужен для запуска синхронного сервера
 - Запускаем сервер:
    Переходим в папку с проектом: cd mysite
    Вводим команду для запуска: python manage.py runsrever
========================================================================================================================
                                        Создаем проект (сервер)

Состав проекта:
 - urls.py - В файле хранятся все маршруты
 - settings.py - Там настраивается весь проект. В нем же можно изменить тип базы данных (по умоляанию SQLlight)
 - namage.py - Через него управляется весь проект (через него же мы создавали проект, суперпользователдя и т.д.)
                                        ***********************

 - Создаем в ней виртуальное окружение - python -m venv venv  # В конце (venv) указываем как будет называться наше окружение
 - Активируем окружение - project\my_venv\Scripts\activate
 - Установка django - pip install django
 - После установки замораживаем зависимости (делаем перенапраление) - pip freeze > requirements.txt
 - Стартуем проект - python -m django startproject mysite
 - Кликаем по созданной папке mysite правой клавишей, выбираем mark directory -> as root derictory (для правильного индексирования)
 - Переходим в папку с проектом - cd mysite
 - Запускаем сервер - python manage.py runserver (для остановки сервера используется CTRL + C)
 - Применяем миграции:
    1) Открываем второе окно терминала (тк в первом запущен сервер) и переходим в папку проекта: cd mysite
    2) вводим команду: python manage.py migrate (питон сам предлагает ее после запуска сервера)
 - Работаем с базой данных:
    1) Дважды жмем левый shift, в открыфвшемся окне пишем plugin, открываем 'Plugins', и в поиске маркетплэйса пишем database
    2) В появившемся списке выбираем database navigator, устанавливаем и перезагружаем пайчарм
    3) В браузер БД навигатора кликаем пкм по созданному соединению и отмечаем autocommit иначе в бд не будут заносится изменения
 - Создаем суперюзера - python manage.py createsuperuser (логин: admin, почта пустая, пароль: 1234)
 - Далее в панеле админа можно добавлять/редактировать группы и юсеров, назначать права т.д. Все действия будут сохранены
    в БД проекта



========================================================================================================================

                                    Создаем джанго париложения
В приложениях хранятся отдельные ссылки, сущности и т.д. Делается все в отдельных приложениях для того, что бы эти
сущности и ссылки не конфликтовали друг с другом и можно переносить функциональности приложений внутри проекта (например
в интернет магазине отдельно существуют приложения "корзина", "личный кабинет", "каталог" и т.д

Состав приложения:
 - __init__.py - делает из папки приложения (shopapp) пвайтон пакет
 - admin.py - позволяет описать, какие модели нужно отображать в джанго админке
 - apps.py - Содержит в себе конфигурацию этого приложения
 - models.py - Создан для того, что бы объявлять в нем модели джанго
 - tests.py - Нужен для того, что бы писать в нем тесты нашего проекта
 - views.py - В нем будем создавать функции, которые будут обрабатывать наши вью представления
 - ПАПКА migrations: в ней тоже есть __init__.py (так же делает из нее пайтон пакет), в эту папку будут складываться миграции
                                    ****************************


 - Создаем приложение - python manage.py startapp shopapp
 - Подключаем приожение к проекту - открываем файл apps.py, кликаем по имени класса ShopappConfig пкм и выбираем copy reference
    Открываем settings.py в папке mysite, находим INSTALLED_APPS и туда добаляем новую строчку, которую только что скопировали ("shopapp.apps.ShopappConfig")
 - Создаем новый файл urls.py в папке с приложением shopapp (Для того что бы маршуртизация проекта и приложения были разделены, и можно было создать новое прсотранство имен)
    В файл добавляем импорт: from django.urls import path
    Так же создаем в нем пространстов имен. Создаем переменню: app_name = "shopapp" (имя лучше выбрать аналогиное приложению, что бы потом не путаться)
    Создаем список паттернов для обработки запросов:  urlpatterns = []
 - Подключаем новый urls.py к проекту - Октрываем urls.py в паке mysite, и добавляем в строку импорта include (from django.urls import path, include)
    А в urlpatterns добавляем:  path('shop/', include('shopapp.urls')) # Где 'shop/' - правила роутинга, 'shopapp.urls' - имя импорта маршрутов из нашего приложения
 - Создаем вью функциюю для обработки запроса к нашему приложению - открываем файл views.py в папке shopapp
    В нем добавляем импорт from django.http import HttpResponse,HttpRequest # HttpRequest - нужен для аннотации ответа
    Пишем функцию def shop_index(request:HttpRequest ): return HttpResponse("Пример текстового ответа")
 - Добавляем созданную функцию обработки в наш urls.py , который лежит в папке приложения (shopapp)
    Добавляем в файл импорт: from .views import shop_index               # shop_index - это имя функции обработки, которю только что создали
    В urlpatterns добавляем: path("", shop_index, name="index")
        "" - означает запрос к корневой странице приложения
        shop_index - функция, отвтетственная за обработку этого запроса
        name="index" - имя, через которое можно обращаться по указанному пути к функции обработки (это нужно, так как имя функции может меняться)
========================================================================================================================

                                    Шаблоны в джанго
Документация - https://docs.djangoproject.com/en/4.0/ref/templates/builtins/
{{}} - Вывод переменной в шаблонах джанго

 - Шаблоны в джанго рендерятся на стороне серера и возвращаются пользователю
 - Все шаблоны хранятся в файле setting.py, в строке templates
 - Тег для автозаполнения шаблона - {% lorem %}
 - Шаблоны позволяют передавать доп параметры в теги просто через пробел (без скобок):  {% lorem 3 p %} - значит будет три параграфа
 - Тег {% now 'H:i' %} может вывести время загрузки страницы ('H' и 'i' - форомат: Часы и минуты)
 - Создать переменную в теге: {% now 'l' as current_weekday %}  ('l' - текущий день недели, current_weekday - переменная)
    Далее просто выводим ее: Today is {{current_weekday}}
                                         ************
Создаем шаблоны в приложении:
 - Кликаем пкм по папке с приложением и создаем там папку templates
 - Кликаем пкм по созданой папке и выбираем mark dirrectory as temlates folder (у меня почему-то нет такого варианта выбора на винде)
 - В созданной паке templates создаем папку с таким же названием как у приложения (shopapp) - это нужно, что бы избежать коллизий разных приложений
 - В созаданной папке (shopapp) создаеам HTTML файлыл, например shop-index.html (там пишем какой нить тестовый текс, пока не верстаем особо)
 - переходим в файл views.py (в папке приложения shopapp) и там в одномиенной функции прописываем возврат шаблона
    return render(request, 'shopapp/shop-index.html') - импорт render был изначально, в функцию передаем реквест и путь к шаблону (в пути просто имя приложения и через слэш имя html файла)
                                        ***************
Передать переменную в шаблон:
 - В файле views.py создаем переменню словарь - context = {}
 - Далее эту переменную передаем в функцию рендера (shop_index)) return render(request, 'shopapp/shop-index.html', context=context)
 - импортируем дефолтный таймер в views.py: from timeit import default_timer
 - Далее в словарь добавляем функцию: context =  {"time_running": default_timer(),}
 - Переходим в шаблон (shop-index.html), туда добавляем блок div и в него вписываем: Time running: {{time_running}} -
    обязательно в двойных фигурных, внутри скобок просто имя переменной из файла views.py
                                        ****************
Переопределение шаблонов и добавление новых данных (Важно! Тэги django поддерживает только про версия Pycharm):
 - создавди базовый шаблон в в папке templates/shopapp: base.html
 - в тэг title втавляем {% block title %} Base Title {% endblock %}
 - в тэг body  вставляем {% block body %} Base body {% endblock %}
 - Далее идем в файл shop-index.html: там све удаляем и пишем {% extends 'shopapp/base.html' %}
 - Далее {% block title %} Переименовываем как нам надо {% endblock %}
 - {% block body %} Втавляем все что нам нужно в body {% endblock %}
                                        *******************
Циклы в шаблонах джанго:
 - В файле views.py в функции shop_index создаем список товаров products = [('laptop', 1999),('desktop', 2999),('smartphone', 999),]
 - Передаем этот список в ранее созданый context: context =  {"time_running": default_timer(), "products": products,}
 - Идем в shop-ndex.html и там создаем список в новом блоке div:
    <div>
        <ul>
            {% for name, price in products %}   # Здесь запускаем цикл, похож на обычный питон
                <li>{{ name }} for ${{price}}</li>
                {% empty %}
                No products here            # Этот тег нужен, если вдруг список будет пустым (что бы не делать проверку if
            {% endfor %}                    # Здесь закрываем цикл
        </ul>
    </div>
                                        *********************

Фильты в шаблонах джанго:
 - Длина элемента:
    <li>{{ name }} ({{ name|length}}) for ${{price}}</li>   #Тут в круглых скобках обращаемся к элементу через | пишем фильтр length (прям в цикле)

 - Фильтр по длине элемента:
    <li>{{ name }} for ${{price}}</li>
        {% if name|length_is:'7' %}       # Тут обращаемся к перепенной чере | далее имя фильтра lanth_is:, '7' - проверяемое значение (без пробелов)
            <span> Lucky product </span>  # Тут пишем что вывести, если условие выполнено
        {{% endif %}}                     # Тут закрывающий тег if
                                        ***********************
========================================================================================================================

                                            Работа с базой данных
 - ORM - Objeckt relation mappin (объектно реляционное отображение) - позволяет  высокоуровневых языках представлять данные
    из БВ в виде объектов. Свойства таких объектов соответсвуют столбцам каждой записи
 - QuerySet - это набор данных которые мы запрашиваем из базы данных. Запрос к базе происходит, когда мы добавляем к запросу
    ,all(). QuerySet позволяет ограничивать выгрузку и добавлять разные параметры к запросу и фильтровать выгрузку
                                            *********************
 - Запускаем созданый ранее сервер - python manage.py runserver
 - Переходим на сраницу админа - http://127.0.0.1:8000/admin/
 - создаем шаблон для отрисовки групп на странице:
    - В папке приложения (shopapp), которая в шаблонах создаем новый файл html (groups-list)
    - В созданном файле удаляем всю инфу и наследуем базовый шаблон(который делали раньше): {% extends 'shopapp/base.html' %}
    - Дале добавляем блок тайтл: {% block title %} Groups list {% endblock %}
    - И блок боди: {% block body %} <h1>Groups:</h1> {% endblock %}
 - Создаем вью функцию для его отрисовки:
    - Переходим в файл views.py(все там же, в папке приложения shopapp)
    - Добавляем функцию:
        def groups_list(request: HttpRequest):
            context = {
                "groups": Group.objects.all() # Когда введем значение Group, питон подсветит его красным, щелкаем по "красной лампочке" и выбираем: импортитровать имя из gjango.contribe.auth.model
            }                   # Или можно в файл добавить импорт вручную: from django.contrib.auth.models import Group
            return render(request, 'shopapp/groups-list.html', context=context)
 - Подключаем созданную функцию к urls.py внутри приложения (папка shopapp):
    Добавляем в импорт имя функции: from .views import shop_index, groups_list
    в список urlpatterns, через запятую добавляем: path("groups/", groups_list, name="groups_list"),
 - Возвращаемся в шаблон и в него добьавляем в блок боди:
    <div>
    {% if not groups %}
        <h3>No groups yet</h3>
    {% else %}
        <ul>
            {% for group in groups %}
                <li>{{group}}</li>
            {% endfor %}
        </ul>
    {% endif %}
    </div>
                                            **************************
Вывод информации о связях в группе:
 - Переходим к определеню группы: Перейдем в файл views.py и удерживая ctrl кликаем по Group. (в строке контекста - "groups": Group.objects.all())
 - В открывшемся файле models.py находим инфу о группе (для примера permissions)
 - В шаблоне добавляем в список отображение прав группы. Делается это через обращение через "." (как к обычному объекту)
    <h1>Groups:</h1>
    <div>
    {% if not groups %}
        <h3>No groups yet</h3>
    {% else %}
        <ul>
            {% for group in groups %}
                <li>
                    <div>{{group.name}}</div>
                    <ul>
                        {% for permission in group.permissions.all %} # Когда делаем запрос к .all запрос делается к каждой группе, страница будет грузиться долго
                            <li>                                      # Для этого ниже будем оптимизировать вью функцию
                                {{permission.name}}
                                (<code>{{permission.codename}}</code>) # Абрамляем в тег кода (<code>), так как выводим кодовое название
                            </li>
                        {% endfor %}
                    </ul>
                </li>
            {% endfor %}
        </ul>
    {% endif %}
    </div>
 - Идем и редактируем вьюху, что бы оптимизировать подгрузку из бд:
    Меняем строку ("groups": Group.objects.all()) в таком виде - "groups": Group.objects.prefetch_related('permissions').all()
        prefetch_related('permissions') - таким образом заранее указываем, какое свойство группы подгружать вместе с запросом
        что бы этих запросов было меньше
                                        *************************************

                                        Модели и поля в Джанго
Документация - https://docs.djangoproject.com/en/4.1/topics/db/models/

Созаем собственные поля:
 - Открываем файл models.py
 - Объявляем свою модель - Создаем класс Product
    class Product(models.Model):
        name = models.CharField(max_length=100) # Каждый атрибут класса является отдельным свойством и соответсвует колонке в таблице
        description = models.TextField(null=False, blank=True) # Null - говорим что не может отсутствовать значение, blank - позволяет сохранить пустое значение (не null)

 - Создаем атомарную (малыми шагами) миграцию (одна файл миграции = одна измененная модель):
    В терминале(остановив сервер) в папке проекта (mysite) пишем: python manage.py makemigrations
    Потом вручную проверяем, в папке migrations нет ли ошибок (имя миграции видно после выполнения команды)
    Далее проверяем доступные миграции: python manage.py showmigrations
    Если нашли не выполненные (у нас будет 1 по shopapp ), в терминале пишем: python manage.py migrate
    Далее обновляем таблицы в DB browser и видем, что была создана таблица shopapp_product

 - Создаем новую сущность в таблице (Создаем файлы с командами):
    Создаем новую папку в приложении: кликаем пкм по папке shopapp и создаем дирректорию management/commands
    Далее в этой папке создаем python файлы. Название указываем то, которое будет соответствовать команде: create_products
    Делаем импорт базовой команды: Пишем BaseCommand - в красной лампочке выбираем iport name из django.core.management, после импорта удаляем надпись BaseCommand
    Добавляем импорт: from shopapp.models import Product
    Создаем класс command:
        class Command(BaseCommand):
            """
            Creates new products
            """
            def handle(self, *args, **options):         # Метод определяет логикуу выполнения команды
                self.stdout.write("Create products")

                products_names = [
                    "Laptop",
                    "Desktop",
                    "Smartphone"
                ]

                for product_name in products_names:
                    product, created = Product.objects.get_or_create(name=product_name) # get_or_create не создает заново одинаковые имена
                    self.stdout.write(f"Created product: {product.name}")

                self.stdout.write(self.style.SUCCESS("Products created"))
    Теперь можно создать сущности просто выполнив команду в терминале: python manage.py create_products
                                        ************************************

                                        Свойства полей
Документация - https://docs.djangoproject.com/en/4.1/ref/models/fields/

 - На ту же модель Product добавляем поля (файл models.py):
    class Product(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(null=False, blank=True)
        prie = models.DecimalField(default=0, max_digits=8, decimal_places=2)
            # DecimalField специально используется для работы с деньгами, если использовать float буду погрешности в вычислениях
            # max_digits=8 - количество возможных чисел, decimal_places=2 - сколько цифр займут десятичные после запятой
        discount = models.SmallIntegerField(default=0) # SmallIntegerField - Маленькое положительное число
        created_at = models.DateTimeField(auto_now_add=True) # Поле со временем создания продукта, auto_now_add=True - автоматически сохраняет время создания
 - Потом создаем миграции:
    В папке mysite в терминале пишем: python manage.py makemigrations
    Если уже были продукты до миграции, джанго спросит что делать, так как в поле created_at нет значения по умолчанию
    В открывшемся диалоге джанго предложет вставить текущее время - просто соглашаемся нажав enter
    Не забываем вручную проверить миграции (в папке migrations)
    После проверки пишем в терминале: python manage.py showmigrations
    Видим миграции, и пишем в терминале: python manage.py migrate shopapp # Выполняем миграцию для приложения shopapp

- Отмена миграции (для этого сначала создадим новое поле для примера)
    В моделе создадим новое поле: archived = models.BooleanField(default=False)
    Далее снова пишем: python manage.py makemigrations
    Проверим саму миграцию вручную
    Выпоняем миграцию:python manage.py migrate shopapp
    Делаем откат (нужно будет указать, на какую миграцию будем откатываться): python manage.py migrate shopapp 0002 # В конце команды просто указываем номер миграции
    Если результат не устроил можно снова вернуться к миграции 0003, для этого просто пишем: python manage.py migrate shopapp 0003

 - Создаем шаблон для отрисовки таблицы с продуктами:
    В папке с шаблонами приложения shopapp создаем новый шаблон: пкм по папке templates/shopapp -> создать файл пhtml 'products-list'
    Переопределяем базовый шаблон, как в примерах выше
    Создаем функцию для отрисовки шаблона: Переходим в файл views.py (в папке приложения shopapp)
        в импорт добавим импорт: from .models import Product
        def products_list(request: HttpRequest):
            context = {"products": Product.objects.all(),}                         #Тут запрашиваем все поля из таблицы Products
            return render(request, 'shopapp/products-list.html', context=context)
    Подключаем функцию к маршрутам urls.py (d gfgrt shopapp):
        Добавим импорт через запятую: from .views import shop_index, groups_list, products_list
        В список добавим маршрут: path("products/", products_list, name="products_list"),
    Добавляем в шаблон отрисовки продуктов (shopapp/templates/shopapp/'products-list'), в тэг {% block body %} сами продукты:
        <h1>Products:</h1>
            {% if products %}
                <div>
                {% for product in products %}
                    <div>
                        <p>Name: {{product.name}}</p>
                        <p>Price: {{product.price}}</p>
                        <p>Discount: {% firstof product.discount 'no discount'%}</p> # % firstof % - тэг который берет первое не отрицательное значение либо выводит текстовое сообщение если значения нет

                    </div>
                {% endfor %}
                </div>
            {% else %}
                <h3>No products yet</h3>
            {% endif %}
                                                **************************
                                                Связи между таблицами

 - Создадим новую модель (таблицу) в файле models.py:
    class Order(models.Model):
        delivery_address = models.TextField(null=True, blank=True)           # TextField больше подходит для текстовых полей
        promocode = models.CharField(max_length=20, null=False, blank=True)  # CharField подходит для полей, где будет не много символов
        created_at = models.DateTimeField(auto_now_add=True)
 - Создаем связь между таблицами:
    Для этого в класс Order добавляем переменную user:         # Просто пишем User в скобках, далее пкм по нему, и выбираем import this name из django.contribe
    user = models.ForeignKey(User, on_delete=models.PROTECT)   # on_delete=models.PROTECT - нужен для защиты полей, в случае удаления User
    Сразу делаем миграцию (будет вопрос, что делать с уже существующими записями, выбираем 1 и потом снова пишем 1, как значение по умолчанию для созданой ранее таблицы)
    После этого в таблицу order будет добавлено поле user_id, так как ссылка делается на таблицу product?, а в ней prymary key = id

- Создаем команду, которая будет делать заказ:
    В папке shopapp/menegment/commands создаем новый python файл create_order:
        Импортируем BaseCommand (пишем BaseCommand, пкм по надписи и выбираем import this name из django.core.management) или написать from django.core.management import BaseCommand
        Импортируем User и Order по такому же принципу, как написано выше (просто написать например Order и далее import this name)
            class Command(BaseCommand):
                def handle(self, *args, **options):
                    self.stdout.write("Create order")
                    user = User.objects.get(username="admin")
                    order = Order.objects.get_or_create(
                        delivery_address="ul chalenko, d 17/1",
                        promocode="SALE123",
                        user=user,
                    )
                    self.stdout.write(f"Created order{order}")
    Далее в терминале пишем: python manage.py create_order (команда может не выполниться, если в бд не включен автокоммит)

 - Создаем шаблон для вывода всех заказов:
    Идем в шаблоны (shopapp/templates/shopapp) и создаем там новый html файл: orders-list
    И как обычно расширяем базовый шаблон
        {% extends 'shopapp/base.html' %}

        {% block title %}
            Orders list
        {% endblock %}

        {% block body %}
            <h1>Orders:</h1>
            {% if orders %}
                <div>
                {% for order in orders %}
                    <div>
                        <p>Order by: {% firstof order.user.first_name order.user.username %}</p>
                        <p>Promocode: <code>{{ order.promocode }}</code></p>
                        <p>Delivery address: {{ order.delivery_address }}</p>
                    <div>
                        Products in order:
                        <ul>
                            {% for product in order.products.all %}
                                <li>{{ product.name }} for ${{product.price}}</li>
                            {% endfor %}
                        </ul>
                    </div>
                {% endfor %}
                </div>
            {% else %}
                <h3>No orders yet</h3>
            {% endif %}
        {% endblock %}

    Подключаем новый шаблон к views.py
        from .models import Product, Order
        def orders_list(request: HttpRequest):
            context = {
                "orders": Order.objects.select_related("user").prefetch_related("products").all() # select_related - нужен, кода нужно подгрузить одну связь, к которой ссылаемся
            }                                                        # Что бы не делать лишних запросов в БД, а загрузить все сразу
                                                                     # prefetch_related("products") - сразу подгружаем весь состав заказов (если их будет много)
            return render(request, 'shopapp/orders-list.html', context=context)
    Подключаем функцию к urls.py в папке shopapp:
        path("orders/", orders_list, name="orders_list"),

 - Добавляем продуты в заказ (делаем связь: многие -> многим). Такая связь делается чероез промежуточную таблицу. Этим занимается сам джанго
    Идем в файл models.py и добавляем строку в класс Order:
        class Order(models.Model):
            products = models.ManyToManyField(Product, related_name="orders") # Product - с какой таблицей связываем
            # related_name="orders" - как получаем список заказов с класса Product
    Делаем миграцию как обычно: python manage.py makemigrations -> python manage.py migrate shopapp

 - Создаем команду для обновления заказов:
    В папке shopapp/menegment/commands создаем новый python файл update_order:
    Импортируем BaseCommand (пишем BaseCommand, пкм по надписи и выбираем import this name из django.core.management) или написать from django.core.management import BaseCommand
    Импортируем User и Order по такому же принципу, как написано выше (просто написать например Order и далее import this name)
        class Command(BaseCommand):
            def handle(self, *args, **options):
                order = Order.objects.first()
                if not order:
                    self.stdout.write("No order found")
                    return
                products = Product.objects.all()
                for product in products:
                    order.products.add(product) #Это менеджер связи ManyToMany
                order.save()       # Сохраняем изменения после цикла
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added products {order.products.all()} to order: {order}"
                    )
                )
                                ********************************************

                                            Метаданные моделей
Документация - https://docs.djangoproject.com/en/4.1/ref/models/options/

 - Метакслассы в джанго позволяют просто добавить информацию к моделе (в отличии от метаклассов питона, которые переопределяют поведение классов)
 - Метакласс объявляется внутри существующего класа (что бы существовать в конкретном нейм спейсе)
    class Product(models.Model):
        class Meta:
            ordering = ["name", "price"]              # Эта строка уазывает, по какому полю сортировать продукты, если указать "-name", то будет сортировка в обратном порядке
            db_table = "tech_products"                # Указывает, к какой таблице нужно обращаться за свойствами
            verbose_name_plural = "products"          # Указывает, как будет объявлять продукты во множественном числе
            # (полезно, когда имя модели не сделать во множественном числе, просто добавив букву s в конце
        name = models.CharField(max_length=100)
        description = models.TextField(null=False, blank=True)
        price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
        discount = models.SmallIntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        archived = models.BooleanField(default=False)
        user = models.ForeignKey(User, on_delete=models.PROTECT)
========================================================================================================================

                                            Административный инфтерфейс джанго
Документация - https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
                                            **********************************

                                            Подключаем свои модели к админке
Документация - https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-objects
 - Открываем файл admin.py в папке приложения (shopapp) и импортируем туда модель Product: from .models import Product
 - Регистрируем модель в админке: admin.site.register(Product)
 - Что бы изменить отображение модели, создадим новый класс в том же файле (admin.py)
    class ProductAdmin(admin.ModelAdmin):
        list_display = "pk", "name", "description", "price", "discount" # "pk" - ключ продукта (primary key), остальное понятно (тут пишем, что хотим отоброазить в админке)
 - Подключаем админ модель, к модели, которую регистрируем (через запятую): admin.site.register(Product, ProductAdmin)
 - Делаем имя продукта кликабельным (перейти к деталям сущности), для этого добавим к лассу еще одну строку:
    class ProductAdmin(admin.ModelAdmin):
        list_display = "pk", "name", "description", "price", "discount"
        list_display_links = "pk", "name"
 - Второй способ зарегистрировать модель:
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = "pk", "name", "description", "price", "discount"
        list_display_links = "pk", "name"
                                          ***************************************
                                          Меняем отоброжение в админке:

 - Меням отоброжение ключа и имени продукта в админке. Для этого открываем сам файл с моделями (models.py) и добавляем в
   модель Product строку (переопределяем метод отоброжения):
    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})" # !r - позволяет выделить текст в кавычки (репрезентативный вид)
 - Ограничиваем количество символов в поле description (на случай если описание очень большое):
    Для этого в файле models.py, в той же модели Product просто добавим метод с декоратором проперти:
        @property
        def description_short(self) -> str:
            if len(self.description) < 48:
                return self.description
            return self.description[:48] + "..."
        После этого, не забываем указать это поле (description_short) в файле admin.py, в строке list_display
    Если же нужно этот метод использовать во всей админке а не только в модели Product, можно внести его в файл admine.py
    в таком виде:
        def description_short(self, obj: Product) -> str:
            if len(obj.description) < 48:
                return obj.description
            return obj.description[:48] + "..."
        После этого, не забываем указать это поле (description_short) в файле admin.py, в строке list_display

 - Фильтры и поле поиска:
    Для этого в админской моделе (в файле admin.py) добавляем поле ordering:
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = "pk", "name", "description_short", "price", "discount"
        list_display_links = "pk", "name"
        ordering = "pk",   #Тут должен быть либо список, либо кортеж, поэтому в конце обязательно стоит "," если элемент 1 в списке
        # Если нужно в обратную сторону, просто ставим "-pk"

 - Поля поиска. Для этого все в ту же админмодель добавляем поле search_fields:
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = "pk", "name", "description_short", "price", "discount"
        list_display_links = "pk", "name"
        ordering = "pk",
        search_fields = "name", "description" # Добавляем именно description, тк именно по нему будет поиск
                                    **********************************************

                                    Отображение и редактирование связанных записей:
 - Отображаем связь многие ко многим:
    Для этого идем в файл admin.py и там объявляем соответсвующий класс
    @admin.register(Order)
    class OrderAdmin(admin.ModelAdmin):
        list_display = "delivery_address", "promocode", "created_at", "user_verbose"
        def get_queryset(self, request):                   # Оптимизируем, что бы запрос не делался каждый раз к базе ,что бы отразить пользователя
            return Order.objects.select_related("user")

 - Выводим имя пользователя (либо имя, либо юзернэйм):
    Все в той же админмоделе, в новом классе Order добавляем поле
    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username # Возвращаем либо имя, либо юзернэйм
    после этого не забыть указать в list_display "user_verbose"

 - Отображаем связанные продукты на странице заказа (tabular inline И stackt inline - разница только в отображении)
    Обявляем еще одну админскую модель (в файле admin.py) - ProductInLine
        class ProductInLine(admin.TabularInline):
            model = Order.products.through # Тут обязательно пишем, что продукты через модель закза вытаскивать
    потом в админ моделе OrderAdmin добавлячем поле inlines
        @admin.register(Order)
        class OrderAdmin(admin.ModelAdmin):
            inlines = [
                ProductInLine,
            ]
            list_display = "delivery_address", "promocode", "created_at", "user_verbose"
            def get_queryset(self, request):
                return Order.objects.select_related("user").prefetch_realted("products") # Хорошая практика, что бы оптимизировать подгрузку продуктов
            def user_verbose(self, obj: Order) -> str:
                return obj.user.first_name or obj.user.username
    далее в самой админке на сайте можно посмотреть детали заказа, там же добавить продукт или удалить

 - Отображаем связь продуков с заказами:
    Там же в админ моделях (admin.py), вне самих моделей объявляем новый класс
        class OrderInLine(admin.TabularInline):
            model = Product.orders.through
    Потом в класс ProductAdmin добавляем запись inlines (по аналогии с OrderAdmin):
        @admin.register(Product)
        class ProductAdmin(admin.ModelAdmin):
            inlines = [
                OrderInLine,
            ]
            list_display = "pk", "name", "description_short", "price", "discount"
            list_display_links = "pk", "name"
            ordering = "pk",
            search_fields = "name", "description"
            def description_short(self, obj: Product) -> str:
                if len(obj.description) < 48:
                    return obj.description
                return obj.description[:48] + "..."
                                        *********************************

                                        групировка полей

 - переходим в класс ProductAdmin (admin.py) и добавляем строку fieldsets:
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        inlines = [
            OrderInLine,
        ]
        list_display = "pk", "name", "description_short", "price", "discount"
        list_display_links = "pk", "name"
        ordering = "pk",
        search_fields = "name", "description"
        fieldsets = [
            (None, {                                  # None - означает что секция не именованная
                "fields": ("name", "description"),    # Второй параметр всегда словарь! Здесь указываем, какие поля в секции отображать
            }),
            ("Price options", {
                "fields": ("price", "discount"),      # "fields" - в значениях всегда содержит пару полей (если одно поле, то обязательно поставить ',')
                "classes": ("wide", "collapse"),      # "collapse" - поле всегда будет свернутым, "wide" - отступ от имени поля шире (длиннее)
            }),                                        #
            ("Extra options", {
                "fields": ("archived",),
                "classes": ("collapse",),
                "description": "Extra option. Field 'archived' is for soft delete", # Это параметр для описания поля, принимает обычный текст
            }),
            ]
                                            *****************************************

                                            Групповые действия
Документация - https://docs.djangoproject.com/en/4.1/ref/contrib/admin/actions/

 - Добавим поле 'archived' в ProductAdmin (файл admin.py)
    Для этого просто в строку list_display через запятую 'archived'
 - Далее в той же админке (файл admin.py) объявляем отдельную функцию (вне классов):
    @admin.action(description="Archive products")
    def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet): # Здесь просто пишем аннотации и через пкм импортируем их
        queryset.update(archived=True)
    Далее в классе ProductAdmin добавляем строку в которой указываем созданную функцию
    @admin.register(Product)
        class ProductAdmin(admin.ModelAdmin):
            actions = [mark_archived,]
        
 - Для разархивации тупо копируем функцию, меняем название и в ней меняем значение archived=False
    @admin.action(description="Unarchive products")
    def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
        queryset.update(archived=False)
    И так же добавляем ее в список action в ProductAdmin:
    @admin.register(Product)
            class ProductAdmin(admin.ModelAdmin):
                actions = [mark_archived, mark_unarchived,]
                                        **********************************

                                        Примеси (миксин, mixin)
 - Создадим отдельный питон файл в папке приложения (shopapp) - admin_mixins.py
 - В этом файл создадим отдельный класс (который позволит скачивать csv файл):
    import csv
    from django.db.models import QuerySet
    from django.db.models.options import Options
    from django.http import HttpRequest, HttpResponse

    class ExportAsCSVMixin:
        def export_csv(self, request: HttpRequest, queryset: QuerySet):
            meta: Options = self.model._meta  # Просто пишем от руки, потом ПКМ и импортируем из django models (так получаем все поля моделей)
            field_names = [field.name for field in meta.fields] # Собираем список названий полей в листкомпрехеншен
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = f"attachment; filename={meta}-export.csv"
            csv_writer = csv.writer(response)                      # Записываем инфу в файл ответа
            csv_writer.writerow(field_names)                       # Записываем первой строчкой имена полей (столбцов)
            for obj in queryset:                                   # Записываем в цикле, так как запись 1 объект/за раз
                csv_writer.writerow([getattr(obj, field) for field in field_names])

            return response

        export_csv.short_description = "Export as CSV"             # Создаем описание метода
 - Потом импортируем этот класс в файл админки (admin.py)
    from .admin_mixins import ExportAsCSVMixin
 - Далее подмешиваем этот класс в нужные нам модели:
    class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
 - И теперь добавляем действие в список actions в нужной моделе (именем действия как раз будет имя метода класса):
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
        actions = [
            mark_archived, mark_unarchived, "export_csv"    # Метод миксина указывается именно как текст, в кавычках
        ]
========================================================================================================================
                                        Обработка запросов в Django (midleware)

                                                *******************
                                                Концепция MVC и MTV

Почитать - https://habr.com/ru/company/vivid_money/blog/544856/
В общем и целом обе концепции определяют слои и последовательность обработки данных

 - mvc (model view controller)
    Model - бизнес логика представления данных
    View - Сущность (представление) модели
    Controller - имеет доступ к моделе, изменяет сущности

 - mtv (model template view) как раз применима к django (тк именно view функция работает с данными и моделями)
    Чаще всего в джанго - бизнеслогика отнесена в отдельный слой с моделями
    Model - бизнес логика представления данных
    Templates - шаблоны представления модели
    View - Сущность (представление) модели, обработка данных

                                        ************************
                                            Postman/Insomnia
                                    (Инструменты для отправки запросов)

Postman - https://www.postman.com/ - Основной для тестирования http запросов
Insomnia - https://insomnia.rest/https://insomnia.rest/ - Так же для тестирования http запросов ,но проще postman

 - Скачиваем insomnia
 - Создаем новый запрос (в выпадающем списке перед запросом можно выбрать его тип get/post/и т.д.)
 - вводим адрес: https://httpbin.org/get - вернется гет запрос
 - вводим адрес: https://httpbin.org/post - https://httpbin.org/post
 - Под строкой ввода адреса (иудет изначально написано body) можно выбрать, какие даные отправить  (текст, json и т.д.)

                                    ************************************
                                    Работа с различными http методами

https://httpbin.org/
querysrting - это дополнительные параметры get запроса, которые идут в адресной строке после занка "?"

 - Создаем новый проект в папке проекта mysite: python manage.py startapp requestdataapp
 - Подключаем приложение к проекту: в папке mysite, открываем файл settings.py и в installed app добавляем через запятую
    наше прложение (для этого, в папке приложения открываем файл apps.py и там кликаем ПКМ по названию нашего приложения -> copy reference)
 - Подключаем urls: для этого можно просто скопировать скопировать файл urls.py из прошлого приложения (shopapp) и в нем удалить все лишнее
    Потом идем в файл urls самого проекта (mysite) и в него через запятую добавляем: path('req/', include('requestdataapp.urls')),
 - Создаем в приложении папку шаблонов: ПКМ -> создать директорию -> templates/requestdataapp
 - Создаем новый базовый шаблон в папке templates/requestdataapp: base.html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            {% block Title %}
            {% endblock %}
        </title>
    </head>
    <body>
    {% block body %}
    {% endblock %}
    <br>
    <div>
        HTTP User-Agent {{request.user_agent}} # Этот блок потребуется для подключения middleware
    </div>
    </body>
    </html>

 - Дале создаем новый шаблон request-query-params.html. В нем переопределяем базовый шаблон:
    {% extends 'requestdataapp/base.html' %}

    {% block Title %}
        Demo request params
    {% endblock %}

    {% block body %}
        <h1>Good afternoon, {% firstof request.GET.name 'User' %}</h1> # Тут указываем, какое значение будет по умолчанию, если ничего не вводить после ?
    <div>
        <pre>
            a = '{{ a }}' # Так мы передаем во вью функцию переменные и связываем их с переменными внутри вью функции
            b = '{{ b }}'
            result = '{{ result }}'
        </pre>
    </div>
    {% endblock %}

 - Передать параметр через адресную строку можно добавив в конце "?": ?name=Jhon (вернестя ответ с именем, которое мы передали)
 - Что бы передать до параметры, используем амперсант(&): http://127.0.0.1:8000/req/get/?name=Сергей&a=Foo&b=bar

 - Создаем вью функцию для этого шаблона (в папке приложения requestdataapp, в файле views.py):
    from django.http import HttpRequest, HttpResponse

    def process_get_view(request: HttpRequest) -> HttpResponse: # Тут как обычно пишем HttpRequest и пкм по надписи -> import from django.http
        a = request.GET.get("a", "") # Содержимое GET-запроса это словарь. Потому обращаемся за значениями через обычный метод get (там же указываем значения по умолчанию)
        b = request.GET.get("b", "")
        result = a + b
        context = {
            "a": a,
            "b": b,
            "result": result,
        }
        return render(request, "requestdataapp/request-query-params.html", context=context)

 - Подключаем функцию в urls.py в папке приложения (requestdataapp):
    from django.urls import path
    from .views import process_get_view

    app_name = "requestdataapp"

    urlpatterns = [
        path("get/", process_get_view, name="get_view"),
    ]
                                        **************************************
                                                Выполнение POST запросов

Почитать - https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpRequest.POST
File storage API - https://docs.djangoproject.com/en/4.1/ref/files/storage/

Post запрос используется для передачи параметров на сервер и отправки специальных форм (например вход на сайт - это спец
форма, у которй есть поля для ввода никнейма и пароля. Или например форма используется для отправки файлов)

                                        ***************************************
                                         Создаем форму для ввода данных

- Создадим новый шаблон в папке templates/requestdataapp - user-bio-form.html:
    {% extends "requestdataapp/base.html" %}

    {% block Title %}
        User BIO
    {% endblock %}

    {% block body %}
        <h1>User form</h1>
        <div>
            <form method="post">                                                 # Метод запроса
                {% csrf_token %}                                                 # Токен нужен что бы джанго форму отправил, а не остановил на проверке
                <p>
                    <label for="name_id">Full name</label>                        # Пишем название поял для ввода
                    <input id="name_id" name="name" type="text" maxlength="100">  # Само поле ввода. Обязательно должен быть параметр name у каждого (имя любое можно указать)
                </p>
                <p>
                    <label for="age">Age</label>
                    <input id="age" name="age" type="number" min="1" max="99">    # Само имя и Id не обязаны совпадать
                </p>
                <p>
                    <label for="bio">Bio</label>
                    <textarea name="bio" id="bio" cols="42" rows="5"></textarea>
                </p>

                <button type="submit">                                             # Это кнопа. type="submit" - означает что это кнопка отправки формы
                    Submit
                </button>
            </form>
        </div>
    {% endblock %}

- Создаем вью функцию для этого шаблона (в папке приложения requestdataapp, в файле views.py):
    def user_form(request: HttpRequest) -> HttpResponse:
        return render(request, "requestdataapp/user-bio-form.html",)

- Подключаем функцию в urls.py в папке приложения (requestdataapp):
    from django.urls import path
    from .views import process_get_view, user_form

    app_name = "requestdataapp"

    urlpatterns = [
        path("get/", process_get_view, name="get_view"),
        path("bio/", user_form, name="user-form"),
]
                                        *******************************************
                                            Достаем данные пост запроса напрямую

 - Создаем доп блок if в шаблоне user-bio-form.html (сразу под блоком div):
    {% extends "requestdataapp/base.html" %}
    {% block Title %}
        User BIO
    {% endblock %}

    {% block body %}
        <h1>User form</h1>
        <div>
            <form method="post">
                {% csrf_token %}
                <p>
                    <label for="name_id">Full name</label>
                    <input id="name_id" name="name" type="text" maxlength="100">
                </p>
                <p>
                    <label for="age">Age</label>
                    <input id="age" name="age" type="number" min="1" max="99">
                </p>
                <p>
                    <label for="bio">Bio</label>
                    <textarea name="bio" id="bio" cols="42" rows="5"></textarea>
                </p>

                <button type="submit">
                    Submit
                </button>
            </form>
        </div>

        {% if request.POST %}         # Эта часть шаблона позволяет видеть те данные, которые мы заполнили в форме и опубликовали
            <div>
                <h2>Previous form data:</h2>
                <table>
                    <tr>
                        <td>Full name:</td>
                        <td>{{request.POST.name}}</td>
                    </tr>
                    <tr>
                        <td>Age:</td>
                        <td>{{request.POST.age}}</td>
                    </tr>
                    <tr>
                        <td>Bio:</td>
                        <td>
                            <p>{{request.POST.bio|linebreaks}}</p>  # Фильтр linebreaks сохраняет форматирование формы, например переносы строк
                        </td>
                    </tr>
                </table>
            </div>
        {% endif %}
    {% endblock %}
                                           ************************************

                                        Обработка формы (загрузка файла)
- Создадим новый шаблон в папке templates/requestdataapp - file-upload.html:
    {% extends 'requestdataapp/base.html' %}

    {% block Title %}
      File upload
    {% endblock %}

    {% block body %}
      <h1>Upload file</h1>
      <form method="post" enctype="multipart/form-data"> # Что бы форма принимала файлы
        {% csrf_token %}
        <p>
          <input type="file" name="myfile">
        </p>
        <button type="submit">Upload</button>
      </form>
    {% endblock %}


- Создаем вью функцию для этого шаблона  + ограничение объема файла (в папке приложения requestdataapp, в файле views.py):
    Лучше использовать версию с формами! Она будет ниже, в разделе валидация форм
    # from django.core.files.storage import FileSystemStorage
    # from django.http import HttpRequest, HttpResponse
    # from django.shortcuts import render
    #
    # def handle_file_upload(request: HttpRequest) -> HttpResponse:
    #     link = '<h3><a href="http://127.0.0.1:8000/req/upload/">Выбрать другой файл</a></h3>'
    #     if request.method == "POST" and request.POST.get("myfile"):
    #         myfile = request.FILES["myfile"]
    #         fs = FileSystemStorage()                # Это помошник сохранения в джанго, пишем от руки и через ПКМ импортируем из django.core.files.storage
    #         if myfile.size <= 1048576:              # Добавляем ограничение на объем файла
    #             filename = fs.save(myfile.name, myfile) # Сохраняем файл (он сохранится в корень проекта)
    #             print("Saved file: ", filename)
    #         else:
    #             return HttpResponse(f"<h1>Размер файла превышает 1 мб {link}</h1>", )
    #     return render(request, "requestdataapp/file-upload.html",)

 - Подключаем функцию в urls.py в папке приложения(requestdataapp):
    rom django.urls import path
    from .views import process_get_view, user_form, handle_file_upload

    app_name = "requestdataapp"

    urlpatterns = [
      path("get/", process_get_view, name="get_view"),
      path("bio/", user_form, name="user-form"),
      path("upload/", handle_file_upload, name="file-upload"),
        ]

                                        *********************************

                                                Middleware
                    (Позволяет изменять обработку запроса и ответ ,который будет возвращен)
Документация - https://docs.djangoproject.com/en/4.1/topics/http/middleware/ (тут описаны все встроенные мидлвэры в джанго)
Подкходит для: Фильтрация запросов(проверка), логировать запросы, выполянть подсчет запросов и т.д.

                   Создаем простейший middlewares в виде функции (выводит на экран инфо о система пользователя)

 - Создадим новый python middlewares.py файл в папке с проектом (requestdataapp)
 - Создадим в нем функцию для чтения из запроса user agent и установки его в качестве отдельного поля на объект request:
    from django.http import HttpRequest
    def set_useragent_on_request_middleware(get_response): # Очень похоже на декоратор
        print("Initial call")
        def middleware(request: HttpRequest):
            print("Before get response")
            request.user_agent = request.META["HTTP_USER_AGENT"]
            response = get_response(request)
            print("After get response")
            return response
        return middleware
 - Подключаем созданный middleware в настройках приложения (requestdataapp):
    Кликаем по названию фунции set_useragent_on_request_middleware ПКМ -> copy reference
    Идем в файл settings.py (папка прокта mysite) и добавляем в список MIDDLEWARE через запятую, то что скопировали

                                        Создаем простейший middlewares в виде класса
                            (Класс может хранить в себе какие либо настройки, плюс он может изменяться)

 - В том же файле middlewares.py создадим ккласс:
    class CountRequestsMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response
            self.requests_count = 0
            self.responses_cont = 0
            self.exceptions_count = 0

        def __call__(self, request: HttpRequest):
            self.requests_count += 1                           # Подсчитываем количество запросов
            print("Requests count: ", self.requests_count)
            response = self.get_response(request)
            print("Responses count: ", self.responses_cont)
            self.responses_cont += 1
            return response

        def process_exception(self, request: HttpRequest, exception: Exception): # Это метод для подсчета ошибок возможных
            self.exceptions_count += 1
            print("got", self.exceptions_count, "exceptions so far")
- Подключаем созданный middleware в настройках приложения (requestdataapp):
    Кликаем по названию фунции set_useragent_on_request_middleware ПКМ -> copy reference
    Идем в файл settings.py (папка прокта mysite) и добавляем в список MIDDLEWARE через запятую, то что скопировали


                                    Middleware ограничивающий количество запросов с одного IP
# class RequestThrottling:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.count = 0
#         self.current_time = datetime.now()
#         self.time_to_stop = datetime.now() + timedelta(seconds=+60)
#         self.seconds = 60
#
#     def __call__(self, request: HttpRequest):
#         current_ip = request.META.get('REMOTE_ADDR')
#         check_user = {current_ip: self.count}  # TODO эта переменная существует только в время конкретного запроса
#         # пользователя и после этого она изчезает, храните словарь в атрибуте класса, или в глобальной переменной или
#         # в файлае
#         while self.time_to_stop > self.current_time:  # TODO цикл тут не нужен
#             self.current_time = datetime.now()
#             if check_user[current_ip] <= 5:
#                 response = self.get_response(request)
#                 self.count += 1
#                 print("Проверка количества запросов:", self.count)
#                 return response
#             else:
#                 remain_time_to_repeat = self.time_to_stop - self.current_time
#                 if 60 > remain_time_to_repeat.seconds:
#                     return HttpResponse(f"Количество запросов превышено, повторите попытку через "
#                                         f"{remain_time_to_repeat.seconds} секунд(ы)")
#         else:
#             self.current_time = datetime.now()
#             self.time_to_stop = datetime.now() + timedelta(seconds=+60)
#             response = self.get_response(request)
#             self.count = 0
#             return response
# # TODO  Попробуйте сделать так:
# #  - храним данные по посещениях в словаре
# #  - при запросе смотрим в словарь по ключу с ip, если его нет, создаём запись вида "ip: време доступа", и всё, а если
# #  ключ есть, то получаем время прошлого доступа
# #  - сравниваем текущее время и время последнего запроса, если разница меньше допустимого - возвращаем страницу с
# #  ошибкой. Если разница допустима - обновляем время доступа для этого ip.

========================================================================================================================

                                        Формы в джанго

 - Создаем файл forms.py в папке приложения requestdataapp
 - Импортируем формы из джанго (from django import forms)

 - Создам клас UserBioForm, наследования должны быть от forms.Form (посмотреть, какие поля добавиить, можно в ранее
    созданом одноименном шаблоне в папке templates)
    from django import forms
    class UserBioForm(forms.Form):
        name = forms.CharField(max_length=100)
        age = forms.IntegerField(label="Your age", min_value=1, max_value=120) # Так указываем, что будет написано в строке ввода
        bio = forms.CharField(label="Biography", widget=forms.Textarea) # Виджет меняет отображение формы

 - Теперь редактируем вью функцию (она все там же в файле views.py в папке приложения requestdataapp)
    from .forms import UserBioForm # Не забывааем импортировать созданную форму
    def user_form(request: HttpRequest) -> HttpResponse:
        context = {
            "form": UserBioForm(), # Инициализируем форму (что бы не создавать переменную отдельно)
        }
        return render(request, "requestdataapp/user-bio-form.html", context=context)

 - Потом меняем одноименный шаблон в папке templates
    {% extends "requestdataapp/base.html" %}

    {% block Title %}
        User BIO
    {% endblock %}

    {% block body %}
        <h1>User form</h1>
        <div>
            <form method="post">
                {% csrf_token %}
                {{form.as_p}}               # as_p - означает, что мы хотим отобразить строки как параграфы (так же это может быть список или таблица)

                <button type="submit">
                    Submit
                </button>
            </form>
        </div>

        {% if request.POST %}
            <div>
                <h2>Previous form data:</h2>
                <table>
                    <tr>
                        <td>Full name:</td>
                        <td>{{request.POST.name}}</td>
                    </tr>
                    <tr>
                        <td>Age:</td>
                        <td>{{request.POST.age}}</td>
                    </tr>
                    <tr>
                        <td>Bio:</td>
                        <td>
                            <p>{{request.POST.bio|linebreaks}}</p> # |linebreaks - сохраняет пользовательские переносы текста
                        </td>
                    </tr>
                </table>
            </div>
        {% endif %}
    {% endblock %}

                                **************************************************
                                Валидация форм (прописывается и работает на бэкэнде)
Документация - https://docs.djangoproject.com/en/4.1/ref/forms/validation/

 - Создадим форму для создания нового продукта
 - Идем в приложениее shopapp и создаем там файл forms.py
    from django import forms
    from django.core import validators
    class ProductForm(forms.Form):
        name = forms.CharField(max_length=100)
        price = forms.DecimalField(min_value=1, max_value=100000, decimal_places=2) # decimal_places - количество символов после запятой
        description = forms.CharField(
        label="Product description",
        widget=forms.Textarea(attrs={"rows": 5, "cols": 30}),    # Если после forms.Textarea поставить () в них можно будет добавлять свои свойства, без скобок будет поле по умолчанию
        validators=[validators.RegexValidator(        # RegexValidator - это валидатор по регулярным выражениям (проверяет слова)
            regex="great",                            # Проверяет, есть ли в тексте слово"great"
            message="Field must contain word great",  # Так мы выводим сообщение, которе получит пользователь в случае ошибки
                )]
            )

 - Создаем новый шаблон create-product.html для отображения формы (в папке shopapp/templates/shopapp)
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Create product
    {% endblock %}
    {% block body %}
        <h1>Create a new product</h1>
        <div>
            <form method="post">
                {% csrf_token %}
                {{form.as_p}}
                <button type="submit">Create</button>
            </form>
        </div>
        <div>
            <a href="{% url 'shopapp:products_list' %}">
                Back to products list
            </a>
        </div>
    {% endblock %}

 - Подключаем шаблон во вью функции (открываем views.py в папке shopapp)
    from .forms import ProductForm
    def create_product(request: HttpRequest) -> HttpResponse:
        form = ProductForm()
        context = {
            "form": form,
        }
        return render(request, 'shopapp/create-product.html', context=context)

 - Подключаем созданную функцию к urls.py (там же, в папке приложения shopapp)
    from django.urls import path
    from .views import shop_index, groups_list, products_list, orders_list, create_product

    app_name = "shopapp"

    urlpatterns = [
        path("", shop_index, name="shop_index"),
        path("groups/", groups_list, name="groups_list"),
        path("products/", products_list, name="products_list"),
        path("orders/", orders_list, name="orders_list"),
        path("products/create/", create_product, name="product_create"),
    ]
                                    ****************************************
                                    Автогенирация ссылок в django

 - Создаем ссылку со страницы products-list на страницу создания продукта (create_product)
 - Идем в шаблон products-list (приложения shopapp) и добавляем туда еще один блок div
    <div>
        <a href="{% url 'shopapp:product_create' %}"> # после тэг url пишем в кавычках имя приложения, двоеточие (без пробела!!)имя вью функции
            Create a new product                        # Которое указывали при подключении к urls.py
        </a>
    </div>

 - И уже в шаблоне create-product делаем обратную сыслку на странцу шаблон products_list
    <div>
        <a href="{% url 'shopapp:products_list' %}">
            Back to products list
        </a>
    </div>
                                ***************************************************
                Редирект и реверс ссылок + валидация формы на бэкэнд (делается во вью функции, не в шаблоне!)
                                Плюс создание сущности (записи в базе данных)

 - Делаем редирект на стрицу списка продукторв со страницы создания продукта, после нажатия кнопки submit
 - Идем в файл views.py (приложения shopapp) и импортируем из django.shortcuts redirect и revers
 - Дописываем функцию create_product
    from django.shortcuts import render, redirect, reverse
    def create_product(request: HttpRequest) -> HttpResponse:
        if request.method == "POST":                        # Делаем редирект, только если запрос POST
            form = ProductForm(request.POST)                # Предзаполняем данными форму из пост запроса
            if form.is_valid():                             # Если форма валидна, делаем редирект
                # name = form.cleaned_data["name"]          # Так делаем если имена полей отличаются от полей в базе данных
                # Product.objects.create(**form.cleaned_data,) # Если поля называются так же как и в бд, то просто распаковываем форму (старая версия, использовалась без форм)
                form.save()
                url = reverse("shopapp:products_list")       # Тут просто пишем имя приложения и функции, джанго сам подставит ссылку
                return redirect(url)                         # Созданный url передаем в redirect
        else:
            form = ProductForm()                    # Переопределяем форму, если это был GET запрос
        context = {
            "form": form,
        }
        return render(request, 'shopapp/create-product.html', context=context)
                                            *************************************
                                            Модернезируем страниц загрузки файла

- Для этого в папке приложения (requestdataapp/forms.py) создаем новый класс
    class UploadFileForm(forms.Form):
        file = forms.FileField()

- Переходим ко вью функции (requestdataapp/views.py)
    from .forms import UserBioForm, UploadFileForm
    def handle_file_upload(request: HttpRequest) -> HttpResponse:

        link = '<h3><a href="http://127.0.0.1:8000/req/upload/">Выбрать другой файл</a></h3>'

        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                # myfile = request.FILES["myfile"]  # Старая версия, использовалась без форм
                myfile = form.cleaned_data["file"]
                fs = FileSystemStorage()
                if myfile.size <= 1048576:
                    filename = fs.save(myfile.name, myfile)
                    print("Saved file: ", filename)
                    print("File size = ", myfile.size)
                else:
                    return HttpResponse(f"<h1>Размер файла превышает 1 мб {link}</h1>",)
        else:
            form = UploadFileForm()

        context = {
            "form": form
        }
        return render(request, "requestdataapp/file-upload.html", context=context)

 - Потом идем в шаблон (requestdataapp/templates/requestdataapp/file-upload.html) и добавляем форму
    {% extends 'requestdataapp/base.html' %}
    {% block Title %}
      File upload
    {% endblock %}

    {% block body %}
      <h1>Upload file</h1>
      <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}

        <button type="submit">Upload</button>
      </form>
    {% endblock %}

 - Создадим свой собственный валидатор файла в (requestdataapp/forms.py). По аналогии можно и проверку на размер файла
    from  django.core.files.uploadedfile import InMemoryUploadedFile        # Импортируем InMemoryUploadedFile
    from django.core.exceptions import ValidationError                      # Импортируем сообщение об ошибке
    def validate_file_name(file: InMemoryUploadedFile) -> None:             # Именно функцию
        if file.name and "virus" in file.name:
            raise ValidationError("File name should not contain word 'virus'")
 - Подключаем созданную функцию в ранее созданный класс UploadFileForm
    class UploadFileForm(forms.Form):
        file = forms.FileField(validators=[validate_file_name])

                                        **********************************
                                                 ModelForm

Документация - https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
В отличии от создания класса наследника Form, наследование от ModelForm позволяет сгенерировать форму на сонове существующей
уже модели (и такая форма будет содержать гшораздо меньше инфы)

 - Создадим форму Product в (shopapp/forms.py)
    from .models import Product
    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = "name", "price", "description", "discount" # В отличии от прошлого класса, достаточно указать просто наличе полей

=========================================================================================================================

                                            Class based views
                                            *****************
Документация - https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/


 - Класс вью с методом GET
 - Открыть mysite/shopapp/vews.py
 - Импортируем Views (потом ПКМ и импорт из django):  from django.views import View

 - Объявляем класс ShopIndexView и в нем метод get (который полностью заменит функцию shop_index)
    class ShopIndexView(View):
        def get(self, request: HttpRequest) -> HttpResponse:
            links = [
                {"title": "Список продуктов", "address": "products/"},
                {"title": "Список заказов", "address": "orders/"},
            ]
            context = {
                "time_running": default_timer(),
                "links": links
            }
            return render(request, 'shopapp/shop-index.html', context=context)

 - Подключаем созданный класс к mysite/shopapp/urls.py
    from django.urls import path
    from .views import ShopIndexView, products_list, orders_list, create_product, create_order
    app_name = "shopapp"
    urlpatterns = [
        path("", ShopIndexView.as_view(), name="shop_index"),
     - Поключаем класс в mysite/shopapp/urls.py
                         ]

 - Класс вью с методом POST
 - Готовим форму для метода POST (shopapp/forms.py):
    from django.contrib.auth.models import Group
    class GroupForm(forms.ModelForm):
        class Meta:
            model = Group
            fields = ['name']

 - Объявляем класс GroupsListView и в нем метод get и post (shopapp/view.py)
    from .forms import GroupForm
    class GroupsListView(View):
        def get(self, request: HttpRequest) -> HttpResponse:
            context = {
                "groups": Group.objects.prefetch_related('permissions').all(),
                "form": GroupForm(),
            }
            return render(request, 'shopapp/groups-list.html', context=context)

        def post(self, request: HttpRequest):
            form = GroupForm(request.POST)
            if form.is_valid():
                form.save()

            return redirect(request.path)   # Так можно сделать редирект на страницу с группами, потому что на этой же странице есть и сама форма, которую обрабатываем
            # То есть в это вслучае revers прописывать ненужно. Плюс если сделать return render(), то пользоватль сможет опубликовать ту же самую форму дважды

 - Добавляем в шаблон отрисовку формы (shopapp/templates/shopapp/group-list.html)
    # {% extends 'shopapp/base.html' %}
    # {% block title %}
    #     Groups list
    # {% endblock %}
    # {% block body %}
    #     <h1>Groups:</h1>
    #     <div>
    #         <form method="post">
    #             {% csrf_token %}
    #             {{ form.as_p }}
    #             <button type="submit">Create</button>
    #         </form>
    #     </div>
    #     <div>
    #     {% if not groups %}
    #         <h3>No groups yet</h3>
    #     {% else %}
    #         <ul>
    #             {% for group in groups %}
    #                 <li>
    #                     <div>{{group.name}}</div>
    #                     <ul>
    #                         {% for permission in group.permissions.all %}
    #                             <li>
    #                                 {{permission.name}}
    #                                 (<code>{{permission.codename}}</code>)
    #                             </li>
    #                         {% endfor %}
    #                     </ul>
    #                 </li>
    #             {% endfor %}
    #         </ul>
    #     {% endif %}
    #     </div>
    #     <div>
    #         <a href="{% url 'shopapp:shop_index' %}">
    #             Back to the shop
    #         </a>
    #     </div>
    # {% endblock %}

                                            ****************************************
                                            Отображение элментов по первичному ключу

Просмотр деталей товара:
 - Создаем вьюфункцию для отоброжения деталей продукта
 - Нужно добавить в импорт метод get_object_or_404
    from django.shortcuts import render, redirect, reverse, get_object_or_404
    class ProductDetailsView(View):
        def get(self, request: HttpRequest, pk: int) -> HttpResponse:
            product = get_object_or_404(Product, pk=pk) #Так мы возращаем ошибку 404, если будет введен не корректный ID продукта
            context = {
                "product": product,
            }
            return render(request, "shopapp/products-details.html", context=context)

 - Cоздадим шаблон для отрисовки страницы с деталями (shopapp/templates/shopapp/products-details.html)
    {% extends 'shopapp/base.html' %}

    {% block title %}
        Product #{{product.pk}}
    {% endblock %}

    {% block body %}
    <h1>Product <strong>{{ product.name }}</strong></h1>
    <div>
        <div>Description: <em>{{ product.description }}</em></div>
        <div>Price: {{ product.price }}</div>
        <div>Discount: {{ product.discount }}</div>
        <div>Archived: {{ product.archived }}</div>
    </div>
    <div>
        <a href="{% url 'shopapp:products_list' %}">Back to products list</a> # Важно!!! В тегах url имена функций после shopapp: пишем без пробелов
    </div>
    {% endblock %}

 - Подключаем функцию r mysite/shopapp/urls.py
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"), # В адресе указываем, что ожидаем перв ключ "/<int:pk>/"
                                                                                    # В пути специально указываем <int:pk> что бы добавить проверку "на число"
 - Редактируем после этого шаблон списка товаров (что бы добавить ссылку) shopapp/templates/shopapp/products-list.html
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Products list
    {% endblock %}
    {% block body %}
        <h1>Products:</h1>
        {% if products %}
            <div>
            {% for product in products %}
                <div>
                    <p><a href="{% url 'shopapp:product_details' pk=product.pk %}">Name: {{product.name}}</a></p> # Тут именованным аргументом добавляем ключ продкукта
                    <p>Price: {{product.price}}</p>
                    <p>Discount: {% firstof product.discount 'no discount'%}</p>
                </div>
            {% endfor %}
            </div>
        {% else %}
            <h3>No products yet</h3>
        {% endif %}
        <div>
            <a href="{% url 'shopapp:product_create' %}">
                Create a new product
            </a>
        </div>
    {% endblock %}
=========================================================================================================================

                                            ****************************
                                                Class  TemplateView

Документация - https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.TemplateView

 - Перепишем функцию products_list() в mysite/shopapp/views.py
    from django.views.generic import TemplateView
    class ProductsListView(TemplateView):
        template_name = 'shopapp/products-list.html'

        def get_context_data(self, **kwargs): # Если нужно добавлять новые объекты в шаблон, делается это в методе get_context_data, дополняя контекст
            contex = super().get_context_data(**kwargs) # Переопределяем родл класс и закидываем туда кварги (ключ продукта)
            contex["products"] = Product.objects.all()  # Контекстом будет просто словарь с продуктами
            return contex

 - Подключаем новый класс в mysite/shopapp/urls.py
    path("products/", ProductsListView.as_view(), name="products_list"),
========================================================================================================================

                                            ****************************
                                                ListView и DetailView

Generic display views - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/
ListView - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
DetailView - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview

                                                ***********************
                                                        ListView

 - Переработаем класс класс ProductsListView в mysite/shopapp/views.py
    from django.views.generic import ListView
    class ProductsListView(ListView):
        template_name = 'shopapp/products-list.html'
        model = Product                               # Указываем модель, сущности которой надо вытащить
        context_object_name = "products"              # Указываем нужное имя в шаблоне, по которому они будут доступны
        # queryset = Product.objects.filter(archived=False) # Такой метод используем, если нужно отобразить только продукты не в архиве

                                                ***********************
                                                        DetailView

 - Переработаем класс класс ProductsDetailView в mysite/shopapp/views.py
    from django.views.generic import ListView, DetailView
        class ProductDetailsView(DetailView):            # При такой отрисовке, не нужно писать логику поиска объекта, джанго сам вернет ошибку 404 при необходимоти
        template_name = "shopapp/products-details.html"
        model = Product
        context_object_name = "product"

                                ************************************************************
                                Реализуем отображение списка заказов с DetailView и ListView

 - создадим класс OrdersListView mysite/shopapp/views.py
class OrdersListView(ListView):
    queryset = (                                # Пишем сразу queryset, тк у заказов есть связи с продуктами
        Order.objects.select_related("user").
        prefetch_related("products")            # .all() в концуе указыаать не нужно
    )
 - Подключаем новую функцию а mysite/shopapp/urls.py
    path("orders/", OrdersListView.as_view(), name="orders_list"),

 - Важно!!! Нужно переименовать шаблон закзов в mysite/shopapp/templates/shopapp
    Переименовыем шаблон orders-list.html в order_list.html # ТК джанго ищет шаблон автоматом по имени модели Order и добавляет суфикс _list сам

 - Изменяем сам шаблон отрисовки заказов mysite/shopapp/templates/shopapp/order_list.html
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Orders list
    {% endblock %}
    {% block body %}
        <h1>Orders:</h1>
        {% if object_list %}  # Тут заменяем 'orders' на 'object_list' что бы не писать кучу кода с context_object во вью функции проще изменить шаблон
            <div>
            {% for order in object_list %}                                      # И тут
                <div>
                    <p>Order by: {% firstof order.user.first_name order.user.username %}</p>
                    <p>Promocode: <code>{{ order.promocode }}</code></p>
                    <p>Delivery address: {{ order.delivery_address }}</p>
                </div>
                    Products in order:
                    <ul>
                        {% for product in order.products.all %}
                            <li>{{ product.name }} for ${{product.price}}</li>
                        {% endfor %}
                    </ul>
                </div>
            {% endfor %}
            </div>
        {% else %}
            <h3>No orders yet</h3>
        {% endif %}
        <div>
            <a href="{% url 'shopapp:order_create' %}">
                Create a new order
            </a>
        </div>
    {% endblock %}

- создадим класс OrderDetailView в mysite/shopapp/views.py
    class OrderDetailView(DetailView):
        queryset = (                            # В кверисет оставляем то же что и в прошлом классе, тк нужны все данные
            Order.objects
            .select_related("user")
            .prefetch_related("products")
        )

 - Создадим новый шаблон для оотрисовки деталей заказа mysite/shopapp/templates/shopapp/order_detail.html
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Orders # {{ object.pk }} details
    {% endblock %}
    {% block body %}
        <h1>Orders # {{ object.pk }}</h1>
            <div>
                <p>Order by: {% firstof object.user.first_name object.user.username %}</p>
                <p>Promocode: <code>{{ object.promocode }}</code></p>
                <p>Delivery address: {{ object.delivery_address }}</p>
                <div>
                    Products in order:
                    <ul>
                        {% for product in order.products.all %}
                            <li>{{ product.name }} for ${{product.price}}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        <div>
            <a href="{% url 'shopapp:orders_list' %}">Back to orders</a>
        </div>
    {% endblock %}

 - Подключаем новый класс к mysite/shopapp/urls.py
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
========================================================================================================================

                            *******************************************************
                                Использование CreateView и UpdateView

Generic editing views - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/
CreateView - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#createview
UpdateView - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#updateview

                                    ***********************
                                            CreateView

 - Создадим новый класс для создания продукта в mysite/shopapp/views.py
    from django.views.generic import TemplateView, ListView, DetailView, CreateView
    class ProductCreateView(CreateView): # Так же под него создается шаблон. Используется суфикс _form
        model = Product
        fields = "name", "price", "description", "discount" # Для создания можно юзать либо fields (не нужно создавать форму предварительно) либо form_class
        success_url = reverse_lazy("shopapp:products_list") # Импортируется из django urls, его юзаем, тк обычные реверс можно использовать только во вью функции (не в классе)

 - Создадим шаблон для отрисовки mysite/shopapp/templates/shopapp/product_form.html
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Create product
    {% endblock %}
    {% block body %}
        <h1>Create product:</h1>
        <div>
            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Create</button>
            </form>
        </div>
    {% endblock %}

- Подключаем новый класс к mysite/shopapp/urls.py
    path("products/create/", ProductCreateView.as_view(), name="product_create"),

                                    ********************************
                                                UpdateView

 - Создадим новый класс для обновления продукта в mysite/shopapp/views.py
    from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
    class ProductUpdateView(UpdateView):
        model = Product
        fields = "name", "price", "description", "discount" # Можно указывать те поля, которые будем редактировать
        template_name_suffix = "_update_form" # Укажем суфикс шаблона, что бы джанго искал именно шаблон обновления а не создания (его создадим позже)


        def get_success_url(self): # Этот метод нужен, что бы добавить реверс в шаблон обновления
            return reverse(
                "shopapp:product_details",
                kwargs={"pk": self.object.pk},  # На self.object.pk доступен объект, который сейчас обновляется
            )

 - Подключаем новый класс к mysite/shopapp/urls.py
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),

 - Добавим ссылку на страницу детелей продукта в шаблоне mysite/shopapp/templates/shopapp/product_details.html
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Product #{{product.pk}}
    {% endblock %}
    {% block body %}
    <h1>Product <strong>{{ product.name }}</strong></h1>
    <div>
        <div>Description: <em>{{ product.description }}</em></div>
        <div>Price: {{ product.price }}</div>
        <div>Discount: {{ product.discount }}</div>
        <div>Archived: {{ product.archived }}</div>
    </div>
    <div>
        <a href="{% url 'shopapp:products_update' pk=product.pk %}" # Тут нужно указать, какой продукт обноляем. Для джанго это все так же primary key (pk)
        >Update product</a>
    </div>
    <div>
        <a href="{% url 'shopapp:products_list' %}"
        >Back to products list</a>
    </div>
    {% endblock %}

 - Создадим шаблон для отрисовки страницы обновления продукта mysite/shopapp/templates/shopapp/product_update_form.html (что бы джанго не использовал шаблон создания продукта)
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Update product
    {% endblock %}
    {% block body %}
        <h1>Update product:</h1>
        <div>Update
            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Update</button>
            </form>
        </div>
        <div>
            <a href="{% url 'shopapp:product_details' pk=object.pk %}"    # Здесь так же указываем ссылку на детали продукта (то есть возвращаемся на страницу этого же продукта)
            >Back to products #{{ object.pk }}</a>                         # Здесь обращаемся к объект по его ключу
        </div>
    {% endblock %}
========================================================================================================================

                            ************************************************************
                                    Использование DeleteView для удаления объектов

DeleteView - https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#deleteview

 - Создадим новый класс ProductDeleteView в mysite/shopapp/views.py
    from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
    class ProductDeleteView(DeleteView):
        model = Product
        success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):                  # Этот метод нужен, если делаем софт-делит(те помечаем как архивный продукт)
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


- Создадим шаблон для отрисовки страницы удаления продукта mysite/shopapp/templates/shopapp/product_confirm_delete.html
# Имя шаблона складывается из имени объекта и суфикса confirm_delete
    {% extends 'shopapp/base.html' %}
    {% block title %}
        Confirm delete {{ object.name }}
    {% endblock %}
    {% block body %}
        <h1>Are you sure you want to delete {{ object.name }}?</h1>
        <br>
        <div>
            <a href="{% url 'shopapp:product_details' pk=object.pk %}"
            >Back to products</a>
        </div>
        <br>
        <div>
          <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Delete</button>
          </form>
        </div>
    {% endblock %}

- Подключаем новый класс к mysite/shopapp/urls.py
    path("products/<int:pk>/confirm-delete/", ProductDeleteView.as_view(), name="product_delete"),
========================================================================================================================

                                        Аутентификация, авторизация, идентификация
Документация - https://docs.djangoproject.com/en/4.1/topics/auth/
 - Аутентификация - процесс подтверждения личности пользователя - Кто вы?
    Типы аутентификеации:
        1) Парольная
        2) Через cookie (данные хранятся в браузере пользователя)
        3) Через token (тоже может храниться в браузере или передается в http заголовках)
 - Авторизация - процесс, в ходе которого система решает, может ли пользователь выполнять поределенные действия или получать
доступ (проверкуа ролей и разрешений) - Что вы можете делать?
 - Идентификация - процедура в которой проверяются идентификаторы субъекта в системе

                                    ***************************************************
                                            Создадим view для аутентификации
 - Создадим новое приложение в папке с проекетом (my site) - python manage.py startapp myauth
 - Переходим в папку приложения (myauth) открываем apps.py -> ПКМ по названию класса MyauthConfig -> copy reference
 - Подклоючаем новое приложение к проекту - папка mysite -> settings.py -> вставляем в installed aps то что скопировали
    Там же проверяем, подключен ли 'django.contrib.auth', там же
 - Созаем новые папки для шаблонов в папке приложения myauth - templates/myauth
 - В созданной папке создаем базовый шаблон 'base.html'
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}
        {% endblock %}</title>
    </head>
    <body>
    {% block body %}
    {% endblock %}
    </body>
    </html>

 - Создадим шаблон формы входа 'login.html'
    {% extends 'myauth/base.html' %}
    {% block title %}
      Login
    {% endblock %}
    {% block body %}
    <form method="post">
        {% csrf_token %}
        {% if error %}
            <p style="color: red">
              {{ error }}
            </p>
        {% endif %}
        <p>
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required> # required - обязательное поле. name и id могут быть одинаковыми
        </p>
        <p>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" required>
        </p>
          <button type="submit">Login</button> # Тип action не указываем, тк он направлен на это же приложение
    </form>
    {% endblock %}

 - Создадим view функцию для обработки формы myauth/views.py
    from django.http import HttpRequest
    from django.shortcuts import render, redirect
    from django.contrib.auth import authenticate, login


    def login_view(request: HttpRequest):
        if request.method == "GET":
            if request.user.is_authenticated:
                return redirect('/admin')
            return render(request, 'myauth/login.html')
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin")
        return render(request, "myauth/login.html", {"error": "invalid login credentials"})

    # Можно так же сделать на основе classview сделать
    # class MyLoginView(LoginView):
    #     template_name = 'myauth/login.html'
    #     redirect_authenticated_user = True
    #
    #     def get_redirect_url(self): # Тут переопределяем метод для редиректа авторизованного пользователя
    #         redirect_to = "/admin"
    #         return redirect_to

 - Подключим функцию к urls.py который нужно создать в папке myauth
    from django.urls import path
    from .views import login_view

    app_name = "myauth"

    urlpatterns = [
        path("login/", login_view, name="login"),
    ]

 - Не забыть подключить url в основне приложение mysite/urls.py:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('shop/', include('shopapp.urls')),
        path('req/', include('requestdataapp.urls')),
        path('myauth/', include('myauth.urls')),
    ]

                                ******************************************************

                                        Стандартные view для аутентификации
Сверху мы писали функцию самостоятельно. Но есть класс вью которые можно использовать для аутентификации

 - Импортируем loginview в myauth/urls.py
    from django.contrib.auth.views import LoginView
    app_name = "myauth"
    urlpatterns = [
        path("login/", LoginView.as_view(template_name="myauth/login.html"), name="login"), # В скобках вью указываем какой шаблон отрисовать
    ]

 - Изменим шаблон для отрисовки страницы логина myauth/templates/myauth/login.html:
    {% extends 'myauth/base.html' %}
    {% block title %}
      Login
    {% endblock %}
    {% block body %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button> # Тип action не указываем, тк он направлен на это же приложение
    </form>
    {% endblock %}

 - Изменим переадресацию в случае логина в настройках mysite/setting.py в самый конец файла:
    LOGIN_REDIRECT_URL = '/admin/'

 - Что бы пользователь не видел форму авторизации после ее прохождения, изменим view функцию в myauth/urls.py:
    from django.contrib.auth.views import LoginView
    from django.urls import path

    app_name = "myauth"
    urlpatterns = [
        path("login/",
             LoginView.as_view(
                 template_name="myauth/login.html",
                 redirect_authenticated_user=True,
             ),
             name="login",
             ),
    ]

                                            ***********************************************
                                                        Хранение пароля
Хэширование паролей необходимо для безопасности. Хэш функция необратима. Если базу украдут, пароли прочитать не выйдет
Хэширование - это преообразование входящих данных в уникальный набор символов. Хэш нельзя преобразовать оброатно в исходные данные
Соль - случайно сгенерированная строчка, склееваемая с паролем

                                            ************************************************
                                                    Пользователи и сессии, куки
Куки - простые текстовые файлы, хранятся в браузере пользователя и передаются с каждым запросом, в них может быть инфа
о языке пользователя, с чем он работает сейчас и т.д. В зависимости от настроек сервера они могут сгорать как после закрытия
браузера, так и в течении какого то времени (в общем это временное хранилище данных) В них не стоит хранить чувствительные
данные

 - Настроим куки в нашей view функции myauth/views.py
    from django.http import HttpRequest, HttpResponse

    def set_cookie_view(request: HttpRequest) -> HttpResponse: # Функция для настройки куки
        response = HttpResponse("Cookie set")
        response.set_cookie("fizz", "buzz", max_age=3600) # В параметрах обычные строи, время жизни(max_age=) в секундах
        return response

    def get_cookie_view(request: HttpRequest) -> HttpResponse: # Функция для чтения куки
        value = request.COOKIES.get("fizz", "default value") # Тут принцип как и в словарях, если нет значения "fizz", вернется "default value"
        return HttpResponse(f"Cookie value: {value!r}")      # !r - значение в кавычкай выведет

 - Подключим новую функцию к urls (myauth/urls.py)
    from django.contrib.auth.views import LoginView
    from django.urls import path
    from .views import (
        get_cookie_view,
        set_cookie_view,
    )
    app_name = "myauth"
    urlpatterns = [
        path("login/",
             LoginView.as_view(
                 template_name="myauth/login.html",
                 redirect_authenticated_user=True,
             ),
             name="login",
             ),
        path("cookie/get", get_cookie_view, name="cookie-get"),
        path("cookie/set", set_cookie_view, name="cookie-set"),
    ]

                                        *******************************************
                                                    Сессии в джанго

Сессия в джанго - способ хранения информации о пользователе (его запросы, корзину и т.д.) У пользователя хранится только токен
(в куки) а инфа о пользователе только на бэкэнде. Так же токен используется для
Способы хранения сессий:
 - В БД
 - В файле
 - В кэше

 - ЧТо бы использовать сесси в джанго, нужно убедится, что сесси подключены в мидларе mysite/setting.py/middlawre и installed apps

 - Создадим вью функцию для сессий myauth/views.py
    def set_session_view(request: HttpRequest) -> HttpResponse: # Функция для настройки сессий
        request.session["foobar"] = "spameggs"
        return HttpResponse("Session set!")


    def get_session_view(request: HttpRequest) -> HttpResponse: # Функция для чтения сессий
        value = request.session.get("foobar", "default")
        return HttpResponse(f"Session value: {value!r}")

- Подключим новую функцию к urls (myauth/urls.py)
    path("login/",
                 LoginView.as_view(
                     template_name="myauth/login.html",
                     redirect_authenticated_user=True,
                 ),
                 name="login",
                 ),
            path("cookie/get", get_cookie_view, name="cookie-get"),
            path("cookie/set", set_cookie_view, name="cookie-set"),
            path("session/get", get_session_view, name="session-get"),
            path("session/set", set_session_view, name="session-set"),

                                *********************************************************
                                            Logout. Как это работает?

 - Создадим вью функцию для логаута в myauth/views.py
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))

 # Так же можно создать свой класс (его потом так же нужно подключить к url и в пути указать как: MyLogoutView.as_view()
    class MyLogoutView(LogoutView):
        next_page = reverse_lazy("myauth:login") # Использовать просто reverse нельзя, тк он работает только во вью функции

- Подключим новую функцию к urls (myauth/urls.py)
    path("logout/", logout_view, name="logout"),

                                ******************************************************
                                                    Регистрация
Документация - https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm

 - Создадим страницу проверки данных пользователя myauth/views.py
    from django.views.generic import TemplateView
    class AboutMeView(TemplateView):
        template_name = "myauth/about-me.html"

- Создадим шаблон для отрисовки myauth/templates/myauth/about-me.html
    {% extends 'myauth/base.html' %}

    {% block title %}
      About me
    {% endblock %}

    {% block body %}
    <h1>User info</h1>
    {% if user.is_authenticated %}
        <h2>Detail</h2>
        <p>Username: {{user.username}}</p>
        <p>First name: {{user.first_name}}</p>
        <p>Last name: {{user.last_name}}</p>
        <p>Email: {{user.email}}</p>
    {% else %}
        <h2>User is anonymous</h2>
    {% endif %}
    {% endblock %}

 - Подключим новую функцию к urls (myauth/urls.py)
    path("about-me/", AboutMeView.as_view(), name="about-me"),

 - Изменим вью функцию для переадресации пользователя после логина myauth/views.py
    class MyLoginView(LoginView):
        template_name = 'myauth/login.html'
        redirect_authenticated_user = True

        def get_redirect_url(self):                        # Можно вместо метода внести строку LOGIN_REDIRECT_URL = reverse_lazy("myauth:about-me") в файле settings.py в папке mysite
            redirect_to = reverse_lazy("myauth:about-me")
            return redirect_to

 - Создадим класс для регистрации пользователя myauth/views.py
    from django.views.generic import TemplateView, CreateView
    class RegisterView(CreateView):
        form_class = UserCreationForm # # Это нужно импортировать через ПКМ
        template_name = "myauth/register.html"
        success_url = reverse_lazy("myauth:about-me")

        def form_valid(self, form):                       # Переопределяем метод, что бы после регистрации сразу залогинить пользователя
            response = super().form_valid(form)

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1") # Тк в форме два пароля (второй как подтверждение), нам нужно взять один из них (все равно какой)
            user = authenticate(
                self.request,
                username=username,
                password=password
            )
            login(request=self.request, user=user)
            return response

 - Создадим шаблон для отрисовки формы регистрации myauth/templates/myauth/register.html
    {% extends 'myauth/base.html' %}

    {% block title %}
      Register
    {% endblock %}

    {% block body %}
      <h1>Register</h1>
      <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
        <input type="submit" value="Register">
      </form>
    {% endblock %}
 - Подключим новую функцию к urls (myauth/urls.py)
    path("register/", RegisterView.as_view(), name="register"),

                                    ****************************************************
                                                Расширение модели пользователя
Документация - https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model
Важно! Использование собственной модели аутентификации должно произойти до выполнения первой миграции в приложении

 - Создадим новую модель пользователя для расширения инфы о нем myauth/models.py
    from django.contrib.auth.models import User
    from django.db import models

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField(max_length=500, blank=True) # blank=True - поле может быть пустым
        agreement_accepted = models.BooleanField(default=False)

 - Выполним миграции. Команды в терминале: python manage.py makemigrations и python manage.py migrate

 - Доработаем вью, для добавления профиля пользователя myauth/views.py
    from .models import Profile
    class RegisterView(CreateView):
        form_class = UserCreationForm
        template_name = "myauth/register.html"
        success_url = reverse_lazy("myauth:about-me")

        def form_valid(self, form):
            response = super().form_valid(form)
            Profile.objects.create(user=self.object)    # Сюда добавляем создание профиля пользователя (сразу после решистрации)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(
                self.request,
                username=username,
                password=password
            )
            login(request=self.request, user=user)
            return response

 - Ну и отредактируем шаблон для отрисовки myauth/templates/myauth/about-me.html, тк у нас появилась новая модель, обращаться будем к profile
    {% extends 'myauth/base.html' %}

    {% block title %}
      About me
    {% endblock %}

    {% block body %}
    <h1>User info</h1>
    {% if user.is_authenticated %}
        <h2>Detail</h2>
        <p>Username: {{user.username}}</p>
        <p>First name: {{user.first_name}}</p>
        <p>Last name: {{user.last_name}}</p>
        <p>Email: {{user.email}}</p>
        <p>Bio: {{user.profile.bio}}</p>            # Вот тут как раз обращение к новой модели
    {% else %}
        <h2>User is anonymous</h2>
    {% endif %}
    {% endblock %}

                                        **********************************************
                                                Групповые и персональные права
Правва бывают групповые и персональные
Важно! Права начзначенные пользователю напрямую, имеют приоритет над правами, которые назначены пользователю через группу
Типы групп в админке джанго:
 1) Superuser - обладают правами администратора (все разрешения)
 2) Staff - могут заходить в админ панель (а дальше завист от разрешений, которые ему назначены)
 3) Active - пользователь может выполнить вход (не забанен)

 - Создадим команды для назначения прав пользователям в отдельной папке myauth/management/commands в которой создадим файл bind_user.py
    from django.contrib.auth.models import User, Group, Permission
    from django.core.management import BaseCommand


    class Command(BaseCommand):
        def handle(self, *args, **options):
            user = User.objects.get(pk=4)
            group, created = Group.objects.get_or_create(
                name="profile_manager",
            )
            # Тут берем разрешение на просмотр профиля
            permission_profile = Permission.objects.get(
                codename="view_profile",
            )
            # Тут берем разрешение на просмотр логов
            permission_logentry = Permission.objects.get(
                codename="view_logentry",
            )
            # Добавление разрешения в группу
            group.permissions.add(permission_profile)
            # Присоединение пользователя к группе
            user.groups.add(group) # Так как здесь связь многие ко многим - связь выполняется через add()
            # Связать пользователя напрямую с разрешением
            user.user_permissions.add(permission_logentry)

            group.save()
            user.save()

 - Теперь можно выполнить команду в терминале: python manage.py bind_user

                                            ***********************************************
                                                    Использование и проверка прав
Документация - https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions-and-authorization

 - Проверка прав в шаблоне, и показывать ссылку если права к созданию продукта есть:
    Почитать - https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions
    {% if 'shopapp.add_product' in perms %}
        <div>
            <a href="{% url 'shopapp:product_create' %}">
                Create a new product
            </a>

        </div>
    {% endif %}

 - Добавим примесь разрешающую доступ ке странице заказов shopapp/views.py
    from django.contrib.auth.mixins import LoginRequiredMixin
    class OrdersListView(LoginRequiredMixin, ListView): # Просто подмешиваем импортированный миесин
        queryset = (
            Order.objects
            .select_related("user")
            .prefetch_related("products")
        )
     - Далее добавим переадресацию на страницу логина (так как джанго по умолчанию переадресовывает на страницу "logins")
        Для это в файл mysite/settings.py добави одну строчку в самый конец файла:
        LOGIN_URL = reverse_lazy("myauth:login")

 - Теперь добавим ограничение через декоратор (если не используется class based views). В файле myauth/views.py изменим функцию
    from django.contrib.auth.decorators import login_required

    @login_required
    def get_session_view(request: HttpRequest) -> HttpResponse:
        value = request.session.get("foobar", "default")
        return HttpResponse(f"Session value: {value!r}")

 - Теперь ограничим права просмотра деталей заказ для пользователя "bob"
    Для этого перейдем на страницу admin джанго и там пользователю добавим права

    Добавим примесь разрешающую доступ к деталям заказа shopapp/views.py
    from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

    class OrderDetailView(PermissionRequiredMixin, DetailView):
        permission_required = "shopapp.order_view" # Тут указываем, какое имено требуется разрешение (название можно взять из таблицы в бд "auth_permissions". Может быть список разрешений (кортеж
        queryset = (
            Order.objects
            .select_related("user")
            .prefetch_related("products")
    )

 - Теперь добавим ограничение через декоратор (если не используется class based views). В файле myauth/views.py изменим функцию
    from django.contrib.auth.decorators import login_required, permission_required

    @permission_required("myauth.view_profile", raise_exception=True) # В скобках указываем, какое разрешение требуется, raise_exception=True - нужно что бы небыло переадресаций по кругу
    def set_session_view(request: HttpRequest) -> HttpResponse:
        request.session["foobar"] = "spameggs"
        return HttpResponse("Session set!")

 - Оставить доступ к админке только для суперпользолвателя (принадлежность к группе) с помощью Mixin -> shopapp/views.py
    from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

    class ProductCreateView(UserPassesTestMixin, CreateView): # Добавляем mixinn UserPassesTestMixin
        def test_func(self):
            # return self.request.user.groups.filter(name="secret-group").exist()
            return self.request.user.is_superuser # Тут проверяем, является ли пользователь с правами админа

        model = Product
        fields = "name", "price", "description", "discount"
        success_url = reverse_lazy("shopapp:products_list")

- Оставить доступ к админке только для суперпользолвателя (принадлежность к группе) с помощью декоратора -> myauth/views.py
    from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

    @user_passes_test(lambda u: u.is_superuser) # Важно, здесть нет флага raise_exception=True, поэтому логику редиректа нужно вносить в тело функции
    def set_cookie_view(request: HttpRequest) -> HttpResponse:
        response = HttpResponse("Cookie set")
        response.set_cookie("fizz", "buzz", max_age=3600)
        return response

 - Если нужно при создании товара указать текущего пользователя автоматически, можно переопределить метод form_valid:
    class ProductCreateView(PermissionRequiredMixin, CreateView):
        permission_required = "shopapp.add_product"
        model = Product
        fields = "name", "price", "description", "discount"
        success_url = reverse_lazy("shopapp:products_list")

        def form_valid(self, form):
            form.instance.created_by_id = self.request.user.id
            return super().form_valid(form)

 - Разрешить редактирование товара только автору карточки и суперпользователю:
    class ProductUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):

        permission_required = "shopapp.change_product"
        model = Product
        fields = "name", "price", "description", "discount"
        template_name_suffix = "_update_form"

        def test_func(self):
            return self.request.user.id == self.get_object().created_by_id or self.request.user.is_superuser # Тут через self.get_object() добираемся до самой карточки продукта

        def get_success_url(self):
            return reverse(
                "shopapp:product_details",
                kwargs={"pk": self.object.pk},
            )

========================================================================================================================

                                                    Тестирование
Почитать - https://docs.djangoproject.com/en/4.1/topics/testing/tools/
Классы тестирования - https://docs.djangoproject.com/en/4.1/topics/testing/tools/#provided-test-case-classes

 - Создадим файл mysite/shopapp/utils.py (простой тест для примера работы)
    def add_two_numbers(a, b):
        return a + b
 - Далее открываем mysite/shopapp/tests.py
    from django.test import TestCase
    from shopapp.utils import add_two_numbers

    class AddTwoNumbersTestCase(TestCase):
        def test_add_two_numbers(self): # Метод вызывает проверяемую функцию
            result = add_two_numbers(2, 3)
            self.assertEqual(result, 5) # Проверяем равенство результа функции и ожидаемого ответа (5 - передаем вторым аргументом)

- Теперь можно запустить тест в терминале: python manage.py test shopapp.tests.AddTwoNumbersTestCase (далее эта же команда используется для запуска тестов)

                            ********************************************************************
                                    Тесты для вьюфункций (имитация запроса пользователя)

 - Откроем mysite/myauth/tests.py
    from django.test import TestCase
    from django.urls import reverse

    class GetCookieViewTestCase(TestCase):
        def test_get_cookie_view(self):
            response = self.client.get(reverse("myauth:cookie-get"), HTTP_USER_AGENT='Mozilla/5.0') #  HTTP_USER_AGENT= нужен, так как в базовом шаблоне к меня функция отображения HTTP_USER_AGENT заложена
            self.assertContains(response, "Cookie value") # Проверяем содержание ожидаемого ответа (его можно посмотреть в самой вьюфункции)

 - Создадим вью функцию для обработки json ответа. Для этого в mysite/myauth/views.py создадим класс:
    from django.views import View
    from django.http import HttpRequest, HttpResponse, JsonResponse

    class FooBarView(View):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse({"foo": "bar", "spam": "eggs"})

 - Поключим класс к mysite/myauth/urls.py
    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),

 - Создадим тест для проверки тела ответа (json). Для этого в mysite/myauth/tests.py создадим класс:
    import json

    class FooBarViewTestCase(TestCase):
        def test_foo_bar_view(self):
            response = self.client.get(reverse("myauth:foo-bar"), HTTP_USER_AGENT='Mozilla/5.0') # HTTP_USER_AGENT= нужен, так как в базовом шаблоне к меня функция отображения HTTP_USER_AGENT заложена
            self.assertEqual(response.status_code, 200) # Тут проверяем статус ответа, должен быть 200
            self.assertEqual(
                response.headers['content-type'], 'application/json', # Тут проверяем заголовки
            )
            expected_data = {"foo": "bar", "spam": "eggs"} # Тут важно не копировать, а написать от руки (что бы случайно не скопировать ошибку)
            # received_data = json.loads(response.content) # Тут заливаем данные в json, тк сравнивать нужно json, а в ответе приходят байты (в str формате лучше не проверять, если порядок будет отличатся, тест провалится
            # self.assertEqual(received_data, expected_data) # Тут проверяем ожидания с ответом
            self.assertJSONEqual(response.content, expected_data) # Тут сразу проверяем все в json, что бы не писать вручную

 - Создадим тест для создания товара в mysite/shopapp/tests.py
    from string import ascii_letters
    from random import choices
    from django.urls import reverse

    class ProductCreateTestCase(TestCase): # Метод нужен для генерации имен создавваемого продукта при тесте
        def setUp(self) -> None:
            self.product_name = "".join(choices(ascii_letters, k=10))
            Product.objects.filter(name=self.product_name).delete() # Так удаляем все сгенерированые имена после теста

        def test_create_product(self):
            response = self.client.post(
                reverse("shopapp:product_create"),
                {
                    "name": self.product_name,
                    "price": "123.45",
                    "description": "A good table",
                    "discount": "10",
                }, HTTP_USER_AGENT='Mozilla/5.0'
            )
            self.assertRedirects(response, reverse("shopapp:products_list")) # Ту проверяется перенаправление. Но тут проблема, я юзаю миксин и тест не проходит (надо разобраться)
            self.assertTrue(
                Product.objects.filter(name=self.product_name).exist()       # Проверяем, существует ли продукт
                )

 - Реализуем тест для проверки получения страницы с продуктом в mysite/shopapp/tests.py
    class ProductDetailsViewTestCase(TestCase):
        @classmethod
        def setUpClass(cls):                                                              # Так поступаем, если есть опасность изменить тестируемую сущность (она создается только один раз)
            cls.product = Product.objects.create(name="Best Product", created_by_id="1")
        # def setUp(self) -> None:                                                          # Метод выполняется перед каждым тестом
        #     self.product = Product.objects.create(name="Best Product", created_by_id="1") # Создаем произвольный продутк
        @classmethod
        def tearDownClass(cls):                                                           # Так поступаем, если есть опасность изменить тестируемую сущность (она создается только один раз)
            cls.product.delete()
        # def tearDown(self) -> None: # Метод выполняется после каждого теста. Удаляем продукт вне зависимости от результата теста
        #     self.product.delete()

        # def test_get_product(self): # Такая проверка нужна если используем классметод для тестирования (он не работает, если допомпередавать created_by_id="1" в модель)
        #     response = self.client.get(
        #         reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
            )
            # self.assertEqual(response.status_code, 200)

    def test_get_product(self):                                                         # Тест проверяет статус код ответа
            self.client.get(
                reverse("shopapp:product_detail", kwargs={"pk": self.product.pk})
            )

    def test_get_product_and_check_content(self):                                  # Тест проверяет содержимое ответа (имя продукта)
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertContains(response, self.product.name)

 - Что бы выгрузить из базы даные для ручного тестирования, используем команду:
    python manage.py dumpdata shopapp  # Так мы получаем все данные из приложения shopapp в формате JSON (через точку можно указать конкретную таблицу приложения, например .Product)

 - Что бы сохранить данные из БД в формате JSON используем команду:
    python manage.py dumpdata shopapp > shopapp-fixtures.json (открыв файл и нажав ctrl+alt+l - можно форматировать код для удобного чтения)

 - Что бы восстановить данные из файл в базу даных, испольуем команду:
    python manage.py loaddata shopapp-fixtures.json

                                                **********************************************
                                                        Тесты для страниц сайта
Важно!!! Что бы фикстуры корректно открыфвались в тестах, получившийся файл с фикстурами и в нижнем правом углу
указать тип кодировки для нешго UTF-8. После выбрать вариант "Convert", что бы перезаписать файл в нужной кодировке

 - Создадим папку fixtures в mysite/shopapp

 - выполним команду: python manage.py dumpdata shopapp.Product > shopapp/fixtures/products-fixture.json
    (Попробовать: python -Xutf8 manage.py dumpdata shopapp.Product > shopapp/fixtures/products-fixture.json)

 - Важно!!!! Что бы выгрузить фикстуры пользователей, вводим команду: python manage.py dumpdata auth.User > shopapp/fixtures/users-fixture.json

 - Создадим новый класс для тестирования получения списка продуктов mysite/shopapp/tests.py
    class ProductsListViewTestCase(TestCase):
        fixtures = [
            'products-fixture.json',
        ]

        def test_products(self):
            response = self.client.get(reverse("shopapp:products_list"))
            self.assertQuerysetEqual(
                qs=Product.objects.filter(archived=False).all(),        # Тут указываем, какие данные ожидаем получить из базы данных (из фикстуры)
                values=(p.pk for p in response.context["products"]),    # Тут указываем, какие данные нужны из контекста вьюфункции (из списка продуктов)
                transform=lambda p: p.pk                                # Тут указываем, как преобразовать данные из qs, что бы сравнить их с values
            )
            self.assertTemplateUsed(response, 'shopapp/products-list.html') # Тут проверяем, какой шаблон был использован
        # Можно так же проверить контекст через зип функцию (минус в том, что сравнение будет проходить по коллекции, которая короче)
        # def test_products(self):
        #     response = self.client.get(reverse("shopapp:products_list"))
        #     products = Product.objects.filter(archived=False).all()
        #     products_ = response.context["products"] # Берем именно "products", потому что во вьюхе context_object_name = "products"
        #     for p, p_ in zip(products, products_):
        #         self.assertQuerysetEqual(p.pk, p_.pk)

 - А теперь блядь, наконец то, создадим тест в котором будет выполняться аутентификация и авторизация польователя (делаем там же mysite/shopapp/tests.py)
    from django.conf import settings
    class OrdersListViewTestCase(TestCase):
        @classmethod
        def setUpClass(cls):
            cls.credentials = dict(username="bob_test", password="qwerty")   # Здесь один раз создаем пользователя для всех тестов
            cls.user = User.objects.create_user(**cls.credentials)           # Здесь распакорвываем данные пользователя при создании епго
            cls.user = User.objects.create_user(**cls.credentials)           # Здесь распакорвываем данные пользователя при создании епго
            permission_order = Permission.objects.get(codename='view_order') # Так указываем, какие права хотим добавить (название можно глянуть в таблице auth_permissions)
            cls.user.user_permissions.add(permission_order)                  # Так добавляем права создаваемому пользователю
        @classmethod
        def tearDownClass(cls):
            cls.user.delete()                                              # Здесь, как обычно, удаляем пользователя после тестов
        def setUp(self) -> None:
            self.client.login(**self.credentials)                          # Здесь забираем данные пользователя для логина
            # self.client.force_login(self.user)                             # Так можно обеспечить логин без проверки данных пользователя
        def test_orders_view(self):
            response = self.client.get(reverse("shopapp:orders_list"))
            self.assertContains(response, "Orders")

        def test_orders_view_not_authenticated(self):                     # Здесь проверяем не авторизованного пользователя
            self.client.logout()
            response = self.client.get(reverse("shopapp:orders_list"))
            # self.assertRedirects(response, str(settings.LOGIN_URL))
            self.assertEqual(response.status_code, 302)
            self.assertIn(str(settings.LOGIN_URL), response.url)

 -  Создадим тест для создания заказа и проверки его содержиого а так же сверки закза из ответа с тем, который создается в тесте по первичному ключу
    class OrderDetailViewTestCase(TestCase):

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.user = User.objects.create_user(username="Test_user", password="qwerty")
            permission_order = Permission.objects.get(codename='view_order')
            cls.user.user_permissions.add(permission_order)          # Проверяем
            cls.user.save()                                        # Сохраняем пользователя, после добавления ему прав

        @classmethod
        def tearDownClass(cls):
            cls.user.delete()

        def setUp(self) -> None:
            self.client.force_login(self.user)
            self.order = Order.objects.create(
                    delivery_address="Test address",
                    promocode="sale_1",
                    user_id=self.user.pk,
            )

        def tearDown(self) -> None:
            self.order.delete()

        def test_order_details(self):
            response = self.client.get(
                reverse("shopapp:order_details", kwargs={"pk": self.order.pk}),
            )
            received_data = response.context["order"].pk              # Тут вызываем context, тк ответ приходит не json, а текст
            expected_data = self.order.pk
            self.assertContains(response, self.order.delivery_address)
            self.assertContains(response, self.order.promocode)
            self.assertEqual(received_data, expected_data)

- Создадим тест для экспорта продуктов в фикстуры и сравнения их с базой
    class OrderExportTestCase(TestCase):
        fixtures = [
            "products-fixture.json",
            "users-fixture.json",
            "orders-fixture.json",
        ]

        @classmethod
        def setUpClass(cls):
            super().setUpClass()  # После переопределения метода нужно вызвать код предка класса через супер
            cls.user = User.objects.create_user(username="Test_user", password="qwerty", is_staff=True)

        @classmethod
        def tearDownClass(cls):
            cls.user.delete()

        def setUp(self) -> None:
            self.client.force_login(self.user)

        def test_get_orders_view(self):
            response = self.client.get(
                reverse("shopapp:orders-export"),
            )
            self.assertEqual(response.status_code, 200)
            orders = Order.objects.order_by("pk").all()
            expected_data = [
                {
                    "pk": order.pk,
                    "address": order.delivery_address,
                    "promocode": order.promocode,
                    "user": order.user.id, # Объекты user и product не сериализуются, их надо преобразовать к id записей в соответствующих таблицах
                    "products": [product.id for product in order.products.all()]
                }
                for order in orders
            ]
            orders_data = response.json()
            self.assertEqual(
                orders_data["orders"],
                expected_data,
            )

 - Создадим вью функцию для ранее созданного теста
    from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse

    class OrderDataExportView(View, UserPassesTestMixin):
        def test_func(self):
            return self.request.user.is_staff
        def get(self, request: HttpRequest) -> JsonResponse:
            orders = Order.objects.order_by("pk").all()
            orders_data = [
                {
                    "pk": order.pk,
                    "address": order.delivery_address,
                    "promocode": order.promocode,
                    "user": order.user.id,
                    "products": [product.id for product in order.products.all()]
                }
                for order in orders
            ]
            return JsonResponse({"orders": orders_data}) # Здесь мы пишем "orders" в ключе словаря,
            # потому что это имя продиктовано тестом выше, где идет обращение к self.assertEqual (orders_data["orders"])

 - Подключим созданную вью функцию к mysite/shopapp/urls.py
    path("orders/export", OrderDataExportView.as_view(), name="orders-export"),

                                            ******************************************
                                                                TDD
Test Driven Development - это когда сначала пишутся тесты, а потом уже сами функции (сам код программы). Пишутся эти тесты в
три этапа:
1) Пишутся тесты, которые проваливаются (потому что если не проваливаются, значит либо тест не правильный, либо функциональность такая уже существует)
2) Пишутся тесты которые проходят
3) Запуск тестов и рефакторинг кода (просто причесываем код и проверяем, что бы тесты проходили)

 - Создадим тест, который будет проваливаться (для апи по выгрузке информации по продуктам) mysite/shopapp/tests.py
    Надо проверить модель Products, что бы там был метод сортировки   class Meta: ordering = ["name", "price"]
========================================================================================================================


                                        ****************************************************
                                                        Рбота с файлами
                                        ****************************************************

                                            Использование FileField для хранения файлов
Документация - https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/

 - Добавим ряд настроек в корневом файле mysite/urls.py:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('shop/', include('shopapp.urls')),
        path('req/', include('requestdataapp.urls')),
        path('accounts/', include('myauth.urls')),
    ]

    if settings.DEBUG:
        urlpatterns.extend(
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        )

 - Далее в файле mysite/settings.py добавим данные параметры, созданные выше (что бы файлы приложения не стали доступны через браузер)
    Добавлять пароаметры можно под значением STATIC_URL = 'static/'
        MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR / 'uploads' # Это означает, что файлы будут лежать в корневой папке приложения mysite (этот путь так же прописан в самом начале файла settings.py

 - Добавим новое поле в модель Order для  mysite/shopapp/models.py:
    receip = models.FileField(null=True, upload_to='orders/receipts') # null=True - т.к. чека может не быть у заказ, upload_to= Это путь, к которому вначале будет приставляться MEDIA_ROOT, который узалаи выше

- Далаее выполняем миграцию: python manage.py makemigrations и python manage.py migrate

- Теперь в теле заказа (если зайти в админку, доступна кнопка для выбора файла для загрузки)

- Так же можно изменить дефолтный класс для работы с файлами. Для этого в файле mysite/settings.py нужно объявить переменну:
    DEFAULT_FILE_STORAGE = # Тут можно указать новый класс, который бдкт оперировать файлами
                                        ******************************************************

                                                        Группы файлов в django
 - Статика: Файлы java scripts  и CSS (Файлы необходимые для работы сайта. Скрипты, стили, иконки и т.д.)

    Для правильной работы, на локльной машине в проект нужно добавить свои статики:
    Что бы добавить пути к таким файлам в проект, нужно добавить в mysite/urls.py:
            if settings.DEBUG:
                urlpatterns.extend(
                    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                )
    По умолчанию для статики используется папка STATIC_URL = 'static'. Важно!! Эти файлы не будут меняться во время работы приложения
    ТЕ удалить или добавить файлы можно только при работе с исходынм кодом. Поэтому для их обновления придется выпускать новый релиз

    Сборка статики, это копирование всех файлов в однку папку, которую сможет обслуживать отдельный вебсервер. Она выполняется каждый раз, при релизе приложения

 - Медиа: Файлы для динамического контента на странице (картикуи, видео, гифки и прочее) - эти файлы могут меняться во
    время работы приложения
       Пути до этих файлов так же конфигурируются с помощью MEDIA_URL и MEDIA_ROOT или же можно использовать сторонние библиотеки (white noise)
                                            ********************************************************

                                                Использование ImageField для работы с картинками

 - Для начала нужно установить библиотеку: в терминале pip install pillow и потом сохранить  зависимость pip freeze > requirements.txt

 - Добавим новое поле на модель Product в mysite/shopapp/models.py:
    def product_preview_directory(instance: "Product", filename: str) -> str:
        return "products/product_{pk}/preview/{filename}".format(
            pk=instance.pk,
            filename=filename,
        )
    class Product(models.Model):
        class Meta:
            ordering = ["name", "price"]

        name = models.CharField(max_length=100)
        description = models.TextField(null=False, blank=True)
        price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
        discount = models.SmallIntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        created_by = models.ForeignKey(User, on_delete=models.PROTECT)
        archived = models.BooleanField(default=False)
        preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory)

        def __str__(self) -> str:
            return f"Product(pk={self.pk}, name={self.name!r})"

 - Далаее выполняем миграцию: python manage.py makemigrations и python manage.py migrate

 - Теперь отредактируем шаблоны деталей продукта и списка продуктов для отображения картинок в mysite/shopapp/templates/shopapp:
    {% extends 'shopapp/base.html' %}

    {% block title %}
        Product #{{product.pk}}
    {% endblock %}

    {% block body %}
    <h1>Product <strong>{{ product.name }}</strong></h1>
    <div>
        <div>Description: <em>{{ product.description }}</em></div>
        <div>Price: {{ product.price }}</div>
        <div>Discount: {{ product.discount }}</div>
        <div>Archived: {{ product.archived }}</div>
        {% if product.preview %}                                                      # Такой же блок if целиком нужно будет добавить в шаблон products-list.html, в цикл, под значением <p>Discount: {% firstof product.discount 'no discount'%}</p>
            <img src="{{ product.preview.url }}" alt="{{ product.preview.name }}">
        {% endif %}
    </div>
    <p>Created by: {% firstof object.created_by.first_name object.created_by.username %}</p>
    <div>
        <a href="{% url 'shopapp:product_update' pk=product.pk %}">Update product</a>
    </div>
    <div>
        <a href="{% url 'shopapp:product_delete' pk=product.pk %}">Archive product</a>
    </div>
    <div>
        <a href="{% url 'shopapp:products_list' %}"
        >Back to products list</a>
    </div>
    {% endblock %}

 - Теперь обновим классы ProductCreateView и ProductUpdateView, что бы в них можно было добавить картинки (mysite/shopapp/views.py)
    ТК оба класса используют одну и ту же форму, достатчно просто добавить в fields = "name", "price", "description", "discount", "preview"

 - Далее нужно изменить шаблоны product_form и product_update_form в mysite/shopapp/templates/shopapp:
    {% extends 'shopapp/base.html' %}

    {% block title %}
        Create product
    {% endblock %}

    {% block body %}
        <h1>Create product:</h1>
        <div>
            <form method="post" enctype="multipart/form-data"> # Такое же значение нужно добавить в product_update_form.html
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Create</button>
            </form>
        </div>
        <div>
            <a href="{% url 'shopapp:products_list' %}"
            >Back to products list</a>
        </div>
    {% endblock %}

                                        ************************************************
                                Загрузка нескольких файлов и работа с административной панелью

Upload file - https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/
Upload multiple files - https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/#uploading-multiple-files
The django admin site - https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#inlinemodeladmin-objects

 - Что бы добавить несколько фото, это связь многие к одному, для этого создадим новую модель ProductImage в mysite/shopapp/models.py:
    def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
        return "products/product_{pk}/images/{filename}".format(
            pk=instance.product.pk,                                       # Здесь нам нужен id именно продукта, для которого собираются картинки
            filename=filename,
        )

    class ProductImage(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
        image = models.ImageField(upload_to=product_images_directory_path)
        description = models.CharField(max_length=200, null=False, blank=True)

 - Далаее выполняем миграцию: python manage.py makemigrations и python manage.py migrate

 - Теперь добавим эту модель в админку!! Нет смысла отдельно отображать картинки как функцию (mysite/shopapp/admin.py)
    и отредактируем запись ProductAdmin. Но для этого сначала создадим новый класс ProductInLine, тк созданный ранее класс
    имеет связь один ко многим, и просто в строчку его добавить нельзя
    from .models import Product, Order, ProductImage
    class ProductInLine(admin.StackedInline):
        model = ProductImage

    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        actions = [
            mark_archived, mark_unarchived,
        ]
        inlines = [
            OrderInLine,
            ProductInLine,
        ]
        list_display = "pk", "name", "description_short", "price", "discount", "archived"
        list_display_links = "pk", "name"
        ordering = "pk",
        search_fields = ["name", "description", "price", "discount"]

        fieldsets = [
            (None, {
                "fields": ("name", "description"),
            }),
            ("Price options", {
                "fields": ("price", "discount"),
                "classes": ("wide", "collapse")
            }),
            ("Extra options", {
                "fields": ("archived",),
                "classes": ("collapse",),
                "description": "Extra option. Field 'archived' is for soft delete",
            }),
            ("Images", {
                "fields": ("preview",),
            }),
        ]

        def description_short(self, obj: Product) -> str:
            if len(obj.description) < 48:
                return obj.description
            return obj.description[:48] + "..."

 -  И теперь создадим саму модель в mysite/shopapp/models.py
    def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
        return "products/product_{pk}/images/{filename}".format(
            pk=instance.product.pk,
            filename=filename,
        )

    class ProductImage(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
        image = models.ImageField(upload_to=product_images_directory_path)
        description = models.CharField(max_length=200, null=False, blank=True)

 - Далее изменим вью функцию для отрисовки деталей продукта в  mysite/shopapp/views.py:
    class ProductDetailsView(DetailView):
        template_name = "shopapp/products-details.html"
        # model = Product
        queryset = Product.objects.prefetch_related("images") # prefetch_related используется, тк связь один ко многим
        context_object_name = "product"

 - Теперь изменим шаблон для отрисовки изменений  mysite/shopapp/templates/shopapp/products_details.html:
    {% extends 'shopapp/base.html' %}

    {% block title %}
        Product #{{product.pk}}
    {% endblock %}

    {% block body %}
    <h1>Product <strong>{{ product.name }}</strong></h1>
    <div>
        <div>Description: <em>{{ product.description }}</em></div>
        <div>Price: {{ product.price }}</div>
        <div>Discount: {{ product.discount }}</div>
        <div>Archived: {{ product.archived }}</div>
        {% if product.preview %}
            <img src="{{ product.preview.url }}" alt="{{ product.preview.name }}">
        {% endif %}
        <h3>Images</h3>
        <div>
            {% for img in product.images.all %}          # Опять же, тк связь один ко многим нужны все картинки продукта
                <div>
                    <img src="{{img.image.url}}" alt="{{img.image.name}}">
                    <div>{{ img.description }}</div>               # Здесь просто берем текстовое поле из модели, потому запись без кавычек
                </div>
            {% empty %}
                <div>No images uploaded yet</div>
            {% endfor %}
        </div>
    </div>
    <p>Created by: {% firstof object.created_by.first_name object.created_by.username %}</p>
    <div>
        <a href="{% url 'shopapp:product_update' pk=product.pk %}">Update product</a>
    </div>
    <div>
        <a href="{% url 'shopapp:product_delete' pk=product.pk %}">Archive product</a>
    </div>
    <div>
        <a href="{% url 'shopapp:products_list' %}"
        >Back to products list</a>
    </div>
    {% endblock %}

 - Методы выше, позволяют добавлять картинки по одной. Для загрузки сразу нескольких, нужно создать свою форму в mysite/shopapp/
    Создаем файл forms.py (если он еще не создан)
    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = "name", "price", "description", "discount", "preview",

        images = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={"multiple": True}), # Это поле позволяет загружать разом несколько
        )

 - Теперь доработаем вью файл mysite/shopapp/views.py:
    from .forms import ProductForm
    from .models import Product, Order, ProductImage

    Далее укажем эту форму в классах ProductCreateView и ProductUpdateView

    class ProductUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView): # Важно!!! Миксины пишем пред  UpdateView иначе они не работают!!!!

        permission_required = "shopapp.change_product"
        model = Product
        # fields = "name", "price", "description", "discount", "preview" # Это поле убираем, в вместо него будем использовать созданную форму ProductForm
        form_class = ProductForm
        template_name_suffix = "_update_form"

        def test_func(self):
            return self.request.user.id == self.get_object().created_by_id or self.request.user.is_superuser

        def get_success_url(self):
            return reverse(
                "shopapp:product_details",
                kwargs={"pk": self.object.pk},
            )

        def form_valid(self, form):                       # Переопределяем метод валидации формы
            response = super().form_valid(form)
            for image in form.files.getlist("images"):    # getlist("images") получает сразу список картинок
                ProductImage.objects.create(              # В цикле, с помощью  ProductImage создаем новые объекты (картинки)
                    product=self.object,
                    image=image,
                )
            return response
