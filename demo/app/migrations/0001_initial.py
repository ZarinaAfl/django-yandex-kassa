# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import yandex_kassa.utils
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_kassa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Наименование')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.CharField(primary_key=True, max_length=64, serialize=False, verbose_name='ID заказа', default=yandex_kassa.utils.get_uuid)),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Кол-во')),
                ('amount', models.PositiveIntegerField(verbose_name='Сумма заказа')),
                ('item', models.ForeignKey(to='app.Item', null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Товар')),
                ('payment', models.ForeignKey(to='yandex_kassa.Payment', null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Платеж')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
    ]
