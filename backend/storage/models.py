import uuid
from django.db import models
from django.contrib.auth.models import User
import qrcode
from datetime import datetime
import datetime, calendar
from django.db.models.signals import post_save, post_delete, pre_save


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


class Stock(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование',default='')
    address = models.CharField(max_length=400, verbose_name='Адрес склада')
    property = models.CharField(max_length=400, verbose_name='Характеристика, свойства склада')
    capacity = models.PositiveBigIntegerField(null=True, default=0)

    def __str__(self):
        return f'{self.address} - {self.property} - {self.capacity}'

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

class BoxX(models.Model):
    """
        по номеру бокса - можно потом QR сделать...
    """
    # picture = models.ImageField(blank=True, verbose_name='Изображение')
    box_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Номер бокса')
    capacity = models.PositiveBigIntegerField(null=True, default=0)
    boxx = models.ForeignKey(Stock, related_name='stock_box', verbose_name='Склад', blank=True,  on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    rented = models.BooleanField(default=False, verbose_name='Задействован')
    box_qr_code = models.ImageField(upload_to='images_qr', blank=True, null=True)
    price = models.FloatField(verbose_name='Цена аренды', default=0)

    # def save(self, *args, **kwargs):
    #     img = qrcode.make(self.box_number)
    #     box_qr_code = img.save(f"images_qr/{self.box_number}.png")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'№{self.box_number} дата создания {self.create_date}'

    class Meta:
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boxx = models.ForeignKey(BoxX, related_name='user_box', verbose_name='ячейка', blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=400, verbose_name='Адрес клиента')

    def __str__(self):
        return f'{self.user} {self.address}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Lead(models.Model):
    address = models.CharField(max_length=400, verbose_name='Адрес')
    eMail = models.CharField(max_length=100, verbose_name='Почта')
    delivery = models.BooleanField(default=False, verbose_name='Доставка')

