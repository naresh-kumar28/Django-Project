from django.db import models

# Create your models here.

class StudentRecord(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.CharField()
    school_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    math = models.IntegerField()
    hindi = models.IntegerField()
    science = models.IntegerField()
    sst = models.IntegerField()
    english = models.IntegerField()

    def __str__(self):
        return self.name
    
    def getTotal(self):
        return self.math + self.hindi + self.science + self.sst + self.english