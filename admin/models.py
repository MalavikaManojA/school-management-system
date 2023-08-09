from django.db import models
from accounts.models import User
# Create your models here.

class Standard(models.Model):
    standard=models.CharField(
        max_length=10
    )
    def __str__(self) -> str:
        return 'class'+ self.standard

class StaffDetail(models.Model):
    staff_name=models.ForeignKey(
        to=User,
        default='',
        on_delete=models.CASCADE
    )
    sub_taught=models.CharField(
        max_length=20,
        
    )
    qualification=models.TextField(
        null=True,
        blank=True
    )
    class_taught=models.ForeignKey(
        to=Standard,
        unique=True,
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return self.staff_name
    
class Subject(models.Model):
    sub=models.CharField(
        verbose_name='Subject',
        max_length=20,
        default=''
        )
    standard=models.ForeignKey(
        to=Standard,
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return self.sub

