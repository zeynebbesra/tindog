from django.urls import path
from . import views

urlpatterns = [
    #path('', views.main ),
    path('dogs', views.get_dogs),   #dogs listesine dog ekliyor
    path('dogs/add_dog', views.add_dog), #dogs listesini veriyor
    path('dogs/<str:id>/', views.get_dog) #dog'u id'ye göre veriyor
]

