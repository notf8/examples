
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

 - Установим Django Debug Toolbar, в терминале ввести: pip install django-debug-toolbar и заморозм: pip freeze requirements.txt

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