from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('articles.html', article, name='article'),
    path('cars.html', cars, name='cars'),
    path('category.html', category, name='category'),
]