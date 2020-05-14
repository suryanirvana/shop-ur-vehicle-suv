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
