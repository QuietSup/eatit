from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name=''),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('filter/', FilterRecipes.as_view(), name='filter'),
    path('search/', Search.as_view(), name='search'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('my_recipes/', my_recipes, name='my_recipes'),
    path('favorites/', favorites, name='favorites')
]
