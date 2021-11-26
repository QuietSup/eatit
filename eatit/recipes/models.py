from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField('Recipe name', max_length=50)
    photo = models.ImageField('Photo', upload_to='photos')
    ingredients = models.TextField('Ingredients', null=True)
    time_created = models.DateTimeField('Creation time', auto_now_add=True)
    time_updated = models.DateTimeField('Update time', auto_now=True)
    cat = models.ManyToManyField('Category', verbose_name='Categories')
    ingr = models.ManyToManyField('Ingredient', verbose_name='Ingredients')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    calories = models.IntegerField('Calories number', max_length=5)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient', kwargs={'ingr_id': self.pk})
