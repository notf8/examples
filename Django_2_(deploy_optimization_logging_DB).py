
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

 - ��������� Django Debug Toolbar, � ��������� ������: pip install django-debug-toolbar � ��������: pip freeze > requirements.txt

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

 - � ����� ������� misite ������ ������ ���� "Dockerfile" (��� ����������) � ���� ".dockerignore" (��� ����������� ��, ���� �� ������ ���� � ����������)

    ������ ����� ".dockerignore" (����� ����� �� ���������):
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

    ������ ����� "Dockerfile" (���� ��� �� ������ � ����� �� ����� ��������� ������ ������!):
        FROM python:3.11

        WORKDIR /app           # � ���� ����� ����� �������� ����������

        ENV PYTHONUNBUFFERED=1                  # ����������� �������� ��� ������ ������ � ������

        COPY requirements.txt requirements.txt  # ������ - ����� ��� ����������, ������ - ��� ���������

        RUN pip install --upgrade pip
        RUN pip install -r requirements.txt

        COPY mysite .                           # "." �������� ������� ����������

 - ����� �������� ���������. ��� ����� ����� ������� � ��������� � �������� ����� ��� ����� �������� ����� mysite (�� ������ mysite), �����!! ����� � ���� ������ ������ ���� ������� �� �����
    ������ �������: docker build . -t app   # "." ��������, ��� �������� � ������� �����������. "-t app" - ��� ����� ������

 - ��� ������� ���������� ���������� � ��������� ������: docker run -it app bash  # -it ������ ������������� �����.
    - ls - ����� �������, ���� �������� ����� ����������, ����� ���� ���� � ����������� ���������� (��� ���������� ������ dir)
    - ����� ����� ��������� ������ ��������� ��������: python manage.py runserver (��������������� ������ ��� ������ ctrl + C)
    - �������� ������ ����� �������� exit
    - ��� �� ��������� ������ � ������� ����� �������: curl http://127.0.0.1:8000/

                                        ***************************************************
                                            Docker compose (����� ��� ��������� �������)

 - �������� ���� docker-compose.yaml � �������� ����� ������� ��� ����� �������� ����� mysite (�� ������ mysite)
    version: "3.9"

    services:                                               #������� �������������!
        app:
            build:
                dockerfile:./ Dockerfile
            command:
                - "python"
                - "manage.py"
                - "runserver"
                - "0.0.0.0:8080"                            # ��������� �� ������ ����� �������� ����������
            ports:                            # ��� ����� ���������� �����, ��� �� ��� ���� �������� �� ������ �� �����
                - "8000:8080"   # 8000 - ���� �������� ������, 8080 ����, �� ������� ����������� ���������� (��� ��, ��� ������ � command

 - ������� ���� � ���������� ���������� � mysite/mysite/settings.py:
    ALLOWED_HOSTS = [
        "0.0.0.0",
        "127.0.0.1",
    ] # ��� ������� ��������� ����� �� ������ �� ������� �����
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

    if DEBUG:              # �����!!! ����� �� ����������, ���� �������� LANGUAGES = [] �� ���������������� (����� �� ��������� � gettext
        import socket
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname()) # ��� ������ ��� �� �������� ����� ��� ������ DEBUGTOOLBAR
        INTERNAL_IPS.append("10.0.2.2")
        INTERNAL_IPS.extend(
            [ip[: ip.rfind(".")] + ".1" for ip in ips]
        )

 - ������� ��������� � compose, � ��������� ������: docker compose build app

 - ��� ������� ���������� � compose ������ � ���������: docker compose up -d app # -d �������� ����� � ������ �� ��������� (��� ������� � ��������� (docker compose up app)
   ��� �� �������� ���� � ����� -d, ����� ������ �������: docker compose logs -f app # -f �������� �������� ���� � ��������� �������

                                        ********************************************
                                                    ���� � Grafana Loki

Grafana | Query, visualize, alerting observability platform - https://grafana.com/grafana/
Grafana Loki OSS | Log aggregation system - https://grafana.com/oss/loki/
https://github.com/grafana/loki/tree/main/production

