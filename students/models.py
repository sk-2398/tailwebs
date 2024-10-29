from django.db import models
from teachers.models import *
# Create your models here.
class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="students")
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   