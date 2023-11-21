# Generated by Django 4.2.7 on 2023-11-19 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_stock_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxx',
            name='boxx',
        ),
        migrations.AddField(
            model_name='boxx',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boxes', to='storage.stock', verbose_name='Склад'),
        ),
    ]