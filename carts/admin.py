from django.contrib import admin
from .models import Carts,CartItems
from order.models import OrderProduct
# Register your models here.


class CartsAdmin(admin.ModelAdmin):
    list_display = ["cart_id","user","date_add"]

admin.site.register(Carts,CartsAdmin)
admin.site.register(CartItems)