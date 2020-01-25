from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)

    gender = models.BooleanField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    postal_code = models.CharField(max_length=16)
    house_number_additions = models.CharField(max_length=16)
    street_name = models.CharField(max_length=64)
    city_name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    phone_number = models.CharField(max_length=16)
    date_of_birth = models.DateField()
