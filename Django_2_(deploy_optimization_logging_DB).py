
                                        *********************************************************
                                             Эффективное взаимодействие с базой данных

Проектирование базы данных. Лучшие практики - https://habr.com/ru/company/otus/blog/471016/
Три аспекта оптимизации (БД и ПО) - https://habr.com/ru/post/349910/
QuerySet API reference, Django documentation - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#select-related

                                        **********************************************
                                                    Принципы оптимизации
1) Индексы: Нужны для поиска, сортировки и фильтрации, хранятся отдепльно от самой таблицы (db_index = True)

 - Добавим индексы на товары: mysite/shopapp/models.py
    class Product(models.Model):
        class Meta:
            ordering = ["name", "price"]
            verbose_name = _('Product')
            verbose_name_plural = _('Products')

        name = models.CharField(max_length=100, verbose_name=_("Name"), db_index=True)
        description = models.TextField(null=False, blank=True, verbose_name=_("Description"), db_index=True)

 - Подготовим миграцию в терминале: python manage.py makemigrations и потом python manage.py migrate

2) Нормализация БД: Избегание дублирования кода. Нужно отделять разные сущности в разны таблицы, использовать связи и первичные ключи
А так же можно использовать хранимые процедуры (сохранять куски частого кода на сервере - используют реже других)

                                        ************************************************
                                                 Логирование SQL запросов

 - Обновим настрой для логирования запросов в конце файла mysite/mysite/settings.py
    Важно!!! Данный логгинг должен быть задействован только в debug режиме!!! (потому там стоят фильтры 'filters': ['require_debug_true'],)
    LOGGING = {
        'version': 1,
        'filters': {
            'require_debug_true': {                        # Тут указываем, что нужно запрашивать данные только в debug режиме (так же указан в этом файле DEBUG = True)
                '()': 'django.utils.log.RequireDebugTrue'  # Фильтр как раз позволяет выводить логи, только если активен debug режим
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',           # Этот класс будет выводить все потоком в терминал
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
        },
    }

 - Теперь перейдем на страницу с продуктами а в терминале появится запрос в бд. Его скопируем и вставим в файл quieries.sql, который создадим в корне проекта
    Это нужно для удобства чтения, но в pycharm comunity не работает форматирование файла ctrl+shift+l - так что ХЗ как быть

 - Важно!!!
    prefetch_related - загружает связь один ко многим
    select-related - загружает связь одни к одному
    И первый и второй способ оптимизации используется для уменьшения кол-ва запросов к БД, на примере вьюхи ниже
        class OrdersListView(LoginRequiredMixin, ListView):
            queryset = (
                Order.objects
                .select_related("user")           # Здесь мы заранее подгружаем пользователя, что бы джанго не обращался каждый раз к БД при загрузке нового заказа
                .prefetch_related("products")     # Здесь мы сразу подгружаем все товары из базы, что бы не запрашивать их для каждого заказа
            )                                     # Иными словами, без оптимизаций джанго будет обращаться дважды к БД для каждого заказа
                                                  # что бы подгрузить пользователя и товары, а если заказов 100, то сервак ляжет

                                            *************************************************
                                                                Проблема N+1

Проблема выбора N + 1 в объектно-реляционном сопоставлении (ORM) - https://intellect.icu/problema-vybora-n-1-o-v-obektno-relyatsionnogo-sopostavleniya-orm-8653
QuerySet API reference, Django documentation - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#select-related

N+1 - Суть проблемы: записи могут ссылаться на другие сущности в других таблицах. Те когда мы запросили одну запись, а к
этой записи нужно сделать еще запрос, потому как в ней есть ссылки на другие записи, где 1 - это первый запрос, а N - это
количество загруженных элементов (например к 1 заказу нужно подгрузить N полльзователей)

 - lazy Loading - Ленивая подгрузка. Например нужно подгрузить только промокоды из заказов (а инфа по товарам и пользователям не нужна)
    Именно такой способ использует django. То есть она работает по умоляанию. Это в свою очерель может увеличивать кол-во
    запросов. Потому и используем select_related и prefetch_related. Отложенную подгрузку используем только там, где точно
    знаем, что доп запросы нам не потребуются

                                        *****************************************************
                                                        Транзакции в базах данных

Что такое транзакция («Хабр») - https://habr.com/ru/post/537594/
Что такое транзакция базы данных? AppMaster - https://appmaster.io/ru/blog/chto-takoe-tranzaktsiia-bazy-dannykh
Database transactions, Django documentation - https://docs.djangoproject.com/en/4.1/topics/db/transactions/

 - Изменим команду создания заказа для проверки транзакции в mysite/shopapp/management/commands/create_order.py
    from typing import Sequence
    from django.db import transaction
    from django.contrib.auth.models import User
    from django.core.management import BaseCommand
    from shopapp.models import Order, Product

    class Command(BaseCommand):
        @transaction.atomic                                      # atomic - защищает от создания (откатывает) объект, при возникновении ошибки
        def handle(self, *args, **options):                      # Так же atomic можно юзать не как декоратор, а как контекстный менеджер: with transaction.atomic(): ....
            self.stdout.write("Create order with products")
            user = User.objects.get(username="admin")
            products: Sequence[Product] = Product.objects.all()
            order, created = Order.objects.get_or_create(        # Здесь если не добавить created в переменную, получим ошибку, тк в переменные попадает кортеж с заказом (если он есть) и статусом (есть/нет)
                delivery_address="ul Ivanova, d 17/1",
                promocode="promo1",
                user=user,
            )
            for product in products:
                order.products.add(product)
            order.save()
            self.stdout.write(f"Created order{order}")

 - Далее в терминале выполним команду python manage.py create_order

                                        ******************************************************************
                                                Приемы оптимизации скорости и количества запросов

QuerySet API reference, Django documentation, values - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#values
QuerySet API reference, Django documentation, bulk-create - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create

 - Если столкнемся с долгой загрузкой из БД и рядом в коде будут циклы, то лучше сделать разовый запрос только к тем полям,
   которые нам нужны, сохранить их в переменные и дальше использовать переменные в циклах, что бы не делать запросы к базе

 - Что бы уменьшить колво запросов, можно присоединять даные из бд в одном запросе с помощью JOIN

 - Если нужно фильтровать много объектов, то можно заранее собрать инфу по их id и с помощью оператора IN передавать их в filter()

 - Частичная загрузка полей. Для этого создадим новую команду в mysite/shopapp/management/commands/selecting_fields.py (файл нужно создать)
    from django.contrib.auth.models import User
    from django.core.management import BaseCommand
    from shopapp.models import Product

    class Command(BaseCommand):
        def handle(self, *args, **options):
            self.stdout.write("Start demo select fields")

            users_info = User.objects.values_list("username", flat=True) # Так выгружаем только username, flat=True - означает что все имена нужно сложить в один список, а не выводить по отдельности
            for user_info in users_info:                                 # Тут Важно! К обхектам обращаемся через values_list, а не как ниже, с моделью Product, через просто values
                print(user_info)

            # products_values = Product.objects.values("pk", "name")     # Так выгружаем только id  и на звания продуктов
            # for p_values in products_values:
            #     print(p_values)
            self.stdout.write("Done")

    # Метод defer позволяет отложить загрузку полей до тех пор, пока они не понадобятся
    products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all()  # В скобках указываем поля, которые не нужны
    products: Sequence[Product] = Product.objects.only("name", "price").all() # only - наоборот (в отличии от defer), в скобках пишем только те поля, которые нужно загрузить

 - Методы массовых вставок (создадим новый файл в  mysite/shopapp/management/commands/bulk_actions.py)

    bulk_create - позволяет создать несколько объектов за один раз (за один запрос)
        from django.contrib.auth.models import User
        from django.core.management import BaseCommand
        from shopapp.models import Product

        class Command(BaseCommand):
            def handle(self, *args, **options):
                self.stdout.write("Start demo bulk_actions")
                info = [
                    ("smartphone1", 1999),
                    ("smartphone2", 2999),
                    ("smartphone3", 3999),
                    ("smartphone4", 4999),
                ]
                products = [
                    Product(name=name, price=price, created_by_id=1) # Тут надо добавить вне цикла created_by_id, тк это обязательное поле
                    for name, price in info                          # Поля ,которые мы не указали, заполнятся значениями по умолчанию
                ]
                result = Product.objects.bulk_create(products)
                for obj in result:
                    print(obj)
                self.stdout.write("Done")

    bulk_update - позволяет обновить несколько объектов за один раз (за один запрос)
        class Command(BaseCommand):
            def handle(self, *args, **options):
                self.stdout.write("Start demo bulk_actions")
                result = Product.objects.filter(
                    name__contains="smartphone",            # Тут говорим фильтру, искать продукты, в названиях которых содержится "smartphone"
                ).update(discount=10)                       # Тут через queryset обновляем объекты
                print(result)

                                        *************************************************
                                                        Агрегации и аннотации

Aggregation, Django documentation - https://docs.djangoproject.com/en/4.1/topics/db/aggregation/
Annotation, Django documentation - https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#joins-and-aggregates
Django Annotations: steroids to your Querysets by Gautam Rajeev Singh, Medium - https://medium.com/@singhgautam7/django-annotations-steroids-to-your-querysets-766231f0823a

 - Агрегации позволяют выполнять действия над несколькими строчками (например среднюю стоимость посмотреть). создадим команду mysite/shopapp/management/commands/agg.py
    from django.contrib.auth.models import User
    from django.core.management import BaseCommand
    from django.db.models import Avg, Max, Min, Count, Sum
    from shopapp.models import Product

    class Command(BaseCommand):
        def handle(self, *args, **options):
            self.stdout.write("Start demo aggregate")
            # result = Product.objects.filter(
            #     name__contains="smartphone",
            # ).aggregate(
            #     average_price=Avg("price"), # Тут сразу указываем, с каким именем вывести инфу (что бы не выводило название из модели)
            #     max_price=Max("price"),
            #     min_price=Min("price"),
            #     count=Count("id"),
            # )
            # print(result)

            orders = Order.objects.annotate(
                total=Sum("products__price", default=0),   # Тут 2 подчеркивания!! default=0 - ставим, если не хотим видеть значение None, когда в заказе пусто
                products_count=Count("products"),        # Так добавляем имя для анностации и одновременно считаем сумму по products__price
            )
            for order in orders:
                print(
                    f"Order {order.id} "
                    f"with {order.products_count} "
                    f"products worth {order.total}"
                )
            self.stdout.write("Done")
    Потом просто введем команду в терминале: python manage.py agg
    Аннотации часто используют, если нужно подготовить данные для какой-либо записи, что бы не подгружать всю базу для этого

                                        *************************************************
                                                Логированиен и профилирование

Logging | Django documentation - https://docs.djangoproject.com/en/4.2/topics/logging/
Logging HOWTO — Python 3.11.3 documentation - https://docs.python.org/3/howto/logging.html

 - Logging, уровни:
  - Debug - низкоуровневое логирование,инфа о каждом шаге приложения
  - Info - на продакшене так же отключен (до инфо, не обязательнгое для отладки)
  - Warmibg - Просто уведомление об обработаных ошибках
  - Error - Инфа о серьезной проблеме
  - Criticsl - сообщения о критической ошибке

  Важно! Уровни, которые ниже, чем выставленный в логгере, вообще не будут выводиться (те если стоит Critical, то info выведен не будет)

 - Запись логов в файл и настройка ротации лог-файлов в пmysite/mysite/settings.py
    LOGFILE_NAME = BASE_DIR / "log.txt"             # Указываем имя файла
    LOGFILE_SIZE = 1 * 1024 * 1024                  # Размер файла для ротации в байтах (1 * 1024 * 1024 = мегабайт)
    LOGFILE_COUNT = 3                               # Сколько файлов будем хранить (3 - количество предыдущих + 1 текущий)

 - Настроем logging в приложении mysite/mysite/settings.py
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s", # Тут пишем asctime что бы выводить время, а [] - для красоты вывода используем, в () - указываем переменные для вывода
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
            "logfile": {
                # "class": "logging.handlers.TimedFileHandler", (Для ротации файла по дням)
                "class": "logging.handlers.RotatingFileHandler",       # Указываем класс для обработки логов (ротация по размеру файла)
                "filename": LOGFILE_NAME,                        # Дальше просто берем переменные, которые создали ранее
                "maxBytes": LOGFILE_SIZE,
                "backupCount": LOGFILE_COUNT,
                "formatter": "verbose",                     # Форматирование оставляем то же самое, что и было в начале
            },
        },
        "root": {
                "handlers": [
                    "console",
                    "logfile",                              # Тут проост в список добавляем хэндлер, который создали выше
                ],
                "level": "INFO",
            },
        }

 - Добавим логгирование в приложение mysite/shopapp/views.py
    import logging
    log = logging.getLogger(__name__) # В скобках указываем имя текущего модуля, это стандартный формат логирования

    class ShopIndexView(View):
        def get(self, request: HttpRequest) -> HttpResponse:
            links = [
                {"title": "Список продуктов", "address": "products/"},
                {"title": "Список заказов", "address": "orders/"},
            ]
            context = {
                "time_running": default_timer(),
                "links": links,
                "items": 5,
            }
            log.debug("Products for shop index: %s", links) # В логгинг передаем правила форматирования, делаем так, если все же придлется выводить уровень debug
            log.info("Rendering shop index") # Логгировать нужно до того, как функция вернет данные, если случиться ошибка до return, мы этого нек увидим в логах
            return render(request, 'shopapp/shop-index.html', context=context)

                                **************************************************
                                            Зачем нужно профилирование?
