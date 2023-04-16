from django.contrib import admin
from .models import Order,OrderProduct,Pyament

# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    fields = ["user","order","product","varation","product_price"]
    readonly_fields = ["user","order","varation","product","product_price"]



class OrderProductAdmin(admin.ModelAdmin):
    list_display = ["user", "order", "product", "product_price"]
    list_filter = ["user", "product"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","first_name","last_name","email","created_at","status"]
    search_fields = ["user","first_name","last_name"]
    list_filter = ["status","is_oredered"]
    list_per_page = 10
    inlines = [OrderProductInline]


admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Pyament)
