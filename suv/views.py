from django.shortcuts import render,redirect
from .models import *
from .forms import *
import datetime

# Create your views here.
def index(request):
    ln = len(Article.objects.all())-1
    article = Article.objects.all().values()[ln]
    title = article['title']
    content = article['content'].split(".")[:3]
    content = " ".join(content) + "."
    response = {'title' : title , "content" : content}
    return render(request,'index.html',response)

def review(request):
    if request.method == "POST":
        req = request.POST
        form = ReviewForm(request.POST)
        # print("\nIni Request :",req)
        print(req)
        print(req['car'])

        new_car = Car.objects.get(name=req['car'])
        new_car.save()

        new_review = Review.objects.create(username=req['username'],car=new_car,message = req['message'],created_date = req['created_date'],rating = req['rating'])
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

        new_car = Car.objects.create(name=req['name'],price=req['price'],description=req['description'],category=type_car,year = req['year'],city = req['location'],username = req['owner'],car_image = req['car_image'])
        new_car.save()
        return redirect('/category.html?q=' + req['car_type'])
    else:
        form = CarForm()
    cars = Car.objects.all()
    car_type = Category.objects.all()
    response = {'cars' : cars, 'car_type' : car_type}
    return render(request,'rent.html',response)

def transaction(request):
    if request.method == "POST":
        req = request.POST
        form = TransactionForm(request.POST, request.FILES)

        type_car = Category.objects.get_or_create(car_type=req['car_type'])[0]
        type_car.save()
        new_car = Transaction.objects.create(name=req['name'],category=type_car,year = req['year'],city = req['location'],date=datetime.datetime.today())
        new_car.save()
        return redirect('/transaction.html')
    else:
        form = TransactionForm()
    cars = Transaction.objects.all()
    car_type = Category.objects.all()
    response = {'cars' : cars, 'car_type' : car_type}
    return render(request,'transaction.html',response)

def article(request):
    response = {'article_list':Article.objects.all().values()}
    return render(request,'articles.html',response)

def category(request):
    #Get GET REQUEST
    req = request.GET

    #Handle if no query is passed
    if 'q' in req:
        response = {'title':req['q'],'car_list':[]}
    elif 'price' in req:
        response = {'title':req['price'],'car_list':[]}
    elif 'year' in req:
        response = {'title':req['year'],'car_list':[]}
    elif 'city' in req:
        response = {'title':req['city'],'car_list':[]}
    else:
        response = {'title':'No matching car found.','car_list':[]}
        #return render(request,'category.html',response)

    #Making Car List
    car_all = list(Car.objects.all().values())
    car_list = list()


    if 'q' in req:
        #Set category for each cars
        for i in range(len(car_all)):
            car_all[i]['category'] = Category.objects.get(pk=car_all[i]['category_id']).car_type

        #List all cars that fit the category
        for i in car_all:
            if i['category'].lower() == req['q'].lower():
                    car_list.append(i)  
    elif 'price' in req:
        #List all cars that fit the category
        for i in car_all:
            if i['price'] <= req['price']:
                    car_list.append(i)
    elif 'year' in req:
        #List all cars that fit the category
        for i in car_all:
            if i['year'] == req['year']:
                    car_list.append(i)
    elif 'city' in req:
        #List all cars that fit the category
        for i in car_all:
            if i['city'].lower() == req['city'].lower():
                    car_list.append(i)
    else:
        pass


    #If there is no car, then say no matching cars
    if (not car_list):
        response = {'title':'No matching car found.','car_list':[]}
        #return render(request,'category.html',response)
    
    try:
        if 'q' in req:    
        #Making Recomended Car
            response = {'title':req['q'],'recomended_car':car_list[0],'car_list':car_list}
        elif 'price' in req:
            response = {'title':req['price'],'recomended_car':car_list[0],'car_list':car_list}
        elif 'year' in req:
            response = {'title':req['year'],'recomended_car':car_list[0],'car_list':car_list}
        elif 'city' in req:
            response = {'title':req['city'],'recomended_car':car_list[0],'car_list':car_list}
        else:
            pass
    except:
        response = {'title':'No matching car found.','car_list':[]}
        

    return render(request,'category.html',response)
