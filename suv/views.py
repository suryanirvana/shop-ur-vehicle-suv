from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    response = {}
    return render(request,'index.html',response)

def article(request):
    response = {'article_list':Article.objects.all().values()}
    return render(request,'articles.html',response)

def cars(request):
    car_list = list(Car.objects.all().values())
    for i in range(len(car_list)):
        car_list[i]['category'] = Category.objects.get(pk=car_list[i]['category_id']).car_type
    try:
        response = {'recomended_car':car_list[0],'car_list':car_list}
    except:
        response = {'car_list':car_list}
    return render(request,'cars.html',response)
	
def category(request):
	response = {}
	return render(request, 'category.html', response)