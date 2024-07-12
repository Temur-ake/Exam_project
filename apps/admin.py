from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin, register

from apps.models import ProductImage, Product


# Register your models here.


class ProductImageStackedInline(StackedInline):
    model = ProductImage
    extra = 2
    min_num = 0


@register(Product)
class ProductModelAdmin(ModelAdmin):
    list_display = 'title', 'is_premium',
    inlines = [ProductImageStackedInline]
