from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pizza/', include('pizzaAPI.urls')),
    path('admin/', admin.site.urls),
]