Optimize your code using profilers | PyCharm Documentation - https://www.jetbrains.com/help/pycharm/profiler.html
Django Debug Toolbar - https://django-debug-toolbar.readthedocs.io/en/latest/

Профилирование - это процесс анализа производительности кода (выявления узких мест)

 - Установим Django Debug Toolbar, в терминале ввести: pip install django-debug-toolbar и заморозм: pip freeze > requirements.txt

 - Добавим приложение в установленные в mysite/mysite/settings.py:
    INSTALLED_APPS = ['debug_toolbar',]

 - Так же добавим его в список middleware в mysite/mysite/settings.py:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',]

 - Добавим настройку в целях безопасности в mysite/mysite/settings.py:
    INTERNAL_IPS = [
        "127.0.0.1",                                # Тут указываем, по какому IP можно получить доступ к DebugToolbar
    ]

 - Добавим приложение в mysite/mysite/urls.py:
    if settings.DEBUG:
        urlpatterns.extend(
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        )
        urlpatterns.append(
            path("__debug__/", include("debug_toolbar.urls")),
        )

 - Запуск оболочки дебага SQL без запуска с сервера (сервер должен быть остановлен):
    В терминале вводим: python manage.py debugsqlshell

                                **************************************************
                                                    Docker
Docker - https://www.docker.com/
Docker Hub - https://hub.docker.com/

