from django.urls import path
from .views import *



urlpatterns = [
    path('signup', create_user, name='create_user'),
    path('login', get_user, name='get_user')
]