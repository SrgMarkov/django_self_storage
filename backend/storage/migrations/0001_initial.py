# Generated by Django 4.2.7 on 2023-11-19 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxX',
            fields=[
                ('box_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Номер бокса')),
                ('capacity', models.PositiveBigIntegerField(default=0, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('rented', models.BooleanField(default=False, verbose_name='Задействован')),
                ('box_qr_code', models.ImageField(blank=True, null=True, upload_to='images_qr')),
                ('price', models.FloatField(default=0, verbose_name='Цена аренды')),
            ],
            options={
                'verbose_name': 'Бокс',
                'verbose_name_plural': 'Боксы',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400, verbose_name='Адрес')),
                ('eMail', models.EmailField(blank=True, default='', max_length=150, null=True, verbose_name='Почта')),
                ('delivery', models.BooleanField(default=False, verbose_name='Доставка')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование')),
                ('address', models.CharField(max_length=400, verbose_name='Адрес склада')),
                ('property', models.CharField(max_length=400, verbose_name='Характеристика, свойства склада')),
                ('capacity', models.PositiveBigIntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400, verbose_name='Адрес клиента')),
                ('boxx', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_box', to='storage.boxx', verbose_name='ячейка')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.AddField(
            model_name='boxx',
            name='boxx',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_box', to='storage.stock', verbose_name='Склад'),
        ),
    ]