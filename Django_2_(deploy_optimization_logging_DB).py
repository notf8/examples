
                                        *********************************************************
                                             ����������� �������������� � ����� ������

�������������� ���� ������. ������ �������� - https://habr.com/ru/company/otus/blog/471016/
��� ������� ����������� (�� � ��) - https://habr.com/ru/post/349910/
QuerySet API reference, Django documentation - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#select-related

                                        **********************************************
                                                    �������� �����������
1) �������: ����� ��� ������, ���������� � ����������, �������� ��������� �� ����� ������� (db_index = True)

 - ������� ������� �� ������: mysite/shopapp/models.py
    class Product(models.Model):
        class Meta:
            ordering = ["name", "price"]
            verbose_name = _('Product')
            verbose_name_plural = _('Products')

        name = models.CharField(max_length=100, verbose_name=_("Name"), db_index=True)
        description = models.TextField(null=False, blank=True, verbose_name=_("Description"), db_index=True)

 - ���������� �������� � ���������: python manage.py makemigrations � ����� python manage.py migrate

2) ������������ ��: ��������� ������������ ����. ����� �������� ������ �������� � ����� �������, ������������ ����� � ��������� �����
� ��� �� ����� ������������ �������� ��������� (��������� ����� ������� ���� �� ������� - ���������� ���� ������)

                                        ************************************************
                                                 ����������� SQL ��������

 - ������� ������� ��� ����������� �������� � ����� ����� mysite/mysite/settings.py
    �����!!! ������ ������� ������ ���� ������������ ������ � debug ������!!! (������ ��� ����� ������� 'filters': ['require_debug_true'],)
    LOGGING = {
        'version': 1,
        'filters': {
            'require_debug_true': {                        # ��� ���������, ��� ����� ����������� ������ ������ � debug ������ (��� �� ������ � ���� ����� DEBUG = True)
                '()': 'django.utils.log.RequireDebugTrue'  # ������ ��� ��� ��������� �������� ����, ������ ���� ������� debug �����
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',           # ���� ����� ����� �������� ��� ������� � ��������
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
        },
    }

 - ������ �������� �� �������� � ���������� � � ��������� �������� ������ � ��. ��� ��������� � ������� � ���� quieries.sql, ������� �������� � ����� �������
    ��� ����� ��� �������� ������, �� � pycharm comunity �� �������� �������������� ����� ctrl+shift+l - ��� ��� �� ��� ����

 - �����!!!
    prefetch_related - ��������� ����� ���� �� ������
    select-related - ��������� ����� ���� � ������
    � ������ � ������ ������ ����������� ������������ ��� ���������� ���-�� �������� � ��, �� ������� ����� ����
        class OrdersListView(LoginRequiredMixin, ListView):
            queryset = (
                Order.objects
                .select_related("user")           # ����� �� ������� ���������� ������������, ��� �� ������ �� ��������� ������ ��� � �� ��� �������� ������ ������
                .prefetch_related("products")     # ����� �� ����� ���������� ��� ������ �� ����, ��� �� �� ����������� �� ��� ������� ������
            )                                     # ����� �������, ��� ����������� ������ ����� ���������� ������ � �� ��� ������� ������
                                                  # ��� �� ���������� ������������ � ������, � ���� ������� 100, �� ������ �����

                                            *************************************************
                                                                �������� N+1

�������� ������ N + 1 � ��������-����������� ������������� (ORM) - https://intellect.icu/problema-vybora-n-1-o-v-obektno-relyatsionnogo-sopostavleniya-orm-8653
QuerySet API reference, Django documentation - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#select-related

N+1 - ���� ��������: ������ ����� ��������� �� ������ �������� � ������ ��������. �� ����� �� ��������� ���� ������, � �
���� ������ ����� ������� ��� ������, ������ ��� � ��� ���� ������ �� ������ ������, ��� 1 - ��� ������ ������, � N - ���
���������� ����������� ��������� (�������� � 1 ������ ����� ���������� N ��������������)

 - lazy Loading - ������� ���������. �������� ����� ���������� ������ ��������� �� ������� (� ���� �� ������� � ������������� �� �����)
    ������ ����� ������ ���������� django. �� ���� ��� �������� �� ���������. ��� � ���� ������� ����� ����������� ���-��
    ��������. ������ � ���������� select_related � prefetch_related. ���������� ��������� ���������� ������ ���, ��� �����
    �����, ��� ��� ������� ��� �� �����������

                                        *****************************************************
                                                        ���������� � ����� ������

��� ����� ���������� (�����) - https://habr.com/ru/post/537594/
��� ����� ���������� ���� ������? AppMaster - https://appmaster.io/ru/blog/chto-takoe-tranzaktsiia-bazy-dannykh
Database transactions, Django documentation - https://docs.djangoproject.com/en/4.1/topics/db/transactions/

 - ������� ������� �������� ������ ��� �������� ���������� � mysite/shopapp/management/commands/create_order.py
    from typing import Sequence
    from django.db import transaction
    from django.contrib.auth.models import User
    from django.core.management import BaseCommand
    from shopapp.models import Order, Product

    class Command(BaseCommand):
        @transaction.atomic                                      # atomic - �������� �� �������� (����������) ������, ��� ������������� ������
        def handle(self, *args, **options):                      # ��� �� atomic ����� ����� �� ��� ���������, � ��� ����������� ��������: with transaction.atomic(): ....
            self.stdout.write("Create order with products")
            user = User.objects.get(username="admin")
            products: Sequence[Product] = Product.objects.all()
            order, created = Order.objects.get_or_create(        # ����� ���� �� �������� created � ����������, ������� ������, �� � ���������� �������� ������ � ������� (���� �� ����) � �������� (����/���)
                delivery_address="ul Ivanova, d 17/1",
                promocode="promo1",
                user=user,
            )
            for product in products:
                order.products.add(product)
            order.save()
            self.stdout.write(f"Created order{order}")

 - ����� � ��������� �������� ������� python manage.py create_order

                                        ******************************************************************
                                                ������ ����������� �������� � ���������� ��������

QuerySet API reference, Django documentation, values - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#values
QuerySet API reference, Django documentation, bulk-create - https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create

 - ���� ���������� � ������ ��������� �� �� � ����� � ���� ����� �����, �� ����� ������� ������� ������ ������ � ��� �����,
   ������� ��� �����, ��������� �� � ���������� � ������ ������������ ���������� � ������, ��� �� �� ������ ������� � ����

 - ��� �� ��������� ����� ��������, ����� ������������ ����� �� �� � ����� ������� � ������� JOIN

 - ���� ����� ����������� ����� ��������, �� ����� ������� ������� ���� �� �� id � � ������� ��������� IN ���������� �� � filter()

 - ��������� �������� �����. ��� ����� �������� ����� ������� � mysite/shopapp/management/commands/selecting_fields.py (���� ����� �������)
    from django.contrib.auth.models import User
    from django.core.management import BaseCommand
    from shopapp.models import Product

    class Command(BaseCommand):
        def handle(self, *args, **options):
            self.stdout.write("Start demo select fields")

            users_info = User.objects.values_list("username", flat=True) # ��� ��������� ������ username, flat=True - �������� ��� ��� ����� ����� ������� � ���� ������, � �� �������� �� �����������
            for user_info in users_info:                                 # ��� �����! � �������� ���������� ����� values_list, � �� ��� ����, � ������� Product, ����� ������ values
                print(user_info)

            # products_values = Product.objects.values("pk", "name")     # ��� ��������� ������ id  � �� ������ ���������
            # for p_values in products_values:
            #     print(p_values)
            self.stdout.write("Done")

    # ����� defer ��������� �������� �������� ����� �� ��� ���, ���� ��� �� �����������
    products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all()  # � ������� ��������� ����, ������� �� �����
    products: Sequence[Product] = Product.objects.only("name", "price").all() # only - �������� (� ������� �� defer), � ������� ����� ������ �� ����, ������� ����� ���������

 - ������ �������� ������� (�������� ����� ���� �  mysite/shopapp/management/commands/bulk_actions.py)

    bulk_create - ��������� ������� ��������� �������� �� ���� ��� (�� ���� ������)
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
                    Product(name=name, price=price, created_by_id=1) # ��� ���� �������� ��� ����� created_by_id, �� ��� ������������ ����
                    for name, price in info                          # ���� ,������� �� �� �������, ���������� ���������� �� ���������
                ]
                result = Product.objects.bulk_create(products)
                for obj in result:
                    print(obj)
                self.stdout.write("Done")

    bulk_update - ��������� �������� ��������� �������� �� ���� ��� (�� ���� ������)
        class Command(BaseCommand):
            def handle(self, *args, **options):
                self.stdout.write("Start demo bulk_actions")
                result = Product.objects.filter(
                    name__contains="smartphone",            # ��� ������� �������, ������ ��������, � ��������� ������� ���������� "smartphone"
                ).update(discount=10)                       # ��� ����� queryset ��������� �������
                print(result)

                                        *************************************************
                                                        ��������� � ���������

