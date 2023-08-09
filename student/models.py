from django.db import models
from staff.models import Student_data
from admin.models import Standard,Subject
# Create your models here.


class MarkList(models.Model):
    term=models.CharField(max_length=10,default="")
    student=models.ForeignKey(
        to=Student_data,
        on_delete=models.CASCADE)
    subject=models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE)
    marks_obtained=models.IntegerField(
        default=0.0,
        verbose_name='marks obtained')
    max_marks=models.IntegerField(
        default=0.0, 
        verbose_name='max marks')
    
    
    