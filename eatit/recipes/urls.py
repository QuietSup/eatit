from django.urls import path

from .views import *

urlpatterns = {
    path('', index),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<int:cat_id>/', show_category, name='category'),
}
