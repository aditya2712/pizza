from django.db import models


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
