# Generated by Django 3.2.3 on 2021-05-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_userverify'),
    ]

    operations = [
        migrations.AddField(
            model_name='userverify',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
