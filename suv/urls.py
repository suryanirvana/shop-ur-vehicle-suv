from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('articles.html', article, name='article'),
    # path('cars.html', cars, name='cars'),
    path('category.html', category, name='category'),
    path('rent.html', rent, name='rent'),
    path('transaction.html', transaction, name='transaction'),
    path('review.html', review, name='review'),
    path('favorite_api', favorite_api, name='favorite_api'),
    path('favorite_car_list', favorite_car_list, name='favorite_car_list'),
    path('login.html', login_user, name='login_user'),
    path('signup.html', signup_user, name='signup_user'),
    path('logout/', logout_user, name='logout'),
    path('api/articles/', articles, name='articles'),
    path('api/likearticles/', likearticles, name='likearticles'),
]