Docker - платформа для создания, развертывания и управления приложениями в изолированных контейнерах
Docker compose - описывает связи между приложениями и позволяет запускать их в правильном порядке

 - Что бы работать в винде: В CMD от админа: wsl --install. Для обновления: wsl --update
   Что бы потом удалить:
   1) Параметры(шестеренка) -> Приложения -> Приложения и возможности -> "windows for linux хххх" = УДАЛЯЕМ ВСЕ
   2) Панель управления -> Програмы и компоненты -> Включение или отключение компонентов windows -> ищем "подсистема windows для linux" = Снимаем галочку

 - В корне проекта misite созаем просто файл "Dockerfile" (без расширения) и файл ".dockerignore" (там перечисляем то, чего не должно быть в контейнере)

    Пример файла ".dockerignore" (можно юзать по умолчанию):
        __pycache__
        *.pyc
        *.pyo
        *.pyd
        .Python
        env
        venv
        pip-log.txt
        pip-delete-this-directory.txt
        .tox
        .coverage
        .coverage.*
        .cache
        nosetests.xml
        coverage.xml
        *.cover
        *.log
        .git
        .mypy_cache
        .pytest_cache
        .hypothesis

    Пример файла "Dockerfile" (если что то меняем в файле то нужно выполнять сборку заново!):
        FROM python:3.11

        WORKDIR /app           # В этой папке будет работать приложение

        ENV PYTHONUNBUFFERED=1                  # Настраиваем окружене для работы логово в докере

        COPY requirements.txt requirements.txt  # Первое - пишем что копировать, второе - как сохранить

        RUN pip install --upgrade pip
        RUN pip install -r requirements.txt

        COPY mysite .                           # "." означает текущая директория

 - Далее собираем контейнер. Для этого нужно перейти в терминале в корневую папку где лежит корневая папка mysite (не вторая mysite), Важно!! Докер в этот момент должен быть запущен на компе
    Вводим команду: docker build . -t app   # "." означает, что собираем в текущей дирректории. "-t app" - тэг имени сборки

 - Для запуска собранного контейнера в терминале вводим: docker run -it app bash  # -it значит интерактивный режим.
    - ls - после запуска, этой командой можно посмотреть, какие файл есть в дирректории контейнера (это линуксовый аналог dir)
    - После можно запустить сервер привычной командой: python manage.py runserver (останавливается сервер как обычно ctrl + C)
    - покинуть сессию можно командой exit
    - Что бы выполнить запрос к серверу вспом команда: curl http://127.0.0.1:8000/

                                        ***************************************************
                                            Docker compose (нужен для проброски потртов)

 - Создадим файл docker-compose.yaml в корневой папке проекта где лежит корневая папка mysite (не вторая mysite)
    version: "3.9"

    services:                                               #Отступы принципиальны!
        app:
            build:
                dockerfile:./ Dockerfile
            command:
                - "python"
                - "manage.py"
                - "runserver"
                - "0.0.0.0:8080"                            # Указываем по какому порту доступно приложение
            ports:                            # Так можно пробросить порты, что бы они были доступны из докера на компе
                - "8000:8080"   # 8000 - порт хостовой машины, 8080 порт, на котором запускается приложение (тот же, что указан в command

 - Добавим хост в настройках приложения в mysite/mysite/settings.py:
    ALLOWED_HOSTS = [
        "0.0.0.0",
        "127.0.0.1",
    ] # Так сделаем доступным порты из докера на рабочем компе
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

    if DEBUG:              # Важно!!! докер не запустится, если параметр LANGUAGES = [] не закомментировать (какая то прооблема с gettext
        import socket
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname()) # Так делаем что бы получить адрес для работы DEBUGTOOLBAR
        INTERNAL_IPS.append("10.0.2.2")
        INTERNAL_IPS.extend(
            [ip[: ip.rfind(".")] + ".1" for ip in ips]
        )

 - Соберем контейнер с compose, в терминале ввести: docker compose build app

 - Для запуска приложения в compose вводим в терминале: docker compose up -d app # -d означает запус в отрыве от терминала (для запуска в терминале (docker compose up app)
   Что бы получить логи в режме -d, нужно ввести команду: docker compose logs -f app # -f означает получать логи в реалдьном времени

                                        ********************************************
                                                    Логи в Grafana Loki

