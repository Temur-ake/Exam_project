from django.db import models
from django.db.models import Model, CharField, TextField, ImageField, ForeignKey, BooleanField, CASCADE
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Product(Model):
    title = CharField(max_length=255)
    description = TextField()
    is_premium = BooleanField(default=True)
    video_file = models.FileField(upload_to='products/', blank=True, null=True)


class ProductImage(Model):
    image = ImageField(upload_to='products/%Y/%m/%d/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
