from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'created')
