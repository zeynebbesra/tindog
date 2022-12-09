from django.urls import path
from . import views

urlpatterns = [
    path('endpoints', views.endpoints),
    path('dogs', views.get_dogs)
]

