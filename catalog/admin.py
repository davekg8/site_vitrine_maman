from django.contrib import admin
from unfold.admin import ModelAdmin
from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('category',)
    readonly_fields = ('image_preview',)

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('image_preview',)

