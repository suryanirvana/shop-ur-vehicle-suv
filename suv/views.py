from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    response = {}
    return render(request,'index.html',response)

def rent(request):
    response = {}
    return render(request,'rent.html',response)

def review(request):
    response = {}
    return render(request,'review.html',response)

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
    #Get GET REQUEST
    req = request.GET

    #Handle if no query is passed
    if 'q' not in req:
        response = {'title':'No matching car found.','car_list':[]}
        return render(request,'category.html',response)
    else:
        response = {'title':req['q'],'car_list':[]}

    #Making Car List
    car_all = list(Car.objects.all().values())
    car_list = list()

    #Set category for each cars
    for i in range(len(car_all)):
        car_all[i]['category'] = Category.objects.get(pk=car_all[i]['category_id']).car_type

    #List all cars that fit the category
    for i in car_all:
        try:
            if i['category'].lower() == req['q'].lower():
                car_list.append(i)
        except:
            pass

    #If there is no car, then say no matching cars
    if (not car_list):
        response = {'title':'No matching car found.','car_list':[]}
        return render(request,'category.html',response)

        
    #Making Recomended Car
    try:
        response = {'title':req['q'],'recomended_car':car_list[0],'car_list':car_list}
    except:
        response = {'title':req['q'],'car_list':{}}

    return render(request,'category.html',response)