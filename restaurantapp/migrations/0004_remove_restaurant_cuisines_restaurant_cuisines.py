# Generated by Django 4.0.1 on 2023-06-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0003_visitedrestaurant_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisines',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisines',
            field=models.CharField(choices=[('fastfood', 'fastfood'), ('Gujarati', 'Gujarati'), ('Hyderabadi', 'Hyderabadi'), ('Chinese', 'Chinese')], default='fastfood', max_length=20),
        ),
    ]