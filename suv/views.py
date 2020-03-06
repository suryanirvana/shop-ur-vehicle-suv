from django.shortcuts import render,redirect
from .models import *
from .forms import *
import datetime

# Create your views here.
def index(request):
    response = {}
    return render(request,'index.html',response)

def review(request):
    if request.method == "POST":
        req = request.POST
        form = ReviewForm(request.POST)
        print("\nIni Request :",req)

        new_car = Car.objects.get(name=req['year'])
        new_car.save()

        new_review = Review.objects.create(username=req['name'],car=new_car,message = req['location'],created_date = datetime.datetime.today(),rating = req['owner'])
        new_review.save()
        return redirect('/review.html')
    else:
        form = ReviewForm()
    reviews = Review.objects.all()
    car = Car.objects.all()
    response = {'reviews' : reviews, 'car' : car}
    return render(request, 'review.html', response)

def rent(request):
    if request.method == "POST":
        req = request.POST
        form = CarForm(request.POST, request.FILES)

        type_car = Category.objects.get_or_create(car_type=req['car_type'])[0]
        type_car.save()

        new_car = Car.objects.create(name=req['name'],category=type_car,year = req['year'],city = req['location'],username = req['owner'],car_image = req['car_image'])
        new_car.save()
        return redirect('/rent.html')
    else:
        form = CarForm()
    cars = Car.objects.all()
    car_type = Category.objects.all()
    response = {'cars' : cars, 'car_type' : car_type}
    return render(request,'rent.html',response)

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