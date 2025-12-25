from django.db import models

# Create your models here.

class Phonebook(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
