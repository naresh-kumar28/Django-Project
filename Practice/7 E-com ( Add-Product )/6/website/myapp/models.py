from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(12)

    def __str__(self):
        return self.name