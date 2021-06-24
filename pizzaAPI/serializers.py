from rest_framework import serializers
from .models import Pizza, PizzaTopping


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaTopping
        fields = '__all__'
