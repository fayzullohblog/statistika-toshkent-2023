from .views import login_view,register,logout_view
from django.urls import path


urlpatterns = [
    path('',login_view,name='login'),
     path('logout/',logout_view,name='logout'),
    path('register/',register,name='register'),
   
]