Grafana - ������ ������������� ����. � Loki �� ��������

 - �������� �������� Grafana Loki. � ����� /mysite/Dockerfile:
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
          - GF_AUTH_ANONYMOUS_ENABLED=true          # ��������� ������ ��� �����
          - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin        # ���� ���� ����� ������
        ports:
          - "3000:3000"
      loki:
        image: grafana/loki:2.8.0
        ports:
          - "3100:3100"

 - �������� �������. � ��������� ������: docker compose pull

 - ��������� ������� � ����� ������, � ���������: docker compose up -d grafana loki

- �� ������ http://localhost:3000/?orgId=1 ����� ������� �� ������� grafana.com

- � ������ ����� ���� ����������� (���������), ��������� � ������� add data sources, ��� �������� loki. ����� � ���������
    url ������ �����: http://loki:3100 # ����� ������������ ���� � ��� save and test

 - ��������� ������ ��� ����� ����� ��� Loki. � ��������� ������: docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions # ����� ��������� ����������� ������������� docker

 - ����� ����������� docker, � �������� ������: docker plugin ls # ���������, ����������� �� ������

 - ������� ������ � ���� /mysite/Dockerfile:
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

 - ������ ������������ � ��������� ���������. � ���������: docker compose build app � docker compose up -d app
    ���� ���� � loki �� �������� http://localhost:3000/ �� ���������, �� ����� ������������ ������ ����� ��� loki
    � ����� Dockerfile: http://localhost/loki/api/v1/push

 - ���� ����� ����� ������� ���������, � ���������: docker compose rm -s -v app # ����� ����������� ������ "Y", �����������

 - ��������� ������ ���� ��������, � ���������: docker compose down -v

                                        **************************************
                                                        Sentry

Sentry - https://sentry.io/        # ������ ��� ����� ���� �� �������
Django | Sentry Documentation - https://docs.sentry.io/platforms/python/guides/django/

����� ����� ������������ �������� ������ sentry, �� ��������� ������� ��������� ��������� �� ����� ������������� �� ��������� ����������� ������ ��������� ������������
�� ����� ������� �������� ������

 - �������� �� sentry, ������� ����� ������ python, �������� django-app, �������� "I'll create my own alerts later", ������� ����������� �������� sdk ����������

- ������ � ��������� sentry: pip install --upgrade sentry-sdk � ������� pip freeze > requirements.txt

 - ��������� ��������� �������� � ������� � mysite/mysite/settings.py
    import sentry_sdk

    sentry_sdk.init(
        dsn="https://6dc8a78edfbae6dbc24c78bba9072649@o4505901180715008.ingest.sentry.io/4505901229473792",
        traces_sample_rate=1.0,
    )

============================================================================================================================

                                    *******************************************
                                                ������� ������

                                        ������� ������ XML, JSON, YAML
YAML.org - https://yaml.org/
XML � Wikipedia - https://en.wikipedia.org/wiki/XML
JSON � Wikipedia - https://en.wikipedia.org/wiki/JSON
�������� � REST API � RESTful ���-�������  - https://habr.com/ru/articles/483202/
�������� REST � SOAP / ���� - https://habr.com/ru/articles/483204/

JavaScriptObjectNatation (JSON) - �������� � �������� ������� ������ � ��������� �������� (����� �� �������, �� ����� ������ ������!)

ExtandsibleMarkupLanguish (XML) - �������� � ���������������� ������ � ���� ������ (���� ������������ ����). ������ ����� �� HTM
    (�� ������ ��� �������� � �������� ������, � �� ��� �����������, ��� HTML). � HTML ��� ������� ����, � XML ���� ������� ����
    ������ �������� ��� �������� ������� � ������� �������� ������

SimpleObjectAcessProtocol (SOAP) - ������������ ��� ����� ������� ����� ������/������. ����� ���������� ��������� ������, � ��� ����� ��������
    ������������ ��� ���������� ������ �������� (RPC) � ���������� ������ � ����� (�������� � ���������� ����������). ���� ����
    ������� ��� �������� ������ (envilop). �� ����� ��� ��� �� ������ JSON (�� ����� � �������)

YetAnotherMarkupLanguage - ���� �������� ��� �������� � �������� ������������ ���������� (�� ��� �� ��������� ������������� Docker compose)
    ������ ��� ��������� � ������ ���������. ����� JSON (������ ������ ����������)