from django.db import models
from datetime import datetime

# Create your models here.
class Customers(models.Model):
    c_name = models.CharField(max_length=40)
    seat_no = models.IntegerField()

    def __str__(self):
        return self.c_name

class Drinks(models.Model):
    drinks_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    manufacture_date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name

class Food(models.Model):
    food_id = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=40)
    food_class = models.CharField(max_length=40)

    def __str__(self):
        return self.food_name