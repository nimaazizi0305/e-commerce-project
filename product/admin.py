from django.contrib import admin
from .models import Product,Variation,Review,ProductGallery
import admin_thumbnails

# Register your models here.

@admin_thumbnails.thumbnail("image_produtc")
class ProductAdminGallery(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","is_active","category","created_date","published_date"]
    readonly_fields = ["created_date","published_date"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    prepopulated_fields = {"slug":("name",)}
    inlines = [ProductAdminGallery]

class VariationAdmin(admin.ModelAdmin):
    list_display = ["product","variation_category","variation_value","is_active"]
    list_editable = ("is_active",)
    search_fields = ["variation_value"]
    list_filter = ["product","variation_value"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(Review)
admin.site.register(ProductGallery)