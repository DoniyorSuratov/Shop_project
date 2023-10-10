from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()


class Images(models.Model):
    img = models.ImageField(upload_to='pics')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
