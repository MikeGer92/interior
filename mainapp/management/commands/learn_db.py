from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.db import connection
from django.db.models import Q
from adminapp.views import db_profile_by_type
from django.db.models import F, When, Case, DecimalField, IntegerField
from datetime import timedelta

from ordersapp.models import OrderItem


class Command(BaseCommand):
   def handle(self, *args, **options):
   #     products_list = Product.objects.filter(
   #         Q(category__name='дом') | Q(category__name='офис')
   #     )
   #     category_list = ProductCategory.objects.filter(
   #         Q(id=2) | Q(id=5)
   #     )
   #     db_profile_by_type('learn db', '', connection.queries)
       ACTION_1 = 1
       ACTION_2 = 2
       ACTION_3 = 3

       action_1__time_delta = timedelta(hours=12)
       action_2__time_delta = timedelta(days=1)

       action_1__discount = 0.3
       action_2__discount = 0.15
       action_3__discount = 0.05

       action_1__condition = Q(order__update__lte=F('order__created') + action_1__time_delta)

       action_2__condition = Q(order__update__gt=F('order__created') + action_1__time_delta) & \
                             Q(order__update__lte=F('order__created') + action_2__time_delta)

       action_3__condition = Q(order__update__gt=F('order__created') + action_2__time_delta)

       action_1__order = When(action_1__condition, then=ACTION_1)
       action_2__order = When(action_2__condition, then=ACTION_2)
       action_3__order = When(action_3__condition, then=ACTION_3)

       action_1__price = When(action_1__condition, then=F('product__price') * F('quantity') * action_1__discount)

       action_2__price = When(action_2__condition, then=F('product__price') * F('quantity') * action_2__discount)

       action_3__price = When(action_3__condition,then=F('product__price') * F('quantity') * action_3__discount)

       orders_items = OrderItem.objects.annotate(
           action_order=Case(
               action_1__order,
               action_2__order,
               action_3__order,
               output_field=IntegerField(),
           )).annotate(
           total_price=Case(
               action_1__price,
               action_2__price,
               action_3__price,
               output_field=DecimalField(),
           )).order_by('action_order', 'total_price').select_related()

       for item in orders_items:
           print(f'{item.action_order:2}: заказ №{item.pk:3}:\
                  {item.product.name:20}: скидка\
                  {abs(item.total_price):6.2f} руб. | \
                  {item.order.update - item.order.created}')

