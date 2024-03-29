
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

                                        ***********************************************
                                                        ������ ������

 - ��� �� �������������� �������� � ������ XML, � ��������� ��������: python manage.py dumpdata --format xml shopapp.Product > shopapp-products-fixtures.xml (��� ����� ������ ���������� ����� xml)

 - �������� ����� ��� �������/�������� ��� django_admin � mysite/shopapp/forms.py
    class CSVImportForm(forms.Form):
        csv_file = forms.FileField()

 - ������� ����� � ������� � mysite/shopapp/templates/admin (��� �� ��������� ��������� �������) � �������� ���� csv_form.html
    {% extends 'admin/base.html' %} # ��������� ������� ��������� ������

    {% block content %}
        <div>
            <form action="." method="post" enctype="multipart/form-data"> # form action="." - ���������, ��� �������� �� ������� ��������
                {% csrf_token %}
                {{ form.as_p }}
                <div class="submit-row">                              # ������ ����� �� ����� ������ ��� � � ����������� ������-�������
                    <input type="submit" value="Upload CSV">
                </div>
            </form>
        </div>
    {% endblock %}

 - ����������� ����� � mysite/shopapp/admin.py
    from django.urls import path
    from django.shortcuts import render
    from .forms import CSVImportForm

    # � ������� ����� ������ � ����� ProductAdmin
    def import_csv(self, request: HttpRequest) -> HttpResponse:
        form = CSVImportForm()
        context = {
            "form": form,
        }
        return render(request, "admin/csv_form.html", context)

    def get_urls(self):
        urls = super().get_urls()      # �������������� ������������ �����, ��� �� ������� ������ ������� + ����� ����� ��� �������
        new_urls = [
            path(
                "import-products-csv/",
                self.import_csv,
                name="import_products_csv"
            )
        ]
        return new_urls + urls   # new_urls ����������� ������ �������!!!! ����� ��������� ������� ����� ��� �� �������� � ������ �������

 - ������� ������ � mysite/shopapp/tempalates/shopapp/products_changelist.html
    {% extends 'admin/change_list.html' %}                                      # ������ ��� ���������� ������ � �������, �� ������� �������

    {% block object-tools-items %}                                              # ��� ���� � �������� � �������
    {% load admin_urls %}                                                       # ��� �� ����� ������������ ��������� ������
        <li>
            <a href="{% url 'admin:import_products_csv' %}" class="addlink">    # class="addlink" ������ ����� ������ ��� � � ���� ���������
                Import CSV
            </a>
        </li>
        {{ block.super }}                                                       # ������������� ������������ ����� � ��������
    {% endblock %}

 - ������� ������ � ����� ProductAdmin (mysite/shopapp/admin.py)
    change_list_template = "shopapp/products_changelist.html"

 - �������� � ����� ������� ���� ��� �������� devices.csv
    name,description,price,discount
    "laptop 14","A new one","29900.00",5
    "laptop 16","A bigger one","49900.00",7

 - ������� ������ � ����� ProductAdmin (mysite/shopapp/admin.py) ����� ��� ������ �����:
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
                Product(**row, created_by_id=1) # ���������, �� � �� ���� ������������ ���� � � ���� CSV ��� ������� ������
                for row in reader
            ]
            Product.objects.bulk_create(products)
            self.message_user(request, "data from CSV was imported")
            return redirect("..")               # �� �������� ��������, �� ���� ������� ���� ��������� � ������, ������ ����� 2 �����, ��� �� ��������� �� ������� ����

                                    ****************************************************
                                                        ����� � DjangoRestFramework

Viewsets � Django REST framework - https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
TextIOWrapper | io � Core tools for working with streams � Python 3.11.3 documentation - https://docs.python.org/3/library/io.html#io.TextIOWrapper


