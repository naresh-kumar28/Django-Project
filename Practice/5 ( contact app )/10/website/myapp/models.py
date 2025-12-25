from django.db import models

# Create your models here.
class phonebook(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()

    def __str__(self):
        return self.name