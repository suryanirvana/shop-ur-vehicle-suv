from django.test import TestCase
from django.test import Client
from django.test import *

#Importing Models
from .models import *

# TDD Unit Tests
#by Fransiscus Emmanuel Bunaren
class SUVTest(TestCase):
    #For testing whether category can be accessed or not
    def test_category_response(self):
        response = Client().get('/category.html')
        self.assertEqual(response.status_code,200)

    #For testing whether homepage can be accessed or not
    def test_index_response(self):
        response = Client().get('/index.html')
        self.assertEqual(response.status_code,200)

        response = Client().get('/')
        self.assertEqual(response.status_code,200)

    #For testing get request
    def test_get_response(self):
        response = Client().get('/cars.html?q=minibus')
        self.assertEqual(response.status_code,200)

        #Check it gives response
        new_response = self.client.get('/cars.html?q=minibus')
        html_response = new_response.content.decode('utf8')
        self.assertTrue(html_response)

    #For testing model "Category"
    def test_model_category(self):
        #Make new category
        cat = Category.objects.create(car_type="minibus")
        self.assertEqual(cat.car_type,"minibus")

    '''
    For testing model "Car" 
    whether it behaves accoring to what we expect or not
    
    =========================
    Car Class Plan
    =========================
    Name
    User name (owner)
    Category
    Year
    City
    Price (per day)
    Description
    '''

    def test_model_car(self):
        #Create new Category
        category = Category.objects.create(car_type="minibus")
        category.save()

        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)

        #Check Car Name
        self.assertEqual(car.name , name)
        #Check for username
        self.assertEqual(car.username,username)
        #Check for category
        self.assertEqual(car.category,category)
        #Check for year
        self.assertEqual(car.year,year)
        #Check for city
        self.assertEqual(car.city,city)
        #Check for price
        self.assertEqual(car.price, price)
        #Check for description
        self.assertEqual(car.description, description)

    '''
    Test Article Model
    ===================
    Title
    Date
    Content
    '''
    def test_article_model(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        self.assertEqual(article.title,title)
        self.assertEqual(article.date,date)
        self.assertEqual(article.content,content)

    #Test Article Views Response
    def test_article_response(self):
        response = Client().get('/articles.html')
        self.assertEqual(response.status_code,200)

    #Test Cars View
    def test_cars_response(self):
        response = Client().get('/cars.html')
        self.assertEqual(response.status_code,200)
        