�����! ������ viewset �� ����� �������� ������������� � urls, �� ��� ���� �������� ���� � default routers

 - ������� ����� �������� ��� �������� ������ � ���� �� API. � mysite/shopapp/views.py:
    from csv import DictWriter
    from rest_framework.decorators import action
    from rest_framework.request import Request

    @extend_schema(description="Product views CRUD")
    class ProductViewSet(ModelViewSet):
        """
        ����� ������������� ��� �������� ��� Product.

        ������ CRUD ��� ��������� ������.
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

        @action(methods=["get"], detail=False) # detail=False - ���� � download_csv ������ ���� �������� �� ������ ������ ���������
        def download_csv(self, request: Request):
            response = HttpResponse(content_type="text/csv")
            filename = "products-export.csv"
            response["Content-Disposition"] = f"attachment; filename={filename}"
            queryset = self.filter_queryset(self.get_queryset())      # ��� ������, ��� �� ������� �� filterset_fields (������� ����, ��� �� ����������� � � queryset)
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
                writer.writerow({                  # ���������� ��������� ������ ���� �������� � ���� csv
                    field: getattr(product, field) # �������� �������� ����� �� ����� field
                    for field in fields
                })
            return response

 - ������ ������� ������� ������� csv � django rest, ��� ����� ������� ���� mysite/shopapp/admin.py:
    ������� ��������� ������� (��� ������ � ������� ��� ����� ProductAdmin)
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


        def save_csv_products(file, encoding):                          # ������� ��������� ��� ������. ��������
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

 - ����� � ����� shopapp �������� ����� ���� common.py, ����� ��� �� ���� � copy reference (abolute path)
 - ����� ����� ��� �� ������� save_csv_products() -> refactor -> move -> � � ���� ��������� ��, ��� ����������� ����
    ��� � ����� ���� ����������� �� ������ ������� �� � ��� �� �����������

 - ���� ����� �������� � ����� ���� ������ ������ �������� �� ������� ��� ����� ��� (��� � ��� �� ����� mysite/shopapp/common.py)
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
        for order in instance:                        # ��� ��� ����� �������� ��������, ��������� � ������ ����� ������ ��������� product_pk
            order.products.set(product_pk)

        return instance

 - ������ ����� ������� ������ �� ����� ����� ��� ������� (�� �������), ������� ����� �������� �� modelviewset � mysite/shopapp/views.py
    from rest_framework.parsers import MultiPartParser
    from .common import save_csv_products
    from rest_framework.response import Response

    @extend_schema(description="Product views CRUD")
    class ProductViewSet(ModelViewSet):
        # �� ���� ����� ���������� ���� �����, �� ���� ����
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
            serializer = self.get_serializer(products, many=True) # ��� �� ����� �����������, ������� ��������� ������ (ProductSerializer), ������ ����� ������� ���������� �����
            return Response(serializer.data)

 - ����� � ������� ��������� ����� �������� ����� ��������� ����. ��� ��� ������� �� �������� shop/api/products � extraoptions
�������� upload csv -> �� ���� ��� - �������� ������ � ����� ������ � ���������:
 curl -X POST -F 'file=@devices.csv' http://127.0.0.1:8000/ru/shop/api/products/upload_csv/      # � ���� �� ���������

                                    ************************************************
                                                    ����� ��������

RSS � ��������� - https://ru.wikipedia.org/wiki/RSS
The syndication feed framework | Django documentation - https://docs.djangoproject.com/en/4.2/ref/contrib/syndication/

 - �������� ����� ���������� ��� RSS ����. ��� ����� �������� � ������ blogapp (��������� ������).

 - � ����� mysite/blogapp/views.py:
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
            .filter(pub_date__isnull=False)         # �� ���� ������� � ���������� ������ �������������
            .order_by("-pub_date")                  # ������ ���������� �� ���� ����������
        )

- ������� ���������� �������� � �������. � ����� mysite/blogapp/admin.py:
    from django.contrib import admin
    from .models import Article

    @admin.register(Article)
    class ArticleAdmin(admin.ModelAdmin):
        list_display = "id", "title", "content", "author", "category", "pub_date"

 - �������� ����� RSS � ����� mysite/blogapp/views.py:
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

        def item_title(self, item: Article):                            # ����� ���������� ��������� ������
            return item.title

        def item_description(self, item: Article):                      # ����� ���������� ����������� ����� ������
            return item.content[:200]

        def item_link(self, item: Article):                             # ����� ���������������� �� ������, ������� �����������
            return reverse("blogapp:article", kwargs={"pk": item.pk})

 - ������� ����� ����� � mysite/blogapp/urls.py:
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
        path("articles/latest/feed/", LatestArticlesFeed(), name="articles-feed"),  # �� ��� �� ��� ������� �� � ��������� �� ��� ��������� �������
    ]

 - ��� �� ��������� ������ ���, ����� ������������� ������ �� �������, �������� RSS Feed Reader � ��� � ���� �������� ������
http://127.0.0.1:8000/blog/articles/latest/feed/

                                        ********************************************
                                                        ����� �����
����� ��� ���������� ����� � ��������� �������� ���� Google, Yandex � ��. ����� ����� ��������� ��� ������� ���������� � �������

Site map � Wikipedia - https://en.wikipedia.org/wiki/Site_map
The sitemap framework | Django documentation - https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/

 - �������� ���� � mysite/blogapp/sitemap.py:
    from django.contrib.sitemaps import Sitemap
    from .models import Article

    class BlogSiteMap(Sitemap):
        changefreq = "never"                                       # ��� ����� ����������� �������� (always, hourly, daily, weekly, monthly, yearly)
        priority = 0.5                                             # �� ������� ������� �������� ��������� (�� 0.1 �� 1)

        def items(self):
            return Article.objects.filter(pub_date__isnull=False).order_by("-pub_date")

        def lastmode(self, obj: Article):
            return obj.pub_date

 - ����� ������� ��������� ��� � mysite/blogapp/models.py:
    class Article(models.Model):
        """
        ������ ������������ ������ ��� �����.
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

 - ����� ��������� ��� ������ sitemap (�� �� �� ������ �� ������ ����������) � ������ ������� mysite/mysite/sitemaps.py
    from blogapp.sitemap import BlogSiteMap

    sitemaps = {
        "blog": BlogSiteMap,
    }

 - �������� �������� ����� � �������� url -> mysite/mysite/urls.py:
    from django.contrib.sitemaps.views import sitemap                     # ��� ��� ������� �� django.contrib
    from .sitemaps import sitemaps                                        # � ��� ������ �� ����� sitemaps
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
            name="django.contrib.sitemaps.views.sitemap", # ��� � �������� �� ���� �����, ����� ��� �������, �� ����� ���
        ),
    ]

 - ������ ������� ���������� � ������������� ���������� � mysite/mysite/settings.py:
    INSTALLED_APPS = ['django.contrib.sitemaps',]

 - �����, ����� ������� �� ������ http://127.0.0.1:8000/sitemap.xml � ������� xml ���� � ������ �� �������� �����
