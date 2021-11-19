from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    ingredients = models.TextField(null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    cat = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
