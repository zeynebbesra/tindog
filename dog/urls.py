from django.urls import path
from . import views

urlpatterns = [
    #path('', views.main ),
    path('dogs', views.get_dogs, name='dogs'),  
    path('dogs/add_dog', views.add_dog), 
    #path('dogs/<str:id>/', views.get_dog) 
    path('dogs/<str:id>/', views.DogDetails.as_view()) 
]