========================================================================================================================

                                                    �����������

                                *************************************************
                                                ��� ����� �����������?

��� - ���������������� ������� �������� ������ ���������� ���������. ��� ����� ���������� � ������ �� �����/� ����������� ������/ � ���� �����

���� ����� ����������� � ��� ��� �������� - https://aws.amazon.com/ru/caching/
���� ����� �����������?� - https://azure.microsoft.com/ru-ru/resources/cloud-computing-dictionary/what-is-caching/
����� - https://ru.wikipedia.org/wiki/%D0%9A%D1%8D%D1%88
Redis - https://redis.io/
PostgreSQL - https://www.postgresql.org/
Memcached - https://memcached.org/
MongoDB - https://www.mongodb.com/
                                        *******************************************
                                                ������� ����������� Django

Django�s cache framework - https://docs.djangoproject.com/en/4.2/topics/cache/
Django�s per-site-cache  - https://docs.djangoproject.com/en/4.2/topics/cache/#the-per-site-cache

 - �������� ��������� �� ������ ������ ������� (����� ��� �������� ��� ������� GET � POST ��������. � ����� mysite/mysite/settings.py
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": "C:/foo/bar",                                          # ���� ����� ������� ��� �� �� ����� ����� ��� ����� ������
            # "LOCATION": "E:/temp/django_cache",
                },
            }

    CACHE_MIDDLEWARE_SECONDS = 200                  # ��� ����� ����������� � ��������. �� ��������� ��������� �� 10 �����

 - ������ ��������� ��� � middleware. �����! ��������� � ����� ������ ������! � ��� ��� ����� mysite/mysite/settings.py
    MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware',] # �� ������ �������� ����������� ����� ����� ��� ��������� �������,
                                        # ��� ������ ����������� ��������� (��� �� ������ ������ �� �������� ��������� �������)

 - ��� �� ��������� ����� ��� ������ ����. �����! ��� ������ � ����� ����� ������! � ��� ��� ����� mysite/mysite/settings.py
    MIDDLEWARE = ['django.middleware.cache.FetchFromCacheMiddleware',] # �� ������ �������� ����������� ������ ���� ��� ��������� ��������,
                                        # ��� ��� �� ������ ������ ������, �� ��������� ���������� ��������

 - ������� ����� �������� ��� �������� ������ ������� �����������. � ����� mysite/shopapp/views.py:
    ����� ������ �������� ������ print("shop index context", context) � ������� shopindex ����� "return" � ����������� ��������
    ��� �� ������ ����� �����, ��� ����������� ������ ������, � ������� ����������� �� ����. �� ���� print �� ������������

                                      *******************************************
                                            ����������� ������������� (view)

����������� �������� ���������� �� CACHE_MIDDLEWARE! �������� �� ������ ����������!
Django�s cache framework. The per-view cache - https://docs.djangoproject.com/en/4.2/topics/cache/#the-per-view-cache

 - ������������ ������ ���������� �� �������� (�� def! �� view) � mysite/myauth/views.py:
    from django.views.decorators.cache import cache_page

    @cache_page(60 * 2)                                       # � ������� ��������� �������
    def get_cookie_view(request: HttpRequest) -> HttpResponse:
        value = request.COOKIES.get("fizz", "default value")
        return HttpResponse(f"Cookie value: {value!r} + {random()}")  # � ���� ������ ������� ������ ,��� �� ���������� ������

 - ��� �� �������� ��������� �� view ��������, ��� ����� ���������� � url! � ����� mysite/shopapp/urls.py:
    from django.views.decorators.cache import cache_page

    urlpatterns = [path("", cache_page(60 * 3)(ShopIndexView.as_view()), name="shop_index"),]  # ������ ��������� ����� ������� ShopIndexView

                                         ����������� �� ������� �� view ������� !!!

 - �����!!! � Django Rest, ����������� view ������� ���� ����� default router (� �� ��� ShopIndexView.as_view()), ������� ��������� ���������� ������
    ������� ��� Django Rest ������������ ��������� ��������� "method decorator"
    �������� ��������� ��� ������� ProductViewSet � ����� mysite/shopapp/views.py:

    from django.utils.decorators import method_decorator
    from django.views.decorators.cache import cache_page

    @method_decorator(cache_page(60 * 2))               # � ��������� �������� ��� ���������, ������� ����� �����
    def list(self, *args, **kwargs):                    # ������ �������������� ������������ �����, ��� �� ��������� ����������� �������� ���������
        return super().list(*args, **kwargs)

    ����� �������, ����� �� ��������� ����������� � url, � ������ �������� ��� �� ��������� ������ ������, ��� ������� ����

                                        ********************************************
                                                ����������� ��������� �������

