from django.urls import path
from . import views

urlpatterns = [
    path('users',views.get_users),
    path('users/add_user',views.add_user),
    #path('users/<str:id>/',views.get_user)
    path('users/<str:id>/', views.UserDetails.as_view())
]
