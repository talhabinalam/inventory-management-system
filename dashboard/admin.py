from django.contrib import admin
from .models import *

admin.site.site_header = 'Inventory Admin'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    list_filter = ['category']
    ordering = ['id']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
