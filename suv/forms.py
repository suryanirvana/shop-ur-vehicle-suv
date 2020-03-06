from django import forms

class CarForm(forms.Form):
    name = models.TextField(max_length=1000)
    username = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.TextField(max_length=1000)
    city = models.TextField(max_length=1000)
    price = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)