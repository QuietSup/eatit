# Generated by Django 3.2.8 on 2021-11-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
    ]