Grafana | Query, visualize, alerting observability platform - https://grafana.com/grafana/
Grafana Loki OSS | Log aggregation system - https://grafana.com/oss/loki/
https://github.com/grafana/loki/tree/main/production

Grafana - просто визуализирует логи. А Loki их собирает

 - Запустим локально Grafana Loki. В файле /mysite/Dockerfile:
    version: "3.9"

    services:
      app:
        build:
          dockerfile: ./Dockerfile
        command:
          - "python"
          - "manage.py"
          - "runserver"
          - "0.0.0.0:8080"
        ports:
          - "8000:8080"
      grafana:
        image: grafana/grafana:9.2.15
        environment:
          - GF_AUTH_ANONYMOUS_ENABLED=true          # Разрешаем запуск без паоля
          - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin        # Даем себе права админа
        ports:
          - "3000:3000"
      loki:
        image: grafana/loki:2.8.0
        ports:
          - "3100:3100"

 - Загрузим сервисы. В терминале вводим: docker compose pull

 - Запускаем сервисы в детач режиме, в терминале: docker compose up -d grafana loki

- По адресу http://localhost:3000/?orgId=1 можно перейти на дашборд grafana.com

- В нижнем левом углу шестеренака (настройки), открываем и кликаем add data sources, там выбираем loki. Далее в настроках
    url вносим адрес: http://loki:3100 # Потом прокручиваем вниз и жем save and test

 - Установим плагин для сбора логов для Loki. В терминале введем: docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions # После установки обязательно перезапустить docker

 - После перезапуска docker, в терминал вводим: docker plugin ls # Проверяем, установился ли плагин

 - Добавим сервис в файл /mysite/Dockerfile:
    version: "3.9"

    services:
      app:
        build:
          dockerfile: ./Dockerfile
        command:
          - "python"
          - "manage.py"
          - "runserver"
          - "0.0.0.0:8080"
        ports:
          - "8000:8080"
        logging:
          driver: loki
          options:
            loki-url: http://host.docker.internal:3100/loki/api/v1/push

      grafana:
        image: grafana/grafana:9.2.15
        environment:
          - GF_AUTH_ANONYMOUS_ENABLED=true
          - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
        ports:
          - "3000:3000"
      loki:
        image: grafana/loki:2.8.0
        ports:
          - "3100:3100"

 - Теперь пересобираем и запускаем контейнер. В терминале: docker compose build app и docker compose up -d app
    Если логи в loki на странице http://localhost:3000/ не появились, то можно использовать другой адрес для loki
    в файле Dockerfile: http://localhost/loki/api/v1/push

 - Если вдруг нужно удалить контейнер, в терминале: docker compose rm -s -v app # После выполднения нажать "Y", соглашаемся

 - Остановка вообще всех сервисов, в терминале: docker compose down -v

                                        **************************************
                                                        Sentry