Aggregation, Django documentation - https://docs.djangoproject.com/en/4.1/topics/db/aggregation/
Annotation, Django documentation - https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#joins-and-aggregates
Django Annotations: steroids to your Querysets by Gautam Rajeev Singh, Medium - https://medium.com/@singhgautam7/django-annotations-steroids-to-your-querysets-766231f0823a

 - ��������� ��������� ��������� �������� ��� ����������� ��������� (�������� ������� ��������� ����������). �������� ������� mysite/shopapp/management/commands/agg.py
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
            #     average_price=Avg("price"), # ��� ����� ���������, � ����� ������ ������� ���� (��� �� �� �������� �������� �� ������)
            #     max_price=Max("price"),
            #     min_price=Min("price"),
            #     count=Count("id"),
            # )
            # print(result)

            orders = Order.objects.annotate(
                total=Sum("products__price", default=0),   # ��� 2 �������������!! default=0 - ������, ���� �� ����� ������ �������� None, ����� � ������ �����
                products_count=Count("products"),        # ��� ��������� ��� ��� ���������� � ������������ ������� ����� �� products__price
            )
            for order in orders:
                print(
                    f"Order {order.id} "
                    f"with {order.products_count} "
                    f"products worth {order.total}"
                )
            self.stdout.write("Done")
    ����� ������ ������ ������� � ���������: python manage.py agg
    ��������� ����� ����������, ���� ����� ����������� ������ ��� �����-���� ������, ��� �� �� ���������� ��� ���� ��� �����

                                        *************************************************
                                                ������������ � ��������������

