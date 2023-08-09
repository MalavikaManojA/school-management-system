from django.db import models
from accounts.models import User
from admin.models import Standard,StaffDetail

# Create your models here.

class ParentDetail(models.Model):
    parent_name=models.CharField(
        max_length=20
    )
    parent_email=models.EmailField()
    parent_phone=models.BigIntegerField(
        null=True,
        blank=True
    )
    parent_job=models.CharField(
        max_length=20,
        null=True,
        blank=True
    )


class Student_data(models.Model):
    student=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    parent=models.ForeignKey(
        to=ParentDetail,
        on_delete=models.CASCADE
    )
    standard=models.ForeignKey(
        to=Standard,
        on_delete=models.CASCADE
    )
    teacher=models.ForeignKey(
        to=StaffDetail,
        on_delete=models.CASCADE
    )


