from datetime import datetime

from django.db import models

# Create your models here.


class Channel(models.Model):
    name = models.CharField("Название канала", max_length=20)
    photo = models.CharField("Ссылка на фотографию канала", max_length=200)
    active = models.BooleanField("Статус канала", default=True)
    order_num = models.IntegerField("Приоритет канала")


statuses = (
    ('NEW', 'new'),
    ('PAID', 'paid'),
    ('CLOSED', 'closed')
)

class Order(models.Model):
    text = models.TextField("Текст заказа")
    client_name = models.CharField("Имя клиента", max_length=100)
    client_phone = models.CharField(max_length=10)
    client_email = models.EmailField()
    total_price = models.FloatField("Total price of order")
    add_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
    status = models.CharField("Order status", choices=statuses)


class OrderDetail(models.Model):
    channels = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    orders = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    price = models.FloatField("Цена выбранного канала с учетом количества дней в определенном заказе")


class Day(models.Model):
    day = models.DateField(format="%d-%m-%Y")
    order_details = models.ForeignKey(OrderDetail, on_delete=models.DO_NOTHING)


class Discount(models.Model):
    channels = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    percent = models.IntegerField("Discount percentage")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=datetime(2999, 12, 31))
    min_days = models.IntegerField("Количество минимальных дней")


class Price(models.Model):
    channels = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=datetime(2999, 12, 31))
    price = models.FloatField("Цена одного символа на определенном канале")

