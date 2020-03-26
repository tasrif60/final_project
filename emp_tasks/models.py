from django.db import models
from users.models import Profile

# Create your models here.
class Tasks (models.Model):
    employee = models.ForeignKey(Profile, on_delete=models.CASCAD)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
