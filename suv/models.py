from django.db import models

# Create your models here.
class Category(models.Model):
    car_type = models.TextField(max_length=1000)

class Car(models.Model):
    name = models.TextField(max_length=1000)
    username = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.TextField(max_length=1000)
    city = models.TextField(max_length=1000)
    price = models.TextField(max_length=1000,default=0)
    description = models.TextField(max_length=1000,default="")
    car_image = models.ImageField(null=True, blank=True, upload_to="{% static 'img' %}")

class Article(models.Model):
    title = models.TextField(max_length=1000)
    date = models.TextField(max_length=1000)
    content = models.TextField(max_length=1000)

class Review(models.Model):
    username = models.TextField(max_length=1000)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    created_date = models.TextField(max_length=1000)
    rating = models.TextField(max_length=1000)

class Transaction(models.Model):
    name = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.TextField(max_length=1000)
    city = models.TextField(max_length=1000)
    date = models.TextField(max_length=1000)