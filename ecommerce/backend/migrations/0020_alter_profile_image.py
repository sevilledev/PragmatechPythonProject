# Generated by Django 3.2.3 on 2021-08-11 15:45

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/home/sevilledev/Desktop/Django/PragmatechPythonProject/ecommerce/media/profile_pictures/default_user.jpg', storage=django.core.files.storage.FileSystemStorage(location='/home/sevilledev/Desktop/Django/PragmatechPythonProject/ecommerce/media'), upload_to='profile_pictures/'),
        ),
    ]
