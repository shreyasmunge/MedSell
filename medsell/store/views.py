from django.shortcuts import render
from .models import Products

def home(request):
    return render(request,'store/home.html')

def products(request):
    products=Products.objects.all()  #retrive products from db
    return render(request,'store/products.html',{'products':products})#products:prodcuts passes data from view to templates it is a dictionay
