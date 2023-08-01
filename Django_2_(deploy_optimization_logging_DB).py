
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
    И первый и второй способ оптимизации используется для уменьшения кол-ва запросов к БД, на примере вьюхи это видно ниже
        class OrdersListView(LoginRequiredMixin, ListView):
            queryset = (
                Order.objects
                .select_related("user")           # Здесь мы заранее подгружаем пользователя, что бы джанго не обращался каждый раз к БД при загрузке нового заказа
                .prefetch_related("products")     # Здесь мы сразу подгружаем все товары из базы, что бы не запрашивать их для каждого заказа
            )                                     # Иными словами, без оптимизаций джанго будет обращаться дважды к БД для каждого заказа, что бы подгрузить пользователя и товары, а если заказов 100, то сервак ляжет
