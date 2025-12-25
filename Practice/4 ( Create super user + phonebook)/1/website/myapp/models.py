from django.db import models

# Create your models here.

class PhoneBook(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()