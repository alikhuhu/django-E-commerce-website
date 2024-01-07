from django.contrib import admin
from .models import tipe , item , messegis ,brand ,deal,orders,user_pro

# Register your models here.
admin.site.register(tipe)
admin.site.register(item)
admin.site.register(messegis)
admin.site.register(brand)
admin.site.register(deal)
admin.site.register(orders)
admin.site.register(user_pro)