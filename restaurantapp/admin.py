from django.contrib import admin

# Register your models here.


# Register your models here.

from .models import Restaurant, Photo, Dish, Review, Bookmark, VisitedRestaurant

admin.site.register(Restaurant)
admin.site.register(Photo)
# admin.site.register(Cuisine)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(Bookmark)
admin.site.register(VisitedRestaurant)
