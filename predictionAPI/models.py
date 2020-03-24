from django.db import models


class Prediction(models.Model):
    category = models.CharField(max_length=50, default='Grocery')
    product = models.CharField(max_length=50, default='')
    gross_sale = models.FloatField(max_length=50, default=0.0)
    qty = models.FloatField(max_length=50, default=0.0)
    month = models.IntegerField(max_length=50, default=1)

    def __str__(self):
        return self.category



