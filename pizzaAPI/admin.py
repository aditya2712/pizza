from django.contrib import admin

from .models import Pizza, PizzaTopping

admin.site.register(Pizza)
admin.site.register(PizzaTopping)