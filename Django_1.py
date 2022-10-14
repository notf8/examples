Фрэймворк - это набор готовых библиотек и готовых модулей, типа панель администратора, набор регистрации пользователей и т.д.
Django - это готовый фреймворк, с огромным набором библиотек

 - HTTP запрос бывает 2-х видов: Get и Post. В себе они содержат голову (Head) и тело (Body)
 - Для получения инфы с сервера используется Get запрос
 - Для обновления инфы на сервере используется Post запрос
 - Host - Указывет, к какому веб приложению нужно обратится на сервере
 - User-agent - говорит с какого браузера и устройства обращается клиент
 - Accept - говорит о том, какой язык может понять клиент
========================================================================================================================

Простейшее серверное приложение:
## (Запустить сервер из командной строки, находясь в директории с файлом: python simple_http_server.py)
from http.server import HTTPServer, BaseHTTPRequestHandler

APP_HOST = 'Localhost'  # Указываем на каком хосту будет запускаться наш веб-сервер (в это случае, это хост нашей машины = 127.001)
APP_PORT = 8000  # Указываем на каком порту сервер будет работать

class SimpleGetHandler(BaseHTTPRequestHandler):  # Класс - элементарный обработчик get запросов
    def _set_handlers(self):
        self.send_response(200)  # Указываем, какие заголовки должны быть в нашем запросе
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

    def _html(self, message):
        content = (f"<html>"
                   f"<body>"
                   f"<h1>{message}</h1>"  # Здесь передаем наш месадж в html код
                   f"</body>"
                   f"/html")
        return content.encode("utf8")  # Кодируем контент в utf8

    def do_GET(self):
        self._set_handlers()
        message = "Привет, мир!"  # Создаем нужный нам месадж
        self.wfile.write(self._html(message))  # Отправляем наш ответ(ответ сервера) клиенту

def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):  # Инициализируем запуск сервера
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()  # Указываем, что сервер необходимо хранить вечно (пока не упадет в ошибку или мы его не выключим)

if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)
========================================================================================================================

Компоненты веб приложений и первый запуск DJANGO: Модель MTV
СУБД (база данных) => Модель => Пердставление => Шаблон
 - Модель - специальный слой, необходимый для общения с источником данных
 - Пердставление - Специальная питоновская функция или класс, вызывается при обращении по спец.url и возвращает http ответ
    Оно преобразует наши http запросы
 - Шаблон - Это форма представления данных. С помошью нее, можно преобразовывать данные из представления в HTML код и
    возвращать их клиенту
========================================================================================================================

Пишем приложение на DJANGO (все команды можно писать в терминале питона или через CMD перейдя в дирректорию, где будем создавать приложение)
 - Установка Django: pip install Django==2.2
 - Установка "ToDo": django-admin startproject todo  # Команда создает каркас и все нужные файлы для работы приложения
 - Создаем новое приложение: django-admin startapp tasks
 - Выполняем миграцию наших данных в базу данных: python manage.py migrate
 - Создаем пользователя для приложения: python manage.py createsuperuser. Django попросит ввести имя пользователя (сделал admin)
    потом попросит ввести email - можно оставить пустым
    после попросит пароль (1234), потом попросит ввести более сложный (можно просто пропустить этот ход)
 - Запускаем сервер: python manage.py runserver
    Запустится приложение на локальном сервере и порту 8000. Можно пройти и проверить (http://localhost:8000)
    Важно! Созданый сайт уже с админкой! ЧТо бы ее открыть нужно добавить http://localhost:8000/admin (логин и пароль указывали ранее)
 - Останоить сервер: CTRL+C
 - Все обработчики запросов находятся в файле views.py Если мы захолтим поменять наше отображение, код меняем именно там
========================================================================================================================

Виртуальное окружение: Нужно для того, что бы можно было установить разные версии фреймворков в один интерпритато питона
Для примекра, как это работает:
 - Создаем папку - mkdir project
 - Переходим в эту папку - cd project
 - Создаем в ней виртуальное окружение - python3 -m venv my_venv  # В конце (my_venv) указываем как будет называться наше окружение
 - Активируем окружение - project\my_venv\Scripts\activate.bat
 - После работы деактивируем окружение - project\my_venv\Scripts\deactivate.bat
========================================================================================================================

Создаем приложение advertisement
Важно! При выкатке на продакшн, все пакеты должны быть подписаны одной версией и лежать в файле requirements.txt
 - Просто создаем файл requirements.txt в папке проекта (команда из видио "touch" не работает в винде)
 - Далее в файл записываем все пакеты, которые нам понадобятся (нарпимер Django==2.2, версия пишется через ==)
 - Установим все необходимое из файла - pip install -r requirements.txt (перед установкой перейти в папку проекта (cd project))
 - После можно стартовать проект - django-admin startproject board (в конце "board" - это название проекта)
 - Смотрим структуру папок проекта - tree board (в терминале)
 - Переходим в папку с проектом (cd board) и выполняем команду python manage.py help
 - Если ввести название команды после 'help', можно получить справку по команде - python manage.py help startapp

Важно! Веб-приложение и Django - не одно и тоже. В django содержутся пакеты, обеспечивающие клиент-серверное взаимодействие
в веб-приложении же хранятся формы, файл, шаблоны и т.д. для работы самого веб-приложения

 - Создаем приложение, в котором будет лежать код для доски объявлений - python  manage.py startapp advertisement
 - Теперь создаем миграцию базы данных (в gjango пердустановлена SQLlite) - python manage.py migrate

Теперь конфигурируем проект:
 - Для этого в файл 'urls.py', который лежит в папке board добавим импорт из проекта advertisement:
    - В строке импорта (from django.urls) дописываем через запятую include
    - А в переменную urlpatterns (в список) добавим через запятую: path('', include('advertisement.urls'))
    - После, в папке advertisement создаем файл urls.ry
    - from django.urls import path
    - from .import views          ## Тут импортируем вьхи
     - urlpatterns = [
        path("", views.advertisement_list, name='advertisement_list')  #Здесь связываем представления advertisement
      ]                                                                #с корневым каталогом двойными кавычками
    #Этот запрос соответсвует пустой строке (обращению к 127.001) и будет обработан этим представлением. Именной аргумент
    # "name" это идентификатор url и должен быть уникальным (и легко запоминающимся)

Теперь открываем файл views в папке advertisement:
 - Добавим в файл свою функцию:
    from django.http import HttpResponse
    def advertisement_list(request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Мастер на час</li>'
                            '<li>Выведение из запоя</li>'
                            '<li>Мастер на час</li>'
                            '<li>Услуги жкскаватора-погрузчика</li>'
                            '</ul>')
