from django.db import models

from django.contrib.auth.models import AbstractUser, User


class UserInfo(AbstractUser):

    groups = None
    user_permissions = None

class UserAddress(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    default = models.BooleanField()