������������, ����� ����� ������������ �� ���� �����, � ������ ����� ��������
Django�s cache framework. Template fragment caching - https://docs.djangoproject.com/en/4.2/topics/cache/#template-fragment-caching

 - ������� ����������� ����� �������� � mysite/shopapp/templates/shopapp/shop-index.html
    {% extends 'shopapp/base.html' %}
    {% load cache %}                    # ������� ��������� ������ ����

    {% block title %}
        Shop index
    {% endblock %}

    {% block body %}
        <h1> ������ ��������� ������� </h1>
        <div>
            <ul>
                {% for link in links %}
                    <li><a href={{link.address}}>{{link.title}}</a></li>
                {% empty %}
                    No links here
                {% endfor %}
            </ul>
        </div>

        {% cache 100 cherr %}             # 100 - ����� � �������� ��� ����. cherr - ��� ���� ��� ���� (�� ����������!!!)
        <div>
            <strong>
                You have {{ items }} cherr{{ items|pluralize:"y,ies" }}
            </strong>
        </div>
        {% endcache %}

        <div>
            Time running: {{time_running}}
        </div>
    {% endblock %}
                                  *****************************************************
                                        ������� �������������� ��� ��� ������������

 - ������� � ������ � mysite/myauth/templates/myauth/about-me.html
    {% extends 'myauth/base.html' %}
    {% load cache %}                                                                    # ������� ��������� ������ ����

    {% block title %}
      About me
    {% endblock %}

    {% block body %}
    <h1>User info</h1>
    <div>
        Products available: {% now "u" %}  # ��� ������ ���������, ������ random ���������� ������� �����, ��� �� �������������� ��������� �����
    </div>
    {% if user.is_authenticated %}
        {% cache 300 userinfo user.username %}        # �����: 300-����� ����, userinfo-���� ��� ����, user.username-���������� ���������� (��� ����) ��� ������� ������������
            <h2>Detail</h2>
            <p>Username: {{user.username}}</p>
            <p>First name: {{user.first_name}}</p>
            <p>Last name: {{user.last_name}}</p>
            <p>Email: {{user.email}}</p>
            <p>Bio: {{user.profile.bio}}</p>
            {% if user.profile.avatar %}
                <img src="{{ user.profile.avatar.url }}" alt="{{ user.profile.avatar.name }}">
            {% else %}
                <h2>No avatar yet</h2>
            {% endif %}
        {% endcache %}
    {% else %}
        <h2>User is anonymous</h2>
    {% endif %}
    {% if request.user.is_staff or user.pk == request.user.id %}
        <div>
            <a href="{% url 'myauth:profile_update' pk=user.profile.pk %}">Update profile</a>
        </div>
    {% endif %}
    <div>
        <a href="{% url 'myauth:profiles_list' %}"
        >Back to profile list</a>
    </div>
    <div>
        <a href="{% url 'myauth:logout'%}">Logout</a>
    </div>
    {% endblock %}

                                    ********************************************************
                                        ������������� ��������������� Cache API � Django

����� ������������ ��� ����, ��� �� ������ ���-������� ��������� � ��� ��������� ������, � �� ���� ��������� ������ �������

Django�s cache framework. The low-level cache API - https://docs.djangoproject.com/en/4.2/topics/cache/#the-low-level-cache-api

����� ������������ � �������:
 - GET (�������� ���� � �������� ���),
 - SET (�������� ������, ����, �������) � ���������� ���
 - ADD (��� �� �������� ������, ����, ������� ) � ������ ���, ��! ADD �� �������������� ��� � ������� �� SET (���� ��� ��� ����)
 - GET OR CREATE (�������� ��� �� �����, � ���� ��� ���, �� ������� ����� ���, �� ���������� �����)
 - DELETE (������� ��� �� ��������� �����)
 - DELETE MANY (������� ��������� ����� �� ������)
 - CLEAR (������ ������ ���� ���)

 - ������������ LowLevelCache � ����� mysite/shopapp/views.py:
    from django.core.cache import cache
    class ProductDataExportView(View, UserPassesTestMixin):
        def test_func(self):
            return self.request.user.is_staff
        def get(self, request: HttpRequest) -> JsonResponse:
            cache_key = "products_data_export"
            products_data = cache.get(cache_key)
            products = Product.objects.order_by("pk").all()
            if products_data is None:
                products_data = [
                    {
                        "pk": product.pk,
                        "name": product.name,
                        "price": product.price,
                        "archived": product.archived,
                    }
                    for product in products
                ]
                cache.set(cache_key, products_data, 3000)
            return JsonResponse({"products": products_data})

                                        *******************************************
                                         ��� ��� �����������!! (����� ��� �������)

 - � ����� ������� � ����� mysite/settings.py �������������� ��� ��������� ���� � ������� ������
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",         # � ���� ������ �������� ����������� �� ����������, � � �������� �� ����� ������ ��������� ���� (������ ��������)
            # "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            # # "LOCATION": "C:/foo/bar",
            # "LOCATION": "E:/temp/django_cache",
        },
    }

                                            ************************************************
                           �������� ��� �������� � ����������� �� ������������, id �������� ������� �� �������� ������

 - ������� � mysite/shopapp/views.py