Sentry - https://sentry.io/        # сервис для сбора инфы по ошибкам
Django | Sentry Documentation - https://docs.sentry.io/platforms/python/guides/django/

Лучше всего использовать облачную версию sentry, тк локальная требует множество ресурсови ее лучше развекртывать на отдельной виртуальной машине отдельным специалистам
Мы будем тестить облачную версию

 - Регаемся на sentry, создаем новый проект python, называем django-app, выбираем "I'll create my own alerts later", Скипаем предложение добавить sdk фрэймворка

- Ставим в терминале sentry: pip install --upgrade sentry-sdk и морозим pip freeze > requirements.txt

 - Скопируем начальную настроку и вставим в mysite/mysite/settings.py
    import sentry_sdk

    sentry_sdk.init(
        dsn="https://6dc8a78edfbae6dbc24c78bba9072649@o4505901180715008.ingest.sentry.io/4505901229473792",
        traces_sample_rate=1.0,
    )

============================================================================================================================

                                    *******************************************
                                                Экспорт данных

                                        Форматы данных XML, JSON, YAML
YAML.org - https://yaml.org/
XML — Wikipedia - https://en.wikipedia.org/wiki/XML
JSON — Wikipedia - https://en.wikipedia.org/wiki/JSON
Введение в REST API — RESTful веб-сервисы  - https://habr.com/ru/articles/483202/
Различия REST и SOAP / Хабр - https://habr.com/ru/articles/483204/

JavaScriptObjectNatation (JSON) - хранение и передача массива данных с правилами разметки (похож на словари, но ключи только строки!)

ExtandsibleMarkupLanguish (XML) - Описание и структурирования данных в виде дерева (есть пространство имен). Внешне похож на HTM
    (но создан для хранения и передачи данных, а не для отображения, как HTML). В HTML уже готовые тэги, в XML тэги создаем сами
    Больше подходит для передачи больших и сложных структур данных

SimpleObjectAcessProtocol (SOAP) - Используется для обена данными между клиент/сервер. Можно передавать различные данные, в том числе бинарные
    Используется для удаленного вызова процедур (RPC) и получекния данных в ответ (например в банковских процедурах). Есть спец
    конверт для передачи данных (envilop). На смену ему так же пришел JSON (он легче и быстрее)

