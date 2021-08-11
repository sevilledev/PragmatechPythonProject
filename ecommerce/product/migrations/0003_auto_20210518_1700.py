# Generated by Django 3.2.3 on 2021-05-18 17:00

import django.core.files.storage
from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210416_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/sevilledev/Desktop/Django/PragmatechPythonProject/ecommerce/media'), upload_to=product.models.upload_product_file_loc),
        ),
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/sevilledev/Desktop/Django/PragmatechPythonProject/static_cdn/product_media'), upload_to=product.models.upload_product_file_loc),
        ),
    ]
