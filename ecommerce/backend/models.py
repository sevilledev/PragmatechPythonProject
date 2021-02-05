from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    is_branch = models.BooleanField(default=True)
    is_delivery = models.BooleanField(default=True)
    is_phone_status = models.BooleanField(default=True)


class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address_name = models.CharField(max_length=40)
    home = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

    #address_location