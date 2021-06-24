from django.db import models


class PizzaTopping(models.Model):
    topping = models.TextField(primary_key=True)

    def __str__(self):
        return self.topping

class Pizza(models.Model):
    class PizzaType(models.TextChoices):
        Regular = 'Regular'
        Square = 'Square'

    class PizzaSize(models.TextChoices):
        Small = 'Small'
        Medium = 'Medium'
        Large = 'Large'
        Jumbo = 'Jumbo'

    type = models.TextField(choices=PizzaType.choices)
    size = models.TextField(choices=PizzaSize.choices)
    toppings = models.ManyToManyField(to=PizzaTopping)
