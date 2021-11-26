from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField('Recipe name', max_length=50)
    photo = models.ImageField('Photo', upload_to='photos')
    content = models.TextField('Content', blank=True)
    time_created = models.DateTimeField('Creation time', auto_now_add=True)
    time_updated = models.DateTimeField('Update time', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient', kwargs={'ingr_id': self.pk})


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_id', 'post_id'], name="unique_blog_likes")
        ]

    def __str__(self):
        return f'{self.user_id.username} --> {self.post_id.name}'
