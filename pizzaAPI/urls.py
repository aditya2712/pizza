from django.urls import path
from .api import CreatePizzaAPI

urlpatterns = [
    path('create/', CreatePizzaAPI.as_view(), name='create-pizza'),
]
