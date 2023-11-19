import os
import pathlib
import uuid
from calendar import calendar
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
import qrcode
from django.core.files.uploadedfile import UploadedFile
from django.db.models import EmailField
from django.db.models.signals import pre_save, post_save
from self_storage.settings import BASE_DIR

IMAGE_QRCODE_DIR = 'images_qr'


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


class Stock(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Наименование', default=''
    )
    address = models.CharField(max_length=400, verbose_name='Адрес склада')
    property = models.CharField(
        max_length=400, verbose_name='Характеристика, свойства склада'
    )
    capacity = models.PositiveBigIntegerField(null=True, default=0)
    slug = models.SlugField(max_length=200, blank=True)
    photo_path = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return (
            f'{self.name} {self.address} [{self.property} - {self.capacity}]'
        )

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class BoxX(models.Model):
    box_number = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Номер бокса',
    )
    capacity = models.PositiveBigIntegerField(null=True, default=0)
    stock = models.ForeignKey(
        Stock,
        related_name='boxes',
        verbose_name='Склад',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    end_date = models.DateTimeField(blank=True, null=True)
    rented = models.BooleanField(default=False, verbose_name='Задействован')
    box_qr_code = models.ImageField(
        upload_to=IMAGE_QRCODE_DIR, blank=True, null=True
    )
    price = models.FloatField(verbose_name='Цена аренды', default=0)

    def save(self, *args, **kwargs):
        pathlib.Path(os.path.join(BASE_DIR, IMAGE_QRCODE_DIR)).mkdir(
            parents=True, exist_ok=True
        )
        img = qrcode.make(self.box_number)
        path_image_file = os.path.join(
            BASE_DIR, IMAGE_QRCODE_DIR, f'{self.box_number}.png'
        )
        img.save(path_image_file)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'№{self.box_number} дата создания {self.create_date}'

    class Meta:
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'


def boxx_pre_save_receiver(sender, instance, *args, **kwargs):
    path_image_file = os.path.join(
        BASE_DIR, IMAGE_QRCODE_DIR, f'{instance.box_number}.png'
    )
    instance.box_qr_code = UploadedFile(file=open(path_image_file, 'rb'))


pre_save.connect(boxx_pre_save_receiver, sender=BoxX)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boxx = models.ForeignKey(
        BoxX,
        related_name='user_box',
        verbose_name='ячейка',
        blank=True,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=400, verbose_name='Адрес клиента')

    def __str__(self):
        return f'{self.user} {self.address}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Lead(models.Model):
    address = models.CharField(max_length=400, verbose_name='Адрес')
    eMail = models.EmailField(
        max_length=150, default='', null=True, blank=True, verbose_name='Почта'
    )
    delivery = models.BooleanField(default=False, verbose_name='Доставка')