YetAnotherMarkupLanguage - Язык разметки для создания и хранения конфигураций приложений (на нем мы описывали конфигурациюв Docker compose)
    Удобен для написания и чтения человеком. проще JSON (меньше знаков припинания)

                                        ***********************************************
                                                        Импорт данных

 - Что бы экспортировать фикстуры в формте XML, в терминале набираем: python manage.py dumpdata --format xml shopapp.Product > shopapp-products-fixtures.xml (для этого нужнол установить пакет xml)

 - Создадим форму для импорта/экспорта для django_admin в mysite/shopapp/forms.py
    class CSVImportForm(forms.Form):
        csv_file = forms.FileField()

 - Добавим папку в шаблоны в mysite/shopapp/templates/admin (что бы расширить админские шаблоны) и создадим файл csv_form.html
    {% extends 'admin/base.html' %} # Расширяем базовый админский шаблон

    {% block content %}
        <div>
            <form action="." method="post" enctype="multipart/form-data"> # form action="." - указываем, что действие на текущей странице
                {% csrf_token %}
                {{ form.as_p }}
                <div class="submit-row">                              # Делаем такой же стиль кнопок как и в стандартной джанго-админке
                    <input type="submit" value="Upload CSV">
                </div>
            </form>
        </div>
    {% endblock %}

 - Импортируем форму в mysite/shopapp/admin.py
    from django.urls import path
    from django.shortcuts import render
    from .forms import CSVImportForm

    # И добавим новые методы в класс ProductAdmin
    def import_csv(self, request: HttpRequest) -> HttpResponse:
        form = CSVImportForm()
        context = {
            "form": form,
        }
        return render(request, "admin/csv_form.html", context)

    def get_urls(self):
        urls = super().get_urls()      # Переопределяем родительский метод, что бы вернуть список адресов + новый адрес для импорта
        new_urls = [
            path(
                "import-products-csv/",
                self.import_csv,
                name="import_products_csv"
            )
        ]
        return new_urls + urls   # new_urls обязательно ставим вначале!!!! Иначе некоторые правила могут его не добавить в список адресов

 - Добавим шаблон в mysite/shopapp/tempalates/shopapp/products_changelist.html
    {% extends 'admin/change_list.html' %}                                      # Именно так называется шаблон в админке, со списком товаров

    {% block object-tools-items %}                                              # Это блок с кнопками в админке
    {% load admin_urls %}                                                       # Что бы точно подгрузились админские ссылки
        <li>
            <a href="{% url 'admin:import_products_csv' %}" class="addlink">    # class="addlink" делает стиль кнопки как и у всех остальных
                Import CSV
            </a>
        </li>
        {{ block.super }}                                                       # Переопределим родительский класс с кнопками
    {% endblock %}

 - Добавим шаблон в класс ProductAdmin (mysite/shopapp/admin.py)
    change_list_template = "shopapp/products_changelist.html"

 - Создадим в корне проекта файл для проверки devices.csv
    name,description,price,discount
    "laptop 14","A new one","29900.00",5
    "laptop 16","A bigger one","49900.00",7

 - Добавим шаблон в класс ProductAdmin (mysite/shopapp/admin.py) метод для чтения файла:
    from io import TextIOWrapper
    from csv import DictReader

    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):

        def import_csv(self, request: HttpRequest) -> HttpResponse:
            if request.method == "GET":
                form = CSVImportForm()
                context = {
                    "form": form,
                }
                return render(request, "admin/csv_form.html", context)
            form = CSVImportForm(request.POST, request.FILES)
            if not form.is_valid():
                context = {
                    "form": form,
                }
                return render(request, "admin/csv_form.html", context, status=400)

            csv_file = TextIOWrapper(
                form.files("csv_file").file,
                encoding=request.encoding,
            )
            reader = DictReader(csv_file, )

            products = [
                Product(**row, created_by_id=1) # Добавляем, тк в БД есть обязательное поле и в файл CSV его вписать нельзя
                for row in reader
            ]
            Product.objects.bulk_create(products)
            self.message_user(request, "data from CSV was imported")
            return redirect("..")               # ТК страница создания, на одну ступень ниже стьраницы с формой, просто пишем 2 точки, что бы подняться на уровень выше

                                    ****************************************************
                                                        Файлы в DjangoRestFramework

Viewsets — Django REST framework - https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
TextIOWrapper | io — Core tools for working with streams — Python 3.11.3 documentation - https://docs.python.org/3/library/io.html#io.TextIOWrapper


