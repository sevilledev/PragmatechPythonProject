# Generated by Django 3.2.3 on 2021-08-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
