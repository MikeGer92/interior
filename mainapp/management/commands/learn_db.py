from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.db import connection
from django.db.models import Q
from adminapp.views import db_profile_by_type

class Command(BaseCommand):
   def handle(self, *args, **options):
       products_list = Product.objects.filter(
           Q(category__name='дом') | Q(category__name='офис')
       )
       category_list = ProductCategory.objects.filter(
           Q(id=2) | Q(id=5)
       )

       print(len(products_list))
       print(products_list)
       print(category_list)
       db_profile_by_type('learn db', '', connection.queries)

