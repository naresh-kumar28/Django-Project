from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='image/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
