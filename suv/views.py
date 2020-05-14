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
    response = {'article_list':Article.objects.all(), 'articleForm':ArticleForm()}
    return render(request,'articles.html',response)

def category(request):
    #Get GET REQUEST
    req = request.GET
    username = "admin"
    fav_cars  =  load_db()[username]
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
        

    response['fav_cars'] = fav_cars
    return render(request,'category.html',response)

def load_db():
    with open("./favorite.json") as f:
        like_db = json.load(f)
    return like_db

def favorite_api(request):
    username = 'admin'
    db = load_db()
    if username not in db:
        db[username] = []
    if 'like' in request.POST:
        if request.POST['like'] not in db[username]:
            db[username].append(int(request.POST['like']))
    elif 'unlike' in request.POST:
        db[username].remove(int(request.POST['unlike']))
    with open("./favorite.json", 'w') as fp:
        json.dump(db, fp)
    return redirect('/category.html?q=' + request.POST['q'])

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
    data = json.loads(request.body)

    articles = Article.objects.get(id= data['id'])
    articles.like += 1
    articles.save()


    # response = str()

    return JsonResponse({
        'likeCount' : articles.like
    })