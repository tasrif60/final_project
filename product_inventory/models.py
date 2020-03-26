from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class ItemLibrary(models.Model):
    item = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.IntegerField(max_length=50)
    in_stock = models.FloatField(max_length=50)
    price = models.FloatField(max_length=50)


class Itemlist(models.Model):
    itemlist = models.CharField(max_length=50)

    def __str__(self):
        return self.itemlist
