from django.db import models


from users.models import Profile


class Schedule(models.Model):
    title = models.CharField(max_length=100, )
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    note = models.CharField(max_length=200)


def __str__(self):
    return self.title