Важно! Модули viewset не нужно отдельно регистировать в urls, тк они сами передают инфу в default routers

 - Добавим новые действия для экспорта данных в файл из API. в mysite/shopapp/views.py:
    from csv import DictWriter
    from rest_framework.decorators import action
    from rest_framework.request import Request

    @extend_schema(description="Product views CRUD")
    class ProductViewSet(ModelViewSet):
        """
        Набор представлений для действий над Product.

        Полный CRUD для сущностей товара.
        """
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        filter_backends = [
            SearchFilter,
            DjangoFilterBackend,
            OrderingFilter,
        ]
        search_fields = ["name", "description"]
        filterset_fields = [
            "name",
            "description",
            "price",
            "discount",
            "archived",
        ]
        ordering_fields = [
            "name",
            "price",
            "discount",
        ]
        @extend_schema(
            summary="Get one product by ID",
            description="Retrieves **product**, returns 404 if not found ",
            responses={
                200: ProductSerializer,
                # 404: None,
                404: OpenApiResponse(description="Empty response, product by id not found"),
            }
        )
        def retrieve(self, *args, **kwargs):
            return super().retrieve(*args, **kwargs)

        @action(methods=["get"], detail=False) # detail=False - путь к download_csv должен быть построен на сонове списка элементов
        def download_csv(self, request: Request):
            response = HttpResponse(content_type="text/csv")
            filename = "products-export.csv"
            response["Content-Disposition"] = f"attachment; filename={filename}"
            queryset = self.filter_queryset(self.get_queryset())      # Так делаем, что бы фильтры из filterset_fields (которые выше, так же применялись и к queryset)
            fields = [
                "name",
                "description",
                "price",
                "discount",
            ]
            queryset = queryset.only(*fields)
            writer = DictWriter(response, fieldnames=fields)
            writer.writeheader()

            for product in queryset:
                writer.writerow({                  # Записываем построчно каждое поле продукта в файл csv
                    field: getattr(product, field) # Получаем значения полей по ключу field
                    for field in fields
                })
            return response

 - Теперь сделаем функцию импорта csv в django rest, для этого изменим файл mysite/shopapp/admin.py:
    Добавим отдельную функцию (вне класса и изменим сам класс ProductAdmin)
        @admin.register(Product)
        class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
            change_list_template = "shopapp/products_changelist.html"
            actions = [
                mark_archived, mark_unarchived, "export_csv"
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

            def import_csv(self, request: HttpRequest) -> HttpResponse:
                if request.method == "GET":
                    form = CSVImportForm()
                    context = {
                        "form": form,
                    }
                    return render(request, "admin/csv_form.html", context)

                form = CSVImportForm(request.POST, request.FILES)
                if not form.is_valid():
                    context = {
                        "form": form,
                    }
                    return render(request, "admin/csv_form.html", context, status=400)

                save_csv_products(
                    file=form.files["csv_file"].file,
                    encoding=request.encoding,
                )
                self.message_user(request, "data from CSV was imported")
                return redirect("..")

            def get_urls(self):
                urls = super().get_urls()
                new_urls = [
                    path(
                        "import-products-csv/",
                        self.import_csv,
                        name="import_products_csv",
                    )
                ]
                return new_urls + urls


        def save_csv_products(file, encoding):                          # Функцию добавляем вне класса. отдельно
            csv_file = TextIOWrapper(
                file,
                encoding=encoding,
            )
            reader = DictReader(csv_file)
            products = [
                Product(**row, created_by_id=1)
                for row in reader
            ]
            Product.objects.bulk_create(products)
            return products

 - Далее в папке shopapp создадим новый файл common.py, далее ПКМ по нему и copy reference (abolute path)
 - После этого ПКМ по функции save_csv_products() -> refactor -> move -> и в путь вставляем то, что скопировали выше
    Так в новый файл перенесется не только функция но и все ее зависимости

 - Если нужно добавить к какой либо строке список объектов то сделать это можно так (Все в том же файле mysite/shopapp/common.py)
    from csv import DictReader
    from io import TextIOWrapper
    from shopapp.models import Order, Product


    def save_csv_orders(file, encoding):
        csv_file = TextIOWrapper(
            file,
            encoding=encoding,
        )
        reader = DictReader(csv_file)
        product_pk = [product.pk for product in Product.objects.all()]
        print(product_pk)
        orders = [
            Order(**row, user_id=1)
            for row in reader
        ]
        instance = Order.objects.bulk_create(orders)
        for order in instance:                        # Тут уже после создания объектов, добавляем в каждый заказ список продуктов product_pk
            order.products.set(product_pk)

        return instance

 - Теперь можно Сделать импорт из файла через вью функцию (не админку), добавим новое действие на modelviewset в mysite/shopapp/views.py
    from rest_framework.parsers import MultiPartParser
    from .common import save_csv_products
    from rest_framework.response import Response

    @extend_schema(description="Product views CRUD")
    class ProductViewSet(ModelViewSet):
        # Не буду снова копировать весь класс, он есть выше
        serializer_class = ProductSerializer
        @action(
                detail=False,
                methods=["post"],
                parser_classes = [MultiPartParser],
            )
        def upload_csv(self, request: Request):
            products = save_csv_products(
                request.FILES["file"].file,
                encoding=request.encoding,
            )
            serializer = self.get_serializer(products, many=True) # Тут мы берем сериалайзер, который объявляли раньше (ProductSerializer), потому юзаем толькол встроенный метод
            return Response(serializer.data)

 - После с помощью помошника через терминал можно загрузить файл. Для это вначале на странице shop/api/products в extraoptions
выбираем upload csv -> по нему ПКМ - копируем ссылку и потом вводим в терминале:
 curl -X POST -F 'file=@devices.csv' http://127.0.0.1:8000/ru/shop/api/products/upload_csv/      # У меня не сработало

                                    ************************************************
                                                    Лента новостей

RSS — Википедия - https://ru.wikipedia.org/wiki/RSS
The syndication feed framework | Django documentation - https://docs.djangoproject.com/en/4.2/ref/contrib/syndication/

 - Создадим новое приложение для RSS фида. Для этого перейдем в проект blogapp (создавали раньше).

 - В файле mysite/blogapp/views.py:
    from django.urls import reverse_lazy
    from .models import Article
    from django.views.generic import ListView, CreateView, DetailView


    class ArticlesListView(ListView):
        template_name = "blogapp/articles-list.html"
        context_object_name = "articles"
        queryset = (
            Article.objects
            .select_related("author", "category")
            .prefetch_related("tags")
            .filter(pub_date__isnull=False)         # Не даст перейти к черновикам другим пользователям
            .order_by("-pub_date")                  # Просто сортировка по дате публикации
        )

- Добавим управление статьями в админку. В файле mysite/blogapp/admin.py:
    from django.contrib import admin
    from .models import Article

    @admin.register(Article)
    class ArticleAdmin(admin.ModelAdmin):
        list_display = "id", "title", "content", "author", "category", "pub_date"

 - Настроим ленту RSS в файле mysite/blogapp/views.py:
    from django.contrib.syndication.views import Feed
    from django.urls import reverse_lazy, reverse

    class LatestArticlesFeed(Feed):
        title = "Blog articles (latest)"
        description = "Updates on changes and addition blog articles"
        link = reverse_lazy("blogapp:articles_list")

        def items(self):
            return (
                Article.objects
                .select_related("author", "category")
                .prefetch_related("tags")
                .filter(pub_date__isnull=False)
                .order_by("-pub_date")[:5]
            )

        def item_title(self, item: Article):                            # Метод возвращает заголовок статьи
            return item.title

        def item_description(self, item: Article):                      # Метод возвращает сокращенный текст статьи
            return item.content[:200]

        def item_link(self, item: Article):                             # Метод переадресовывает на статью, которая понравилась
            return reverse("blogapp:article", kwargs={"pk": item.pk})

 - Добавим новый класс в mysite/blogapp/urls.py:
    from django.urls import path
    from .views import (
        ArticlesListView,
        CreateArticleView,
        ArticleDetailView,
        LatestArticlesFeed,
    )

    app_name = "blogapp"

    urlpatterns = [
        path("articles/", ArticlesListView.as_view(), name="articles_list"),
        path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article_details"),
        path("articles/create/", CreateArticleView.as_view(), name="create_article"),
        path("articles/latest/feed/", LatestArticlesFeed(), name="articles-feed"),  # ТК это не вью функция то и добавляем ее как экземпляр функции
    ]

 - Что бы нормально читать фид, нужно досустановить плагин на браузер, например RSS Feed Reader и уже в него добавить ссылку
http://127.0.0.1:8000/blog/articles/latest/feed/

                                        ********************************************
                                                        Карта сайта
Нужна для индексации сайта в поисковых системах типа Google, Yandex и тд. Карта сайта создается для каждого приложения в проекте

Site map — Wikipedia - https://en.wikipedia.org/wiki/Site_map
The sitemap framework | Django documentation - https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/

 - Создадим файл в mysite/blogapp/sitemap.py:
    from django.contrib.sitemaps import Sitemap
    from .models import Article

    class BlogSiteMap(Sitemap):
        changefreq = "never"                                       # Как часто обновляется страница (always, hourly, daily, weekly, monthly, yearly)
        priority = 0.5                                             # На сколько главной страница являеется (от 0.1 до 1)

        def items(self):
            return Article.objects.filter(pub_date__isnull=False).order_by("-pub_date")

        def lastmode(self, obj: Article):
            return obj.pub_date

 - Далее сделаем абсолюный юрл в mysite/blogapp/models.py:
    class Article(models.Model):
        """
        Модель представляет статью для блога.
        """
        class Meta:
            verbose_name = "Article"
            verbose_name_plural = "Articles"

        title = models.CharField(max_length=200, verbose_name="title")
        content = models.TextField(max_length=500, blank=True, verbose_name="content")
        pub_date = models.DateTimeField(auto_now_add=True, verbose_name="pub_date")
        author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="author")
        category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
        tags = models.ManyToManyField(Tag, related_name="articles", verbose_name="tags")

        def get_absolute_url(self):
            return reverse("blogapp:article_details", kwargs={"pk": self.pk})

 - Далее перенесем все классы sitemap (тк их ко одному на каждое приложение) в корень проекта mysite/mysite/sitemaps.py
    from blogapp.sitemap import BlogSiteMap

    sitemaps = {
        "blog": BlogSiteMap,
    }

 - Осталось добавить адрес в корневой url -> mysite/mysite/urls.py:
    from django.contrib.sitemaps.views import sitemap                     # Это вью функция из django.contrib
    from .sitemaps import sitemaps                                        # А это объект из файла sitemaps
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns = [
        path('req/', include('requestdataapp.urls')),
        path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
        path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name="swagger"),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
        path('api/', include('myapiapp.urls')),
        path('blog/', include('blogapp.urls')),
        path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap", # Тут в принципе не осбо важно, какое имя указать, но лучше так
        ),
    ]

 - Теберь добавим приложение в установленные приложения в mysite/mysite/settings.py:
    INSTALLED_APPS = ['django.contrib.sitemaps',]

 - После, можно перейти по адресу http://127.0.0.1:8000/sitemap.xml и увидеть xml файл с имнфой по странице сайта