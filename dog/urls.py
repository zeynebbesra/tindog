from django.urls import path
from . import views

urlpatterns = [
    path('', views.main ),
    path('dogs', views.get_dogs),
    path('dogs/<str:id>/', views.get_dog)
]

