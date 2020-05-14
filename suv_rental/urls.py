"""suv_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('suv.urls')),
    path('index.html', include('suv.urls')),
    path('articles.html', include('suv.urls')),
    # path('cars.html', include('suv.urls')),
    path('rent.html', include('suv.urls')),
    path('category.html', include('suv.urls')),  
    path('review.html', include('suv.urls')),  
    path('transaction.html', include('suv.urls')),  
    path('', include('social_django.urls', namespace='social')),
]