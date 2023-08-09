from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    phone=models.CharField(max_length=10,default='')
    date_of_birth = models.DateField(default=timezone.now)
    photo=models.ImageField(null=True,blank=True)
    
class Contact(models.Model):
    c_name=models.CharField(max_length=25)

    from_mail=models.EmailField(
        max_length=50,
        null=False,
        blank=False,
        unique=False
    )
    subject=models.TextField(
        max_length=100,
        null=True,
        blank=True
    )
    body=models.TextField(
        max_length=50000,
        null=False,
        blank=False
    )
    def __str__(self) -> str:
        return self.c_name

