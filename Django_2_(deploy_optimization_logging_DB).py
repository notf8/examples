
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