from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    def __str__(self):
        return self.email