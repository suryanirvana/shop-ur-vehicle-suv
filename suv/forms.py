from django import forms
from .models import *

CAR_TYPE = [
    ('SUV','SUV'),
    ('CUV', 'CUV'),
    ('SEDAN','SEDAN'),
]

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
    car_image = forms.FileField()