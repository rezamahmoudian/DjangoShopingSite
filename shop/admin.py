from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price', 'available', 'updated')
    list_filter = ('available', 'updated', 'created')
    list_editable = ('price', 'editable')
    prepopulated_fields = {'slug': ('name',)}
