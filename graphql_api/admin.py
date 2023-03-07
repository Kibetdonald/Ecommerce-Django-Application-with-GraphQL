from django.contrib import admin
from .models import Product


class ProductDetails(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'available')
    search_fields = ['name', 'description']

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


admin.site.register(Product, ProductDetails)
