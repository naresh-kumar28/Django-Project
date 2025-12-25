from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=20)
    schoolname = models.CharField(max_length=200)
    fathername = models.CharField(max_length=100)

    math = models.IntegerField()
    sci = models.IntegerField()
    sst = models.IntegerField()
    hindi = models.IntegerField()
    eng = models.IntegerField()

    def __str__(self):
        return self.name

    def getTotal(self):
        return self.math + self.sci + self.sst + self.hindi +self.eng