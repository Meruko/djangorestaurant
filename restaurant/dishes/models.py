from django.db import models

class Ingridient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)
    count = models.IntegerField(default=0)
    # common = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return '/ingridients/'

class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    default_price = models.FloatField(default=0.00)
    ingridients = models.ManyToManyField(Ingridient, related_name='ingridients')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return '/'