# Generated by Django 5.0.7 on 2024-07-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
