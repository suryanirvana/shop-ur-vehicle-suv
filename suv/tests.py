from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, LiveServerTestCase
from django.test import *
from django.http import HttpRequest
from selenium import webdriver
from .views import *
from .models import *
import datetime
import time

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

    def test_category_user(self):
        # Test Like
        category = Category.objects.create(car_type="suv")
        category.save()

        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        password='volcano_sauce'
        email = 'test@test.com'

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        username2 = "hahahihi"
        email2 = "sjdaldjdlkas@gmail.com"
        password2 = "ajdjasl;jflkasdjlfkjasdl;jf;ldasjlkfaslkdjfoi;asdjop"
        user2 = User.objects.create_user(username=username2, email=email2, password=password2)
        user2.save()
     
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        
        self.client.login(username=username, password=password)
        response =  self.client.get('/category.html?q=SUV')
        self.assertEqual(response.status_code,200)

        # Test Like
        response =  self.client.post('/favorite_api',{'like':car.id , 'q':category.car_type})
        self.assertEqual(response.status_code,302)

        self.client.login(username=username2, password=password2)

        response =  self.client.get('/category.html?q=SUV')
        self.assertEqual(response.status_code,200)


    def test_favorite_api(self):
        # Test Like
        category = Category.objects.create(car_type="suv")
        category.save()

        name = "Avanza"
        username = "Bejo Paijo"
        year = "2015"
        city = "Bekasi"
        price = 500000
        description = "An avanza minibus"
        password='volcano_sauce'
        email = 'test@test.com'

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
     
        car = Car.objects.create(name=name,username=username,category=category,year=year,city=city,price=price,description=description)
        car.save()
        
        self.client.login(username=username, password=password)

        response =  self.client.post('/favorite_api',{'like':car.id , 'q':category.car_type})
        self.assertEqual(response.status_code,302)

        # Test Disike
        response =  self.client.post('/favorite_api',{'unlike':car.id , 'q':category.car_type})
        self.assertEqual(response.status_code,302)