class UserOrdersListView(LoginRequiredMixin, ListView):
    template_name = "shopapp/user_orders.html"

    def get_queryset(self, owner=None, **kwargs):
        self.owner = get_object_or_404(User, pk=self.kwargs['user_id']) # ��������� ������ ������������ ��� ���������� 404
        return Order.objects.select_related('user').prefetch_related('products').filter(user_id=self.owner)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.owner                   # �������� ������������ � �������� ��� �������
        return context
    # �� �������� ���������� � mysite/shopapp/urls.py [path("users/<int:user_id>/orders/", UserOrdersListView.as_view(), name="user_orders"),]

 - ������ ������ � mysite/shopapp/templates/shopapp/user_orders.html
    {% extends 'shopapp/base.html' %}
    {% load cache %}                         # ���������� ���

    {% block title %}
        Orders list
    {% endblock %}

    {% block body %}
        <h1>The user {{ owner }} made an order(s):</h1>
        {% if object_list %}
        {% cache 300 userinfo owner.pk %}                   # ������� ������� ���� � ���������� ���� ��� ����������� ������������ (��� �� ���� ���� ������)
            <div>
            {% for order in object_list %}
                <div>
                    <p><a href="{% url 'shopapp:order_details' pk=order.pk %}">
                        Details # {{ order.pk }}</a></p>
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
        {% endcache %}
        {% else %}
            <h3>The user has no orders yet</h3>
        {% endif %}

        <div>
            <a href="{% url 'shopapp:order_create' %}">
                Create a new order
            </a>
        </div>
    {% endblock %}

                                *************************************************
                                    ExportView � ������������ � �������������

class OrderCacheExportView(View, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request: HttpRequest, **kwargs) -> JsonResponse:
        user_id = get_object_or_404(User, pk=self.kwargs['user_id'])  # �������� 'user_id' �� �������� ������
        cache_key = f"orders_data_export_for_user_{user_id}"          # ������� �������������� ���� ������������ ��� ����
        orders_data = cache.get(cache_key)                            # �������� ������ �� ����, ���� ��� ��� ����
        if orders_data is None:
            owner: User = get_object_or_404(User, pk=user_id.id)
            orders = Order.objects.select_related("user").prefetch_related("products").order_by('pk').filter(
                user=owner).all()                                    # ��������� ������ �� ������������
            orders_data = OrderSerializer(orders, many=True).data    # ������������ ������ (������������� ������ ������, �� � ����� mysite/shopapp/serializers.py
            cache.set(cache_key, orders_data, timeout=120)           # ��������� ������ � ���
        return JsonResponse({"products": orders_data})

========================================================================================================================

                                    ********************************************
                                        ������������� ����� �� ������� (������)

�������� ����� VPS-��������� � �������� ���������. ����� �������?� - https://oblakoteka.ru/about/v_mire_it/raznica-mezhdu-vpshostingom-i-oblachnym/
VPS - ���������� ����������� �������

 - ��� ������ �������� ����� ������ �� https://gitlab.com/ (create new project � ����� ������� unutialize new repository - ������ ��� � ��� ��� ���� ������� ������)

 - ����� � � ��������� cd Test_area � ������ git init. ����� ����� � ����� ������� �������� .gitignore ��������� ��� ����� �� ������� �� github/gitignore

 - ������ ������ ������ (initial commit: create .gitignore) ���� � ���������������� (������� �������)

 - ����� ��� ��� ���� ������, ����� ������ �������� � ������ - �������� ����� directory � ������ ��� ����� ������ ������ (add all files)

 - ����� ������������ �� ���� � �������� ������� (������ ����� ��� ����� �����): git remote add origin git@gitlab.com:notf8/django-app.git

 - ���������� ��������� � �����������, �������� ������� �� �����: git push --set-upstream origin main (� ���� �� ���������, ������ src ������� ����� �������������)

 - � ��� ����� ���� ����������� �������� �� ������� (�����������) � docker compose ��������� � ���������� ������������ � ��������� ����������

 - ���� ��� ������� �������� �� Django ������������ ���� �������: WSGI. �������� GUNICORN (��� ��������� ���������) ��� UWSGI (��� ����������� ����������)

 - ��� ������ �������� gunicorn. �������� ��� � ���������: pip install gunicorn � ��������� pip freeze > requirements.txt


                                ***********************************************************
                                        ���������� Python ������� � �������������

������� ������������������ WSGI-�������� - https://habr.com/ru/articles/428047/
Ways to set environment variables in Compose. Docker Documentation - https://docs.docker.com/compose/environment-variables/set-environment-variables/
Start containers automatically. Docker Documentation - https://docs.docker.com/config/containers/start-containers-automatically/
Logging. Django documentation - https://docs.djangoproject.com/en/4.2/topics/logging/
What is .env? How to Set up and run a .env file in Node? Codementor - https://www.codementor.io/@parthibakumarmurugesan/what-is-env-how-to-set-up-and-run-a-env-file-in-node-1pnyxw9yxj
OpenSSL rand - https://www.openssl.org/docs/man1.1.1/man1/rand.html

- ����� � ����� ����� ��������������� Dockerfile . �� ������� ��� ������� �� gunicorn ����������:
    FROM python:3.11

    ENV PYTHONUNBUFFERED=1

    WORKDIR /app

    COPY requirements.txt requirements.txt

    RUN pip install --upgrade pip
    RUN pip install -r requirements.txt

    COPY mysite .

    CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]

 - ����� ����� ����� ������� ����� ���� ��� ���� ������ �� ������� (�� ��������� ����� ��� ���), � ����� mysite/mysite/settings.py, ������, ��� BASE_DIR
    DATABASE_DER = BASE_DIR/"database" # ����� ��������, ��� �� �� ��������� �� ������� � ��� ���������� ���������� �� ����������������
    DATABASE_DER.mkdir(exist_ok=True) # ���� ����� ��� ����������, �� ������ �� �������

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DATABASE_DIR / 'db.sqlite3',    # ��� �� ����� �������� ������������ �� � ���������� ��
        }
    }

