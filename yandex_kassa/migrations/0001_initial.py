# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import yandex_kassa.utils
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('customer_number', models.CharField(unique=True, max_length=64, default=yandex_kassa.utils.get_uuid, verbose_name='Номер заказа')),
                ('status', models.CharField(choices=[('processed', 'Processed'), ('hold', 'Hold'), ('cancel', 'Cancel'), ('success', 'Success'), ('fail', 'Fail')], max_length=16, default='processed', verbose_name='Результата')),
                ('scid', models.PositiveIntegerField(default=123, verbose_name='Номер витрины')),
                ('shop_id', models.PositiveIntegerField(default=123, verbose_name='ID магазина')),
                ('payment_type', models.CharField(choices=[('AB', 'Альфа-Клик'), ('AC', 'Банковская карта'), ('GP', 'Наличные через терминал'), ('MA', 'MasterPass'), ('MC', 'Мобильная коммерция'), ('PB', 'Интернет-банк Промсвязьбанка'), ('PC', 'Кошелек Яндекс.Денег'), ('SB', 'Сбербанк Онлайн'), ('WM', 'Кошелек WebMoney'), ('QW', 'QiWi кошелёк')], max_length=2, default='PC', verbose_name='Способ платежа')),
                ('invoice_id', models.CharField(null=True, max_length=64, blank=True, verbose_name='Номер транзакции оператора')),
                ('order_amount', models.FloatField(verbose_name='Сумма заказа')),
                ('shop_amount', models.DecimalField(decimal_places=2, null=True, max_digits=15, blank=True, help_text='За вычетом коммиссии', verbose_name='Сумма полученная на р/с')),
                ('order_currency', models.PositiveIntegerField(choices=[(643, 'Рубли'), (10643, 'Тестовая валюта')], default=643, verbose_name='Валюта платежа')),
                ('shop_currency', models.PositiveIntegerField(null=True, choices=[(643, 'Рубли'), (10643, 'Тестовая валюта')], blank=True, verbose_name='Валюта полученная на р/с', default=643)),
                ('payer_code', models.CharField(null=True, max_length=33, blank=True, verbose_name='Номер виртуального счета')),
                ('success_url', models.URLField(default='/kassa/success/', verbose_name='URL успешной оплаты')),
                ('fail_url', models.URLField(default='/kassa/fail/', verbose_name='URL неуспешной оплаты')),
                ('cps_email', models.EmailField(null=True, max_length=254, blank=True, verbose_name='Почта плательщика')),
                ('cps_phone', models.CharField(null=True, max_length=15, blank=True, verbose_name='Телефон плательщика')),
                ('created', models.DateTimeField(verbose_name='Создан', auto_now_add=True)),
                ('performed_datetime', models.DateTimeField(null=True, blank=True, verbose_name='Обработан')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='Пользователь')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'Платежи',
                'verbose_name': 'платеж',
            },
        ),
    ]
