from django.db import models

# Create your models here.


class UserLogin(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    email_id = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50, null=True)
    user_type = models.CharField(max_length=50, null=True)


class Profile(models.Model):
    employee_id = models.AutoField(max_length=50, primary_key=True, editable=False, default='0001',
                                      auto_created=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