- ������ ������� ��������� ������������ �� ���������� ����� �� �������. ��� �� � mysite/mysite/settings.py:
    from os import getenv
    import logging.config

    SECRET_KEY = getenv(                                                     # ���� ����������� �������� ����� getenv()
        "DJANGO_SECRET_KEY",
        'django-insecure-*kzcgnp=a(yak7daj@y-@g9h0+9@c*g-q1*m%^&)$3p*ogittr'
    )
    DEBUG = getenv("DJANGO_DEBUG", "0") == "1"    # ��� ������ ����������� �������� �������� ������ �� ��������� (���� �������� debug=True �� ������, �� ���������� ������� ������)

    ALLOWED_HOSTS = [
        "0.0.0.0",
        "127.0.0.1",
    ] + getenv("DJANGO_ALLOWED_HOSTS", "").split(",") # ��� �� ����������� ������ ������ �� ���������

    LOGLEVEL = getenv("DJANGO_LOGLEVEL", "info").upper()
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(message)s"
            },
        },
        "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "console",
                },
            },
        "loggers": {
            "": {
                "level": LOGLEVEL,
                "handlers": [
                    "console",
                ],
            },
        },
    })

 - ������ ������������� ���� docker-compose.yaml (������ ����� � ����� �������, ���� ��������� ������) ���� ������� ���
    version: "3.9"

    services:
      app:
        build:
          dockerfile: ./Dockerfile
        command:
          - gunicorn
          - mysite.wsgi:application
          - --bind
          - "0.0.0.0:8080"

        ports:
          - "8000:8080"
        restart: always
        env_file:
          - .env
        logging:
          driver: "json-file"
          options:
            max-file: "10"
            max-size: "200k"
        volumes:
          - ./mysite/database:/app/database

 - ����� �������� � ����� ��������� ������:  .env � .env.template
    ���� .env.template (��� ���, ������� ������� �� ������):
        DJANGO_LOGLEVEL=
        DJANGO_SECRET_KEY=
        DJANGO_DEBUG=
        DJANGO_ALLOWED_HOSTS=

    ���� .env (���� ��������� � ��� �� ��������� �����, �� ���� ����� �������� ���� .env.template)
        DJANGO_LOGLEVEL=INFO
        DJANGO_SECRET_KEY=sdaoihasijhfijahisjufajikanfj #��� ��� ������ �� ����� �� ����� �������� (���� ���-�� �������� �� �����)
        DJANGO_DEBUG=1
        DJANGO_ALLOWED_HOSTS=

 - �� � �������� ���������. � ���������: docker compose build app � docker compose up app (���������, ��� � ��� ��������)
========================================================================================================================
                                            ************************************************
                                                �������� SSH-������ � �������

��� ��������� ������� � ������� ����� ��������� ������� ���������: �������� ��������� ���� �� �������� ������ � ������ �����������.
���� �� ������������ ����������� ������ ����� �������-���������, � ���-���������� ������ ���� ����������� ����� � ����������
��� ������� ���������� SSH-�����.

��������� � Timeweb
���� �� ������������ ����������� ������ � Timeweb, ��� �������� ����� ����������� ������ � ������� ������������� ������� ���������� ����� �����:
� ����������� ���� ����� ���� ��� ����� ����� � ��������� ���� ��� ��������. �������� ��� ��������� ���� � ���� ������,
� ��� �������� ������� � ���� ��������� �����:

������� ����������, ����� ��������� ���� � ����� ������ �������� � �������� ��� � ����������� ������.
����� �������� ����������� ������ � � ��������� ������� ��������� �������� ������ �� SSH. ��� ������ ����� ���������,
��� ���������� ����� ���� �����������. � ���������� ����������� ������ ��������� �� ������� ������. ������� IPv4-�����
(�� �������� ����, ������� �������) � ������ IP-�������. ���������� IP-�����.

��������� ����������� ����� ������� SSH-������ (� ��������� ��� ����� ���������� � ����������� �����������).
������������ � ������ root �������� �� ���������, ������� ������� �������� ���: ssh root@46.19.67.97

root � ��� ��� ������������, � 46.19.67.97 � ��� IP-����� �������.

��� ������ ����������� �� ������� ������: Are you sure you want to continue connecting (yes/no/[fingerprint])? # ����������� yes � ������� Enter.

 - �������� �������� root-������, ��� ����� ����������� �� �������� ������ �������, �� ������� "������"

  - ���������� � ��������� ������� (����� ������� ����) �������� � ��������� �����������: git clone https://github.com/notf8/Django_app.git (����� �������� �� ����� �������)


 - ����� ������� � ����� ���������. ������� �� ������ � �������� ����� (Clone with SSH)

 - ������������ � ���������� �������. ����� � ��������� ssh ��� ������������ � ����� ������� (��� �������: ssh root@46.19.67.97)

 - ��� �� �������, � ��������� ��������� � ���� ����� � ��������� (������� "CD") � �����:
    git clone git@gitlab.com:notf8/django-app.git # ��, ��� ����������� �� ����

 - ��������� ������ ������ ��������: ls -a

 - ����� �� ������� ��������� � �������������� ������ , �������� ���� .env.template � ��������� ��� �� �������
    � ���������: cp .env.template .env

