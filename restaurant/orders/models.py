from django.db import models
from dishes.models import Dish

class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    dishes = models.ManyToManyField(Dish, related_name='dishes', through='OrderComposition')
    cost = models.FloatField(default=0.00)

    def __str__(self) -> str:
        return str(self.date)

class OrderComposition(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish_count = models.IntegerField(default=1)