from django.urls import path
from .api import CreatePizzaAPI, GetAllPizzaAPI, GetPizzaBasedOnFilterAPI, DeletePizzaAPI, UpdatePizzaAPI

urlpatterns = [
    path('create/', CreatePizzaAPI.as_view(), name='create-pizza'),
    path('get-all/', GetAllPizzaAPI.as_view(), name='get-all'),
    path('get/', GetPizzaBasedOnFilterAPI.as_view(), name='get'),
    path('delete/<pk>', DeletePizzaAPI.as_view(), name='delete'),
    path('update/<pk>', UpdatePizzaAPI.as_view(), name='update'),
]
