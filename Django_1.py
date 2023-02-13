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
        search_fields = "name", "description" # Добавляем именно description, тк имено по нему будет поиск
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
    Там же в админ моедлях (admin.py) объявляем новый класс
        class OrderInLine(admin.TabularInline):
            model = Product.orders.through
    Потом в класс ProductAdmin добавляем запись inlines (пог аналогии с OrderAdmin):
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
