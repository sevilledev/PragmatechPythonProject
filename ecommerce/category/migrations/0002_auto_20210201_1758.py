# Generated by Django 3.1.1 on 2021-02-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]