Logging | Django documentation - https://docs.djangoproject.com/en/4.2/topics/logging/
Logging HOWTO � Python 3.11.3 documentation - https://docs.python.org/3/howto/logging.html

 - Logging, ������:
  - Debug - �������������� �����������,���� � ������ ���� ����������
  - Info - �� ���������� ��� �� �������� (�� ����, �� ������������� ��� �������)
  - Warmibg - ������ ����������� �� ����������� �������
  - Error - ���� � ��������� ��������
  - Criticsl - ��������� � ����������� ������

  �����! ������, ������� ����, ��� ������������ � �������, ������ �� ����� ���������� (�� ���� ����� Critical, �� info ������� �� �����)

 - ������ ����� � ���� � ��������� ������� ���-������ � �mysite/mysite/settings.py
    LOGFILE_NAME = BASE_DIR / "log.txt"             # ��������� ��� �����
    LOGFILE_SIZE = 1 * 1024 * 1024                  # ������ ����� ��� ������� � ������ (1 * 1024 * 1024 = ��������)
    LOGFILE_COUNT = 3                               # ������� ������ ����� ������� (3 - ���������� ���������� + 1 �������)

 - �������� logging � ���������� mysite/mysite/settings.py
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s", # ��� ����� asctime ��� �� �������� �����, � [] - ��� ������� ������ ����������, � () - ��������� ���������� ��� ������
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
            "logfile": {
                # "class": "logging.handlers.TimedFileHandler", (��� ������� ����� �� ����)
                "class": "logging.handlers.RotatingFileHandler",       # ��������� ����� ��� ��������� ����� (������� �� ������� �����)
                "filename": LOGFILE_NAME,                        # ������ ������ ����� ����������, ������� ������� �����
                "maxBytes": LOGFILE_SIZE,
                "backupCount": LOGFILE_COUNT,
                "formatter": "verbose",                     # �������������� ��������� �� �� �����, ��� � ���� � ������
            },
        },
        "root": {
                "handlers": [
                    "console",
                    "logfile",                              # ��� ������ � ������ ��������� �������, ������� ������� ����
                ],
                "level": "INFO",
            },
        }

 - ������� ������������ � ���������� mysite/shopapp/views.py
    import logging
    log = logging.getLogger(__name__) # � ������� ��������� ��� �������� ������, ��� ����������� ������ �����������

    class ShopIndexView(View):
        def get(self, request: HttpRequest) -> HttpResponse:
            links = [
                {"title": "������ ���������", "address": "products/"},
                {"title": "������ �������", "address": "orders/"},
            ]
            context = {
                "time_running": default_timer(),
                "links": links,
                "items": 5,
            }
            log.debug("Products for shop index: %s", links) # � ������� �������� ������� ��������������, ������ ���, ���� ��� �� ��������� �������� ������� debug
            log.info("Rendering shop index") # ����������� ����� �� ����, ��� ������� ������ ������, ���� ��������� ������ �� return, �� ����� ��� ������ � �����
            return render(request, 'shopapp/shop-index.html', context=context)

                                **************************************************
                                            ����� ����� ��������������?
