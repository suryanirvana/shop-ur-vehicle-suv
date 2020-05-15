from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

CAR_TYPE = [
    ('SUV','SUV'),
    ('CUV', 'CUV'),
    ('SEDAN','SEDAN'),
]

class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))

class ReviewForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))
    car = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))
    created_date = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))
    rating = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '100',
    }))

class TransactionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Please enter your car name',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    car_type = forms.CharField(widget=forms.Select(choices=CAR_TYPE))
    year = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'From what year is it?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Your location?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    date = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'maxlength' : '1000',
    }))

class CarForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Please enter your car name',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    car_type = forms.CharField(widget=forms.Select(choices=CAR_TYPE))
    year = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'From what year is it?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Your location?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    price = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Price?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Description?',
        'type' : 'text',
        'maxlength' : '1000',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))

class SignUpForm(UserCreationForm):
    image = forms.URLField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'image')