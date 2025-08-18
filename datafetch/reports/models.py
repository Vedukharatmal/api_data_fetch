from django.db import models

# Create your models here.

class DummyReport(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateField()
    value = models.IntegerField()


    def __self__(self):
        return f"{self.name} - {self.date}"
