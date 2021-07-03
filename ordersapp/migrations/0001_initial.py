# Generated by Django 3.2 on 2021-06-28 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0003_product_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('FM', 'Формируется'), ('STP', 'Отпралено в обработку'), ('PSD', 'Обработано'), ('PD', 'Оплачено'), ('RD', 'Готов к выдаче'), ('CNC', 'Отменен'), ('DVD', 'Выдан')], default='FM', max_length=3, verbose_name='статус заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='количество товара')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='ordersapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='продукт')),
            ],
        ),
    ]
