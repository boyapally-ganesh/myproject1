from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import os
from django.contrib.auth.decorators import login_required
# Create your models here.
def get_file_path(request, filname):
    original_filename = filname
    nowtime = datetime.datetime.now().strftime('%Y%m%d%h,:%M:%S')
    filename = '%s%s' % (nowtime, original_filename)
    return os.path.join('uploads/', filename)


class Restaurant(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    restaurant_photo_home = models.ImageField(upload_to=get_file_path)
  
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )

    cost_for_two = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.CharField(max_length=100)
    Hyderabad = "Hyderabad"
    Banglore = 'banglore'
    Channai = "channai"
    Tamilnadu = "Tamilnadu"
    Delhi = 'Delhi'
    Mumbai = 'mumbai'
    location_choices = (
        (Hyderabad, "Hyderabad"),
        (Banglore, 'banglore'),
        (Channai, "channai"),
        (Delhi, 'Delhi'),
        ( Mumbai, 'mumbai'),
    )
    location = models.CharField(max_length=100, choices=location_choices, default='Hyderabad')
    address = models.TextField()
    timings = models.CharField(max_length=100)
    VEG = 'Veg'
    VEGAN = 'Vegan'
    NON_VEG = 'Non Veg'
    FOOD_CHOICES = (
        (VEG, 'Veg'),
        (VEGAN, 'Vegan'),
        (NON_VEG, 'Non Veg'),
    )
    veg_or_nonveg = models.CharField(max_length=10, choices=FOOD_CHOICES)
    OPEN = 'open'
    CLOSE = 'close'
    OPEN_OR_CLOSE = (
        (OPEN, 'open'),
        (CLOSE, 'close'),
    )
    open_or_close = models.CharField(max_length=20, choices=OPEN_OR_CLOSE)
    Fast_Food = 'fastfood'
    Gujarati = 'Gujarati'
    Hyderabadi = 'Hyderabadi'
    Chinese = 'Chinese'
    CUISINES = (
        (Fast_Food, 'fastfood'),
        (Gujarati, 'Gujarati'),
        (Hyderabadi, 'Hyderabadi'),
        (Chinese, 'Chinese'),
       )
    cuisines = models.CharField(max_length=20, choices=CUISINES, default='fastfood')


class Photo(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path)


# class Cuisine(models.Model):
#     # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)


class Dish(models.Model):
    slug = models.CharField(max_length=100, null=100, blank=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_path)
    VEG = 'Veg'
    NON_VEG = 'Non Veg'
    FOOD_CHOICES = (
        (VEG, 'Veg'),
        (NON_VEG, 'Non Veg'),
    )
    veg_or_nonveg = models.CharField(max_length=10, choices=FOOD_CHOICES)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1,   validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class VisitedRestaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)