from django.contrib import admin
from .models import CustomUser,Products

class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products,ProductsAdmin)

