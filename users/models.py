from django.db import models

# Create your models here.

class Profile(models.Model):
    employee_id = models.AutoField(max_length=50, primary_key=True, editable=False,
                                      auto_created=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name


class UserLogin(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    email_id = models.ForeignKey(Profile, on_delete=models.CASCADE )
    user_password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50, null=True)
    user_type = models.CharField(max_length=50, null=True)