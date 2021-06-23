from rest_framework import generics
from .serializers import PizzaSerializer


class CreatePizzaAPI(generics.CreateAPIView):
    serializer_class = PizzaSerializer
