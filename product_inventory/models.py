from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)


class ItemLibrary(models.Model):
    item = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    unit = models.IntegerField(max_length=50)
    in_stock = models.FloatField(max_length=50)
    price = models.FloatField(max_length=50)


