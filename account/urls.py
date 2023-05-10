from .views import login_view,register
from django.urls import path


urlpatterns = [
    path('',login_view,name='login'),
    path('register/',register,name='register'),
   
]
