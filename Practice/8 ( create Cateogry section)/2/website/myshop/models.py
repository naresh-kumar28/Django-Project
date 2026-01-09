from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return self.name