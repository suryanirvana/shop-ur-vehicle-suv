from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('articles.html', article, name='article'),
]