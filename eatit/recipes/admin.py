from django.contrib import admin
from .models import *


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'time_created', 'time_updated')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
