from django.db import models

# Create your models here.

class Vcard(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name
        # return f"{self.name} : {self.phone_no}"