class FunctionalTest(LiveServerTestCase):
    def setUp(self) :
        title = "A New Avaza Car For Rent"
        date = "2017-12-11"
        content = "A new cheap car is for rent."
        
        article = Article.objects.create(title=title,date = date, content = content)

        super().setUp()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')
    
    def tearDown(self) :
        self.driver.quit()
        super().tearDown()

    def test_user_register_then_login_then_logout(self) :
        self.driver.get(self.live_server_url)
        response_content = self.driver.page_source

        self.assertIn('Register', response_content)

        time.sleep(5)

        # Test when user signing up a new account
        self.driver.find_element_by_id('register').click()

        first_name = 'Functional'
        last_name = 'Test'
        username = 'FunctionalTest'
        email = 'functional@test.com'
        password = 'WebDesign&Pr0gr4mm1n9'
        url_image = 'https://i.picsum.photos/id/1005/5760/3840.jpg'

        time.sleep(5)

        for i in first_name:
            self.driver.find_element_by_id('id_first_name').send_keys(i)
            time.sleep(0.1)

        for i in last_name:
            self.driver.find_element_by_id('id_last_name').send_keys(i)
            time.sleep(0.1)

        for i in username:
            self.driver.find_element_by_id('id_username').send_keys(i)
            time.sleep(0.1)
        
        for i in email:
            self.driver.find_element_by_id('id_email').send_keys(i)
            time.sleep(0.1)

        for i in password:
            self.driver.find_element_by_id('id_password1').send_keys(i)
            time.sleep(0.1)

        for i in password:
            self.driver.find_element_by_id('id_password2').send_keys(i)
            time.sleep(0.1)
        
        for i in url_image:
            self.driver.find_element_by_id('id_image').send_keys(i)
            time.sleep(0.1)
        
        self.driver.find_element_by_id('signUp').click()

        time.sleep(5)

        # Test when user wants to log in
        for i in username:
            self.driver.find_element_by_id('username').send_keys(i)
            time.sleep(0.1)
        
        for i in password:
            self.driver.find_element_by_id('password').send_keys(i)
            time.sleep(0.1)
        
        self.driver.find_element_by_id('logIn').click()

        time.sleep(5)

        response_content = self.driver.page_source
        self.assertIn('FunctionalTest', response_content)

        self.driver.find_element_by_id('register').click()

        # Test when user wants to log out
        self.driver.find_element_by_id('logOut').click()

        time.sleep(5)

        response_content = self.driver.page_source
        self.assertIn('Register', response_content)
    
    def test_when_account_doesnt_exist_or_invalid_username_or_password(self):
        self.driver.get(self.live_server_url)
        response_content = self.driver.page_source

        self.assertIn('Register', response_content)

        time.sleep(5)

        # Test when user signing up a new account
        self.driver.find_element_by_id('register').click()

        time.sleep(5)
        
        self.driver.find_element_by_id('logIn').click()

        self.driver.find_element_by_id('username').send_keys("FunctionalTest")
        self.driver.find_element_by_id('password').send_keys("FunctionalTest")

        time.sleep(5)

        self.driver.find_element_by_id('logIn').click()

        response_content = self.driver.page_source
        self.assertIn("Invalid username or password", response_content)
    
    def test_create_article_return_article(self) :
        self.driver.get(self.live_server_url)
        response_content = self.driver.page_source

        self.assertIn('Article', response_content)

        time.sleep(5)

        # Test when user signing up a new account
        self.driver.find_element_by_id('articleBtn').click()

        title = 'FunctionalTest'
        date = '2020-12-12'
        content = 'FunctionalTest Content'

        time.sleep(5)

        for i in title:
            self.driver.find_element_by_id('id_title').send_keys(i)
            time.sleep(0.1)

        for i in date:
            self.driver.find_element_by_id('id_date').send_keys(i)
            time.sleep(0.1)

        for i in content:
            self.driver.find_element_by_id('id_content').send_keys(i)
            time.sleep(0.1)
        
        self.driver.find_element_by_id('submitBtn').click()

        time.sleep(5)  

        response_content = self.driver.page_source

        self.assertIn("FunctionalTest", response_content)
        self.assertIn("2020-12-12", response_content)
        self.assertIn("FunctionalTest Content", response_content)
    
    def test_like_article(self) :
        self.driver.get(self.live_server_url)
        response_content = self.driver.page_source

        self.assertIn('Register', response_content)

        time.sleep(5)

        # Test when user signing up a new account
        self.driver.find_element_by_id('register').click()

        first_name = 'Functional'
        last_name = 'Test'
        username = 'FunctionalTest'
        email = 'functional@test.com'
        password = 'WebDesign&Pr0gr4mm1n9'
        url_image = 'https://i.picsum.photos/id/1005/5760/3840.jpg'

        time.sleep(5)

        for i in first_name:
            self.driver.find_element_by_id('id_first_name').send_keys(i)
            time.sleep(0.1)

        for i in last_name:
            self.driver.find_element_by_id('id_last_name').send_keys(i)
            time.sleep(0.1)

        for i in username:
            self.driver.find_element_by_id('id_username').send_keys(i)
            time.sleep(0.1)
        
        for i in email:
            self.driver.find_element_by_id('id_email').send_keys(i)
            time.sleep(0.1)

        for i in password:
            self.driver.find_element_by_id('id_password1').send_keys(i)
            time.sleep(0.1)

        for i in password:
            self.driver.find_element_by_id('id_password2').send_keys(i)
            time.sleep(0.1)
        
        for i in url_image:
            self.driver.find_element_by_id('id_image').send_keys(i)
            time.sleep(0.1)
        
        self.driver.find_element_by_id('signUp').click()

        time.sleep(5)

        # Test when user wants to log in
        for i in username:
            self.driver.find_element_by_id('username').send_keys(i)
            time.sleep(0.1)
        
        for i in password:
            self.driver.find_element_by_id('password').send_keys(i)
            time.sleep(0.1)
        
        self.driver.find_element_by_id('logIn').click()

        time.sleep(5)

        response_content = self.driver.page_source
        self.assertIn('FunctionalTest', response_content)

        self.driver.find_element_by_id('articleBtn').click()

        time.sleep(5)

        self.driver.find_element_by_id('likeBtn1').click()

        response_content = self.driver.page_source
        self.assertIn('Likes: ', response_content)
        self.assertIn('1', response_content)