Optimize your code using profilers | PyCharm Documentation - https://www.jetbrains.com/help/pycharm/profiler.html
Django Debug Toolbar - https://django-debug-toolbar.readthedocs.io/en/latest/

�������������� - ��� ������� ������� ������������������ ���� (��������� ����� ����)

 - ��������� Django Debug Toolbar, � ��������� ������: pip install django-debug-toolbar � ��������: pip freeze requirements.txt

 - ������� ���������� � ������������� � mysite/mysite/settings.py:
    INSTALLED_APPS = ['debug_toolbar',]

 - ��� �� ������� ��� � ������ middleware � mysite/mysite/settings.py:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',]

 - ������� ��������� � ����� ������������ � mysite/mysite/settings.py:
    INTERNAL_IPS = [
        "127.0.0.1",                                # ��� ���������, �� ������ IP ����� �������� ������ � DebugToolbar
    ]

 - ������� ���������� � mysite/mysite/urls.py:
    if settings.DEBUG:
        urlpatterns.extend(
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        )
        urlpatterns.append(
            path("__debug__/", include("debug_toolbar.urls")),
        )

 - ������ �������� ������ SQL ��� ������� � ������� (������ ������ ���� ����������):
    � ��������� ������: python manage.py debugsqlshell

                                **************************************************
                                                    Docker
Docker - https://www.docker.com/
Docker Hub - https://hub.docker.com/

Docker - ��������� ��� ��������, ������������� � ���������� ������������ � ������������� �����������
Docker compose - ��������� ����� ����� ������������ � ��������� ��������� �� � ���������� �������

 - ��� �� �������� � �����: � CMD �� ������: wsl --install. ��� ����������: wsl --update
   ��� �� ����� �������:
   1) ���������(����������) -> ���������� -> ���������� � ����������� -> "windows for linux ����" = ������� ���
   2) ������ ���������� -> �������� � ���������� -> ��������� ��� ���������� ����������� windows -> ���� "���������� windows ��� linux" = ������� �������