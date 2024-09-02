from django.db import models
# Create your models here.
class List(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()