from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .serializers import PizzaSerializer
from .models import Pizza


class CreatePizzaAPI(generics.CreateAPIView):
    serializer_class = PizzaSerializer


class GetAllPizzaAPI(generics.ListAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class GetPizzaBasedOnFilterAPI(generics.ListAPIView):
    serializer_class = PizzaSerializer
    model = Pizza

    def get_queryset(self):
        type_filter = self.request.GET.get('type')
        size_filter = self.request.GET.get('size')

        if type_filter is None and size_filter is None:
            raise ValidationError("please provide atleast one filter or to get all data user 'get-all' endpoint")

        if type_filter is not None:
            queryset = Pizza.objects.filter(type__iexact=type_filter)
        if size_filter is not None:
            queryset = queryset.filter(size__iexact=size_filter)

        return queryset
