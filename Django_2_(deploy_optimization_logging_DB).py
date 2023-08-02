
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