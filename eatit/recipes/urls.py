from django.contrib.auth import login
from django.urls import path

from .views import *

urlpatterns = {
    path('', index),
    path('login/', login, name='login'),
    path('register/'. RegisterUser.as_view(), name='register'),
}
