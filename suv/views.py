from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
import datetime
import json

# Create your views here.
counter = 0
id = 999999

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
        new_car = Transaction.objects.create(name=req['name'],user=request.user,category=type_car,year = req['year'],city = req['location'],date=datetime.datetime.today())
        new_car.save()
        return redirect('/transaction.html')
    else:
        form = TransactionForm()
    cars = Transaction.objects.all()
    car_type = Category.objects.all()
    response = {'cars' : cars, 'car_type' : car_type}
    return render(request,'transaction.html',response)

def article(request):
    response = {'article_list':Article.objects.all(), 'articleForm':ArticleForm()}
    return render(request,'articles.html',response)

def category(request):
    #Get GET REQUEST
    req = request.GET
    all_fav = FavoriteCar.objects.all().values()
    db = []
    for i in all_fav:
        if (i['user_id'] == request.user.id):
            db.append(i['car_id'])
    # Handle if no query is passed
    if 'q' not in req:
        response = {'title':'No matching car found.','car_list':[]}
        return render(request,'category.html',response)
    response = {'title':req['q'],'car_list':[]}

    #Making Car List
    car_all = list(Car.objects.all().values())
    car_list = list()

    #Set category for each cars
    for i in range(len(car_all)):
        car_all[i]['category'] = Category.objects.get(pk=car_all[i]['category_id']).car_type

    #List all cars that fit the category
    trans_list = set([i['name'] for i in Transaction.objects.all().values() if i['user_id'] == request.user.id])

    for i in car_all:
        car_obj = Car.objects.get(pk=i['id'])
        if (i['category'].lower() == req['q'].lower()) and (car_obj.name not in trans_list):
            car_list.append(i)

    #If there is no car, then say no matching cars
    if (not car_list):
        response = {'title':'No matching car found.','car_list':[]}
        return render(request,'category.html',response)

    #Making Recomended Car
    try:
        response = {'title':req['q'],'recomended_car':car_list[0],'car_list':car_list}
    except:
        response = {'title':req['q'],'car_list':{}}

    response['fav_cars'] = db
    return render(request,'category.html',response)

def favorite_api(request):
    all_fav = FavoriteCar.objects.all().values()
    db = []
    for i in all_fav:
        if i['user_id'] == request.user.id:
            db.append(i['car_id'])
    if 'like' in request.POST:
        if request.POST['like'] not in db:
            tmp = FavoriteCar.objects.create(user_id=request.user.id,car_id=request.POST['like'])
            tmp.save()
    elif 'unlike' in request.POST and db:
        tmp = FavoriteCar.objects.get(user_id=request.user.id,car_id=request.POST['unlike'])
        tmp.delete()
    if 'q' in request.POST:
        return redirect('/category.html?q=' + request.POST['q'])
    else:
        return redirect('/favorite_car_list')

def favorite_car_list(request):
    all_fav = FavoriteCar.objects.all().values()
    db = []
    for i in all_fav:
        if i['user_id'] == request.user.id:
            tmp = i['car_id']
            tmp = Car.objects.get(pk=tmp)
            db.append(tmp)
    return render(request,'favorite-car.html',{'cars':db})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        user_dict = {'username':username, 'password':password}
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            message = {'message':'Invalid username or password'}
            return render(request, 'login.html', message)
    
    else :
        return render(request, 'login.html')

def logout_user(request):
    request.session.flush()
    logout(request)
    return redirect('/')

def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.profileImage = form.cleaned_data.get('image')
            user.save()
            return redirect('/login.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})


@csrf_exempt
def articles(request):
    data = json.loads(request.body)
    article = Article.objects.create(
        title = data['title'],
        date = data['date'],
        content = data['content']
    )

    article_list = []

    article_list.append({
        'id' : article.id,
        'title': article.title,
        'date': article.date,
        'content': article.content,

    })
    return JsonResponse({
        'article' : article_list
    })

@csrf_exempt
def likearticles(request):
    global counter
    global id
    data = json.loads(request.body)

    articles = Article.objects.get(id= data['id'])
    articles.like += 1

    temp_id = data['id']

    if ((counter <= 0) & (id != temp_id)):
        counter += 1
        id = data['id']
        articles.save()
    
    elif(id == temp_id):
        counter = 0

    return JsonResponse({
        'likeCount' : articles.like
    })
