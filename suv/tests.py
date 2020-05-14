from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.test import Client
from django.test import *
from .views import *
from django.http import HttpRequest
#Importing Models
from .models import *
import datetime

# TDD Unit Tests
class SUVTest(TestCase):
    # For testing rent
    def test_rent_response(self):
        response = Client().get('/rent.html')
        self.assertEqual(response.status_code,200)

    def test_rent(self):
        upload_file = open("./suv/static/img/test.png", 'rb')
        image = SimpleUploadedFile(upload_file.name, upload_file.read())
        response = Client().post('/rent.html',{'name':'test' , 'car_type' : 'suv' , 'year' : '2000' , 'location' : 'bekasi', 'owner':'apam', 'price' : '10000' , 'description' : 'yaaa', 'car_image' : str(image.read())})
        self.assertEqual(response.status_code,302)

    # For testing whether category can be accessed or not
    def test_category_response(self):
        response = Client().get('/category.html')
        category = Category.objects.create(car_type="suv")
        category.save()
        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        self.assertEqual(response.status_code,200)
    
    def test_category_response_with_q(self):
        category = Category.objects.create(car_type="suv")
        category.save()
        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        response = Client().get('/category.html?q=suv')
        self.assertEqual(response.status_code,200)

    def test_category_response_with_price(self):
        category = Category.objects.create(car_type="suv")
        category.save()
        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        response = Client().get('/category.html?price=500000')
        self.assertEqual(response.status_code,200)

    def test_category_response_with_year(self):
        category = Category.objects.create(car_type="suv")
        category.save()
        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        response = Client().get('/category.html?year=2015')
        self.assertEqual(response.status_code,200)

    def test_category_response_with_city(self):
        category = Category.objects.create(car_type="suv")
        category.save()
        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        response = Client().get('/category.html?city=bekasi')
        self.assertEqual(response.status_code,200)
    
    def test_category_response_wrong_url(self):
        response = Client().get('/category.html?a=bekasi')
        html_response = response.content.decode('utf8')
        self.assertIn('No matching car found.', html_response)

    def test_category_response_not_found(self):
        response = Client().get('/category.html?price=10')
        html_response = response.content.decode('utf8')
        self.assertIn('No matching car found.', html_response)

    # For testing whether homepage can be accessed or not
    def test_index_response(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        response = Client().get('/')
        self.assertEqual(response.status_code,200)

    #For testing get request
    def test_get_response(self):

        #Check it gives response
        new_response = self.client.get('/cars.html?q=suv')
        html_response = new_response.content.decode('utf8')
        self.assertTrue(html_response)

    #For testing model "Category"
    def test_model_category(self):
        #Make new category
        cat = Category.objects.create(car_type="suv")
        self.assertEqual(cat.car_type,"suv")

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
        category = Category.objects.create(car_type="suv")
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
        
    def test_url_review(self):
        response = Client().get('/review.html')
        self.assertEqual(response.status_code, 200)

    def test_url_rent(self):
        response = Client().get('/rent.html')
        self.assertEqual(response.status_code, 200)

    def test_url_transaction(self):
        response = Client().get('/transaction.html')
        self.assertEqual(response.status_code, 200)
    
    def test_url_post(self):
        response = Client().post('/transaction.html',{'name' : 'apan' , 'car_type':'suv', 'year' : '2000', 'location' : 'Bandung', 'date' : datetime.datetime.today()})
        self.assertEqual(response.status_code, 302)

    def test_review_landing_page_is_completed(self):
        request = HttpRequest()
        response = review(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Review', html_response)

    def test_rent_landing_page_is_completed(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        request = HttpRequest()
        response = rent(request)
        html_response = response.content.decode('utf8')
        self.assertTemplateUsed(Client().get(path=''), 'index.html')

    def test_rent_transaction_page_is_completed(self):
        request = HttpRequest()
        response = transaction(request)
        html_response = response.content.decode('utf8')
        self.assertTemplateUsed(Client().get(path='/transaction.html'), 'transaction.html')

    def test_contains_question_in_title1(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        response = Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("Looking for a nice ride?", response_content)

    def test_contains_question_in_title2(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        response = Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("We've got you cover!", response_content)

    def test_contains_question_in_title3(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        response = Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("Hello there! we are the development group of this project, we make this website in order to make a platform for those who want to rent a car or want your car to be rented. We took alot of effort in making this website so we hope you have the best experience when using this website. Happy Renting!", response_content)

    def test_contains_question_in_title4(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        response = Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("C A T E G O R Y", response_content)

    def test_contains_question_in_title5(self):
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)
        response = Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("A R T I C L E S", response_content)

    def test_create_review(self):
        category = Category.objects.create(car_type="suv")
        category.save()

        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        
        response = Client().post('/review.html', {'username':"Surya", 'car' : "Avanza", 'message': "Hello", 'created_date':datetime.datetime.today(), 'rating':'5'})
        
        self.assertEqual(response.status_code,302)

        self.assertEqual(1, Review.objects.all().count())