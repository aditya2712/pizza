from django.db import models


class Pizza(models.Model):
    class PizzaType(models.TextChoices):
        REGULAR = 'Regular'
        SQUARE = 'Square'

    class PizzaSize(models.TextChoices):
        S = 'Small'
        M = 'Medium'
        L = 'Large'
        XL = 'Extra-Large'

    type = models.TextField(choices=PizzaType.choices)
    size = models.TextField(choices=PizzaSize.choices)
