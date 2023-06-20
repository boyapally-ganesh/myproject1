
from django.urls import path
from . import views
from . import consumers

app_name = 'restaurantapp'

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<str:slug>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurants/<int:restaurant_id>/bookmark/', views.bookmark_add, name='bookmark_adds'),
    # path('restaurants/<str:slug>/visited/', views.mark_visited, name='mark_visited'),
    path('restaurants/<int:restaurant_id>/visited/', views.mark_visited, name='mark_visited'),
    path('bookmarks/', views.get_user_bookmarks, name='bookmarks'),
    path('bookmarks/remove/<int:restaurant_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('my-visited-restaurants/', views.my_visited_restaurants, name='my_visited_restaurants'),
    path('delete-visited-restaurant/<int:restaurant_id>/', views.delete_visited_restaurant, name='delete_visited_restaurant'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('restaurants/<str:slug>/add-review/', views.add_review, name='add_review'),
    # path('restaurants/<str:slug>/review/<int:review_id>/', views.add_review, name='edit_review'),
    # .........
    # path('restaurants/<slug:slug>/delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    #......
    # path('restaurants/<str:slug>/edit-review/<int:review_id>/', views.edit_review, name='edit_review')
    path('update-review/', views.update_review, name='update_review'),
    path('delete-review/', views.delete_review, name='delete_review')


]




