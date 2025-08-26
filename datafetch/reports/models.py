from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateField()
    value = models.IntegerField()
    price = models.IntegerField()

    def __self__(self):
        return self.name
    

class Product(models.Model):
    product = models.CharField(max_length = 100)
    date2 = models.DateField()
    value2 = models.IntegerField()
    rate = models.IntegerField()

    def __self__(self):
        return self.product
    