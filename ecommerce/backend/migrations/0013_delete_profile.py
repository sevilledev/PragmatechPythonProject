# Generated by Django 3.2.3 on 2021-08-11 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('chat', '0002_room'),
        ('cart', '0003_delete_t'),
        ('billing', '0003_alter_billingprofile_user'),
        ('analytics', '0001_initial'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('backend', '0012_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
