from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields specific to Teacher if needed

    def __str__(self):
        return self.user.username