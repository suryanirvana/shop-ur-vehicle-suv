from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    response = {}
    return render(request,'index.html',response)

def article(request):
    response = {'article_list':Article.objects.all().values()}
    print(Article.objects.all().values())
    return render(request,'articles.html',response)