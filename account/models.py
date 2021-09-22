from django.db import models

from django.contrib.auth.models import AbstractUser, User


class UserInfo(AbstractUser):

    groups = None
    user_permissions = None

class UserAddress(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

