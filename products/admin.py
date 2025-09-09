from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'category', 'serie_number', 'cost_price', 'selling_price', 'quantity', 'description']
    search_fields = ['title', 'brand', 'category']
