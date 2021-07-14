from django.contrib import admin
from .models import Channel, Order, OrderDetail, Discount, Day, Price
# Register your models here.


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'active', 'order_num']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['text', 'client_name', 'client_phone', 'client_email', 'total_price', 'add_date', 'edit_date', 'status']

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['channels', 'orders', 'price']

class DayAdmin(admin.ModelAdmin):
    list_display = ['day', 'order_details']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['channels', 'percent', 'start_date', 'end_date', 'min_days']

class PriceAdmin(admin.ModelAdmin):
    list_display = ['channels', 'start_date', 'end_date', 'price']

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Price, PriceAdmin)
