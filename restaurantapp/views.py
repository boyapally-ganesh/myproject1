from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import ReviewForm
# Create your views here.
from django.shortcuts import render
from .models import Restaurant, Bookmark, VisitedRestaurant, Dish, Photo, Review
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
def restaurant_list(request):
    # location = request.GET.get('location')
    # veg_or_nonveg = request.GET.get('veg_or_nonveg')
    # cuisines = request.GET.getlist('cuisines')
    # open_or_close = request.GET.get('open_or_close')
    restaurants = Restaurant.objects.all()
    # if location:
    #     restaurants = restaurants.filter(location=location)
    # if veg_or_nonveg:
    #     restaurants = restaurants.filter(veg_or_nonveg=veg_or_nonveg)
    # if cuisines:
    #     restaurants = restaurants.filter(cuisines__in=cuisines)
    # if open_or_close:
    #     restaurants = restaurants.filter(open_or_close=open_or_close)
    context = {'restaurants': restaurants}
    return render(request, 'restaurant_list.html', context)

# def restaurant_detail(request, slug):
#     if(Restaurant.objects.filter(slug=slug)):
#         restaurants = Restaurant.objects.filter(slug=slug).first()
#         context = {
#             'restaurants':restaurants
#         }
#         return render(request, 'restaurant_detail.html',context)
    
#     else:
#         return redirect('restaurants/')
#     # context = {'restaurant': restaurant}
#     return render(request, 'restaurant_detail.html', context)
# def restaurant_detail(request, slug):
#     restaurant = Restaurant.objects.filter(slug=slug).first()
#     if restaurant:
#         context = {'restaurant': restaurant}
#         return render(request, 'restaurant_detail.html', context)
#     else:
#         return redirect('restaurant_list')
# this is main.............................
def bookmark_add(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, restaurant=restaurant)
    if created:
        print("add sucessfully")

        # Bookmark was added
        # Add any additional logic or messages here
        # return redirect('restaurant_detail', slug=restaurant.slug)
        return JsonResponse({'status': 'Bookmark added successfully'})
    else:
        # Bookmark already exists
        # Add any additional logic or messages here
        print("Bookmark already exists")
        # return redirect('restaurant_detail', slug=restaurant.slug)
        return JsonResponse({'status': 'Bookmark allready'})

def mark_visited(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    visited, created = VisitedRestaurant.objects.get_or_create(user=request.user, restaurant=restaurant)
    if created:
        print("Restaurant marked as visited successfully")
        return JsonResponse({'status': 'visited added successfully'})
        # Additional logic or messages can be added here
    else:
        print("Restaurant is already marked as visited")
        # Additional logic or messages can be added here
        return JsonResponse({'status': 'all ready add'})



def restaurant_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    bookmarked = False
    visited = False
    if request.user.is_authenticated:
        bookmarked = Bookmark.objects.filter(user=request.user, restaurant=restaurant).exists()
        visited = VisitedRestaurant.objects.filter(user=request.user, restaurant=restaurant).exists()
    dishes = Dish.objects.filter(restaurant=restaurant)
    restaurant_photos = Photo.objects.filter(restaurant=restaurant)
    reviews = Review.objects.filter(restaurant=restaurant)
      # Process the review form
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', slug=slug)
    else:
        form = ReviewForm()

    # Get the reviews for the restaurant
   
   
       
        

        
        # Redirect to the restaurant detail page
    
    
    # Get the reviews for the restaurant
    reviews = Review.objects.filter(restaurant=restaurant)
    context = {
        'restaurant': restaurant,
        'bookmarked': bookmarked,
        'visited': visited,
        'dishes': dishes,
        'restaurant_photos': restaurant_photos,
        'reviews': reviews,
       
    }
    return render(request, 'restaurant_detail.html', context)

@login_required
def get_user_bookmarks(request):
    user = request.user
    bookmarks = Bookmark.objects.filter(user=user)
    
    # You can access the bookmarked restaurants or other fields as needed
    bookmarked_restaurants = [bookmark.restaurant for bookmark in bookmarks]
    
    context = {
        'bookmarks': bookmarked_restaurants
    }
    return render(request, 'user_bookmarks.html', context)

def remove_bookmark(request, restaurant_id):
    bookmark = get_object_or_404(Bookmark, user=request.user, restaurant_id=restaurant_id)
    if request.method == 'POST':
        bookmark.delete()
    return redirect('restaurantapp:bookmarks')




def my_visited_restaurants(request):
    user = request.user
    visited_restaurants = VisitedRestaurant.objects.filter(user=user)
    
    # You can access the visited restaurants or other fields as needed
    visited_restaurant_list = [visited.restaurant for visited in visited_restaurants]
    
    context = {
        'visited_restaurants': visited_restaurant_list
    }
    return render(request, 'my_visited_restaurants.html', context)

def delete_visited_restaurant(request, restaurant_id):
    visited_restaurant = get_object_or_404(VisitedRestaurant, user=request.user, restaurant_id=restaurant_id)
    
    if request.method == 'POST':
        visited_restaurant.delete()
    
    return redirect('restaurantapp:my_visited_restaurants')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('restaurantapp:restaurant_list')  # Redirect to desired page after login
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('restaurantapp:restaurant_list')


def add_review(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', slug=slug)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'restaurant': restaurant,
    }

    return render(request, 'add_review.html', context)

# def delete_review(request, slug, review_id):
#     review = get_object_or_404(Review, id=review_id)
#     # Perform any necessary checks or validations
#     if request.method == 'POST':
#         # Delete the review
#         review.delete()
#     # Redirect to the restaurant detail page
#     return redirect('restaurantapp:restaurant_detail', slug=slug)
@login_required
def delete_review(request, slug, review_id):
    # Retrieve the review object
    review = get_object_or_404(Review, id=review_id)

    # Check if the logged-in user is the owner of the review
    if review.user != request.user:
        # User is not the owner, return an error response or redirect to an appropriate page
        # For example, you can redirect back to the restaurant detail page
        return redirect('restaurantapp:restaurant_detail', slug=slug)

    # Delete the review
    review.delete()

    # Redirect to the restaurant detail page
    return redirect('restaurantapp:restaurant_detail', slug=slug)


