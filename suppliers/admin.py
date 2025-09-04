from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name']