- ��� �� ������������� �������� secret key, � ��������� ������: openssl rand -hex 32 # ��� �� ������� ��������� ������. �� �������� � ���������

 - ���������� ������������� ���� � ������������ ���������. � �������� ������: nano .env # � ��� ��������� ��������� � ����� .env
    DJANGO_LOGLEVEL=INFO
    DJANGO_SECRET_KEY=������ ��������� �������� (����� �������� ������ ����, ������� �� ������ ���)
    DJANGO_DEBUG=1
    DJANGO_ALLOWED_HOSTS=46.19.67.97  # ������ IP ����� ������� (������� ��� ��� ��������� �������), ����� ������� ����� ������� ������� ���

    ����� ��������� ����: CTRL+O � ENTER. ��� �� ����� �� ���������: CTRL+X

 - ������������� �� ������� docker compose ��������: sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 - ��������� ������ ������: docker-compose -v
 - ������ ������� �����������: sudo chmod +x /usr/local/bin/docker-compose
 - ��������� ���������� ���������: docker-compose --version

 - �������� ���������: docker-compose build app
 - ����� ����� ��������� ���������. � ���������: docker-compose up -d app
 - ��������� ������ ������ � ����������: ls -la mysite/database/ # (��� ���������� ������ �� �����)
 - ��� �� ��������� �� � ������ ������ ��������. � ��������� ������: docker-compose exec app python manage.py migrate
 - �� ���� ������, �������� ����������: docker-compose exec app python3 manage.py createsuperuser

                                **************************************************
                                    ���������� �������. ���������� � SSH

 - � ����������� ������� �� Linux (��������, Ubuntu, Linux Mint) ����������� ��� ������ � SSH ��� �����������. ���� �� ���, ���������� ����� ��������� �������:
    apt update
    apt upgrade -y
    apt install -y openssh-client
 ��� ��� ������ ����� �������:
    apt update && apt upgrade -y && apt install -y openssh-client

 - �� macOS ������ SSH �������� �� ���������. ����� �� ������ ��������������� ���������� ��������� � ����������� �����������, �������� termuis.

 - Windows - ��� ������ � SSH �� Windows ����� ������������ ���������� SSH-������ ��� ���������� ��������� ����������,
   ����� ������� ����� ��������� �������������. ����� �� Windows ���� � ����� ������, �� ���� ���������� ��������� ���
   ������ � SSH: PuTTY � ��� ���� (�����������) � ����������� KiTTY. ��� �� ������� �����������.

 - ������ ������ � ���������. ��������� � �������� � ��������� �������: ssh-keygen -b 2048 -t rsa

 - � ��������� �� ������� ������ � ���, ���� ��������� ����� ����. �� ����� ������, ������� Enter (��� Return �� Mac), ����� ����������:

 - ����� ��� �������, ����� ������� ����� ���������� ������������. ����� �������� ������� ����� ������. � ���� ������ ������ ������� Enter (��� Return �� Mac)

 - ����� ������: �������� ��������, ��� ��� ����� ������� � ���������, � ��� ����� ������� ����, �� ������ ������ ������ ����.

 - ���������� ���� ��������� ����. � ���������: head ��� cat: head ~/.ssh/id_rsa.pub.
    � �������� ����� �������� ������� ������� � ��� � ���� ��������� ����. ���������� � ��������� ��� ���������� ������, ���� ���������� � ����������.

                                            *********************************************
                                                    ������ �� SSH � GitHub

��������� �� GitHub. ���������, ��� �� ���������������� � ��������� ����. �������� �� ������ ������� � ������ ������� ����.
� ���������� ������ �������� Settings (����������):
    1) ����� � ������ � ������ Access (���������) �� ������� ������� SSH and GPG keys. �������� �� ���.
    2) ������� �� New SSH key ��� Add SSH key ������ ������.
    3) � ���� Key �������� ����, ������� ����������� �����.
    4) ��������������/��������� ���� Title.
    5) �������� Add SSH key, ����� ��������� ���������.
    6) ���� �������� ���� ��� ������������� ������� (��������, ���� ������), ����������� ���������.
    ����� ��������� ������ � ���������, ��� ��������� �����, ��������� � ��������� (��� �� ����������� �������� � SSH) ������� ssh -T git@github.com.

 - ��� ������ ����������� ������� ����� ��������, ������� �� ��, ��� ������ ������������ � ����� ������. �������� yes � ������� Enter, ����� �����������.

                                        *********************************************
                                                    ������ �� SSH � GitLab

1) ������� � GitLab.
2) �� ������� ������ � ������ ������� ���� �������� �� ���� ������.
3) ������� Edit profile (�������������� ��������).
4) �� ����� ������� ������ �������� SSH Keys (������ SSH�).
5) � ���� Key �������� ��������� ����, ������� ����������� �����.
6) ��������������/��������� ���� Title.
7) ������� Add key (��������� �����).
����� ��������� ������ � ���������, ��� �� �� ����� ���������, ��������� � ��������� (��� �� ����������� �������� � SSH)
������� ssh -T git@gitlab.com.
�������� yes � ������� Enter, ����� �����������.


========================================================================================================================

                                    ******************************************************
                                    ������������� ���� � �������� ��� ��������� ����������

Git merge conflicts. Atlassian Git Tutorial - https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts
Django Migrations and How to Manage Conflicts - https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/
����������� �������� �������� ������������� - https://habr.com/ru/articles/534238/

 - ����� ����� ������������ ��������� ����� ��� ������ ����� ����
 - �� ������ � ������ ����� ����� ���. ����� ������� ����� ���� �������
 - ���� ����� �� ��������� ���� ����� � ��������, ����� ���� ������ ������
 - ��� �� ������� ��������� �������� - ��� ����� ��������� ������ ������ ��������� ������� (�� ������ � �� �������)
 - ����� ����������� �������� �� ��������� ������ ����� �������� �����
 - � API �� ������������� ������/������� ���� � �� ��� (���� ���� �������� � �������)

                                    ******************************************************
                                                    �������� ������������

Pipenv - https://pipenv.pypa.io/en/latest/
Poetry - https://python-poetry.org/
Integrating Python Poetry with Docker - https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
Document docker poetry bestpractices - https://github.com/orgs/python-poetry/discussions/1879
������ ��� ������������ ������������: �� DEV �� PROD� - https://habr.com/ru/companies/rtlabs/articles/577580/

 - Pipenv � Poetry ���������� ��� ������� Pipenv. Poetry ����� ����� � ����� ������������. ��� ������� ����� � ���

 - ��������� Poetry (����� ������� ��� � �������� ��� � � ���������, �� �������������). � ���������: pip install poetry

 - ����� �������: poetry init
    ����� ��� ����� ��� ��������, ��� ��������� �� ��������� (����� �������, ������ ������, ��������)
    �� ������ ��� ��������� ������� � ��������� ������ no � no
    ��������� ������ ��� ������� ��������� �������� yes

 - ����� � ��� �������� � ����� ���� pyproject.toml, ��� ��������� � ���
    �� � ��� ��� ����� readme, ������ � ��� ������� ������ �� ������� pakages (���� ��� ����)

- ��������� rest_framework. � ���������: poetry add django django-rest-framework
    �������� ���� poetry.lock ��� ������ �������������� � ������!!! ��� ���� ��������� � ���

 - ������� ������� ��, ��� ������������ � ������� (�� ����� rquirements ������ �������� ����, ��� ������)
    poetry add

 - ����� �������� ����: docker compose build app � ���������� ������: docker compose up app

 - � ����� ������� ����������, � �������� ������: poetry install

 - �����, ���� ���������� �� ��������� �� �� ������ ������ ���������, �� ����� � poetry ���� ��������, ����� ������ �����:
     - ��� �������: poetry add "pillow@9.5.0"

 - ����� �������� poetry � dockerfile
    FROM python:3.11

    ENV PYTHONUNBUFFERED=1

    WORKDIR /app

    RUN pip install --upgrade pip "poetry==1.6.1"
    RUN poetry config virtualenvs.create false --local
    COPY pyproject.toml poetry.lock ./
    RUN poetry install

    COPY mysite .

    CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]

 - ��� �� ��������� ������ ������ � ���������: poetry --version
========================================================================================================================
����� ���� ���������: 94.241.141.104:8000/shop/

========================================================================================================================

                                        *************************************
                                                    ���� Django
1) ����� ������ �������������� ���������� ��������� Django? - MVC
2) ���������� ������� ������ shop. ����� �������� ��������������? - django-admin startproject shop
3) ������ ������� ����� ������� ����������������� ����������. ����� �������� ��������������? - django-admin startapp accounts
2) ������ �������� � ����� ������ ���������� ������ (request). ����� ������ ������ ������ ��� ���������? - urls.py
3) ��� ���������� Goods ��� ����� ������ ����� �������� ������ � ������. � ����� ������ ����� ������� ��� ������? - settings.py
4) ��� ����� �������� �������, ������� ����� ���������� ������ ���, ����� ��������� ����������. ����� ���������� �� ��������������? - middleware
5) ����� ������� ���������� �������� ������ � �������� ����������� �������? - render
6) ��� ����� �������� ������������� ��� �������� ������ ���������� ������. ������ CBV �� ��������������? - CreateView (�������� ��� View)
7) ��� ���� ��� ������ ��������� ����� �������������� �����, ��� �����������, JavaScript ��� CSS. ��� ��� ����� ���������� � Django? - ����������� �����
8) � ��� ���� ������� ������. ����� ������� �� ������ ��� ������������ � ������ ��������? - {% extends "base.html" %}
9) �� ������� ������. � ������� ����� ������ ����� �������� �������� � ���������� ��? python manage.py � makemigrations, migrate
10) ����� ����� ���������� ���������� ������ � ��?: Shop.objects.all()[2], len(Shop.objects.all())
11) ��������� ����� ���������� �������� ������� ����� ������ � ��? - django-debug-toolbar
12 ) ������� ������� ������� ������. - loaddata
13) ��� ���������� �������� ��� �������� ������� Django � ������ �������? - ������������
14) ��������� ������ ���������� ��� ������������ openapi-������������ ��� �������������� API. - drf-yasg
15) ��� ������� �����������������? python manage.py � createsuperuser
16) ��� ����� � �������� Django? python manage.py � shell
17) ��� ����� ������� ��������� � ������� ��� �������� ������ �������. ������ ������������ �� ��������������: logging.info(), logging.debug(), logging.error(), Print()
